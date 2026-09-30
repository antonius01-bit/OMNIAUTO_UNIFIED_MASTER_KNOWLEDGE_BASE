"""
MiniMind-O: 0.1B Parameter Multimodal Omni SLM Architecture
Features Thinker-Talker Dual-Path design with Kyutai Mimi Audio Codebook Heads.
Upstream Reference: jingyaogong/minimind-o
"""

import math
from dataclasses import dataclass
from typing import Optional, Tuple, List, Dict, Any

try:
    import torch
    import torch.nn as nn
    import torch.nn.functional as F
except ImportError:
    # Graceful fallback for environments before pip install torch
    torch = None
    nn = None
    F = None

@dataclass
class MiniMindOmniConfig:
    vocab_size: int = 32000           # Text vocabulary size
    hidden_size: int = 512            # ~0.1B model scale
    intermediate_size: int = 1376     # SwiGLU intermediate dimension
    num_hidden_layers: int = 8        # Efficient depth for consumer GPU / mobile
    num_attention_heads: int = 8      # Query heads
    num_key_value_heads: int = 2      # Grouped Query Attention (GQA)
    max_position_embeddings: int = 2048
    rms_norm_eps: float = 1e-5
    rope_theta: float = 10000.0
    
    # Audio Omni Parameters (Kyutai Mimi Codec)
    audio_vocab_size: int = 2048      # Codebook size per codebook
    num_audio_codebooks: int = 8      # 8 parallel codebooks for Mimi audio
    talker_hidden_size: int = 256     # Talker audio projector dimension
    audio_loss_weight: float = 0.5    # Weight lambda for acoustic loss

if torch is not None:
    class RMSNorm(nn.Module):
        def __init__(self, dim: int, eps: float = 1e-5):
            super().__init__()
            self.eps = eps
            self.weight = nn.Parameter(torch.ones(dim))

        def forward(self, x: torch.Tensor) -> torch.Tensor:
            norm = torch.rsqrt(x.pow(2).mean(-1, keepdim=True) + self.eps)
            return x * norm * self.weight

    def precompute_rope_frequencies(dim: int, max_seq_len: int, theta: float = 10000.0) -> torch.Tensor:
        freqs = 1.0 / (theta ** (torch.arange(0, dim, 2)[: (dim // 2)].float() / dim))
        t = torch.arange(max_seq_len)
        freqs = torch.outer(t, freqs)
        return torch.polar(torch.ones_like(freqs), freqs)

    def apply_rope(x: torch.Tensor, freqs_cis: torch.Tensor) -> torch.Tensor:
        x_complex = torch.view_as_complex(x.float().reshape(*x.shape[:-1], -1, 2))
        freqs_cis = freqs_cis[:x.shape[1]].unsqueeze(0).unsqueeze(2)
        x_rotated = torch.view_as_real(x_complex * freqs_cis).flatten(-2)
        return x_rotated.type_as(x)

    class MiniMindAttention(nn.Module):
        def __init__(self, config: MiniMindOmniConfig):
            super().__init__()
            self.config = config
            self.head_dim = config.hidden_size // config.num_attention_heads
            self.num_heads = config.num_attention_heads
            self.num_kv_heads = config.num_key_value_heads
            self.num_kv_groups = self.num_heads // self.num_kv_heads

            self.q_proj = nn.Linear(config.hidden_size, config.hidden_size, bias=False)
            self.k_proj = nn.Linear(config.hidden_size, self.num_kv_heads * self.head_dim, bias=False)
            self.v_proj = nn.Linear(config.hidden_size, self.num_kv_heads * self.head_dim, bias=False)
            self.o_proj = nn.Linear(config.hidden_size, config.hidden_size, bias=False)

        def forward(self, x: torch.Tensor, freqs_cis: torch.Tensor, mask: Optional[torch.Tensor] = None) -> torch.Tensor:
            B, S, _ = x.shape
            q = self.q_proj(x).view(B, S, self.num_heads, self.head_dim)
            k = self.k_proj(x).view(B, S, self.num_kv_heads, self.head_dim)
            v = self.v_proj(x).view(B, S, self.num_kv_heads, self.head_dim)

            q = apply_rope(q, freqs_cis)
            k = apply_rope(k, freqs_cis)

            # GQA expansion
            k = k.repeat_interleave(self.num_kv_groups, dim=2)
            v = v.repeat_interleave(self.num_kv_groups, dim=2)

            q = q.transpose(1, 2)
            k = k.transpose(1, 2)
            v = v.transpose(1, 2)

            scores = torch.matmul(q, k.transpose(-2, -1)) / math.sqrt(self.head_dim)
            if mask is not None:
                scores = scores + mask
            scores = F.softmax(scores, dim=-1)
            output = torch.matmul(scores, v).transpose(1, 2).contiguous().view(B, S, -1)
            return self.o_proj(output)

    class MiniMindSwiGLU(nn.Module):
        def __init__(self, config: MiniMindOmniConfig):
            super().__init__()
            self.gate_proj = nn.Linear(config.hidden_size, config.intermediate_size, bias=False)
            self.up_proj = nn.Linear(config.hidden_size, config.intermediate_size, bias=False)
            self.down_proj = nn.Linear(config.intermediate_size, config.hidden_size, bias=False)

        def forward(self, x: torch.Tensor) -> torch.Tensor:
            return self.down_proj(F.silu(self.gate_proj(x)) * self.up_proj(x))

    class MiniMindDecoderLayer(nn.Module):
        def __init__(self, config: MiniMindOmniConfig):
            super().__init__()
            self.attn_norm = RMSNorm(config.hidden_size, eps=config.rms_norm_eps)
            self.attn = MiniMindAttention(config)
            self.ffn_norm = RMSNorm(config.hidden_size, eps=config.rms_norm_eps)
            self.ffn = MiniMindSwiGLU(config)

        def forward(self, x: torch.Tensor, freqs_cis: torch.Tensor, mask: Optional[torch.Tensor] = None) -> torch.Tensor:
            h = x + self.attn(self.attn_norm(x), freqs_cis, mask)
            out = h + self.ffn(self.ffn_norm(h))
            return out

    class TalkerAudioHead(nn.Module):
        """
        Talker Head: Multi-Token Prediction (MTP) for Kyutai Mimi 8-codebook audio stream.
        """
        def __init__(self, config: MiniMindOmniConfig):
            super().__init__()
            self.config = config
            self.audio_projector = nn.Sequential(
                nn.Linear(config.hidden_size, config.talker_hidden_size),
                nn.SiLU(),
                nn.Linear(config.talker_hidden_size, config.talker_hidden_size)
            )
            # 8 discrete codebook classification heads
            self.codebook_heads = nn.ModuleList([
                nn.Linear(config.talker_hidden_size, config.audio_vocab_size, bias=False)
                for _ in range(config.num_audio_codebooks)
            ])

        def forward(self, thinker_hidden_states: torch.Tensor) -> List[torch.Tensor]:
            proj = self.audio_projector(thinker_hidden_states)
            logits = [head(proj) for head in self.codebook_heads]
            return logits

    class MiniMindOmniForCausalLM(nn.Module):
        """
        Complete MiniMind-O Multimodal Omni Architecture:
        - Thinker: Text & Multimodal reasoning backbone
        - Talker: Mimi discrete audio codec prediction heads
        """
        def __init__(self, config: MiniMindOmniConfig):
            super().__init__()
            self.config = config
            self.embed_tokens = nn.Embedding(config.vocab_size, config.hidden_size)
            self.layers = nn.ModuleList([MiniMindDecoderLayer(config) for _ in range(config.num_hidden_layers)])
            self.norm = RMSNorm(config.hidden_size, eps=config.rms_norm_eps)
            
            # Thinker text LM Head
            self.lm_head = nn.Linear(config.hidden_size, config.vocab_size, bias=False)
            
            # Talker Audio Head (Duplex streaming voice)
            self.talker = TalkerAudioHead(config)

            # Precomputed RoPE frequencies
            head_dim = config.hidden_size // config.num_attention_heads
            self.register_buffer(
                "freqs_cis", 
                precompute_rope_frequencies(head_dim, config.max_position_embeddings, config.rope_theta), 
                persistent=False
            )

        def forward(
            self,
            input_ids: torch.Tensor,
            text_labels: Optional[torch.Tensor] = None,
            audio_labels: Optional[torch.Tensor] = None # Shape: [Batch, Seq, 8]
        ) -> Dict[str, Any]:
            B, S = input_ids.shape
            x = self.embed_tokens(input_ids)
            freqs_cis = self.freqs_cis[:S]

            # Causal triangle mask
            mask = torch.full((S, S), float("-inf"), device=input_ids.device)
            mask = torch.triu(mask, diagonal=1)

            for layer in self.layers:
                x = layer(x, freqs_cis, mask)
            hidden_states = self.norm(x)

            # Thinker text output
            text_logits = self.lm_head(hidden_states)

            # Talker audio output (8 parallel codebooks)
            audio_logits = self.talker(hidden_states)

            total_loss = None
            text_loss = None
            audio_loss = None

            if text_labels is not None:
                # Text Next-Token-Prediction Loss
                shift_logits = text_logits[..., :-1, :].contiguous()
                shift_labels = text_labels[..., 1:].contiguous()
                text_loss = F.cross_entropy(
                    shift_logits.view(-1, self.config.vocab_size),
                    shift_labels.view(-1),
                    ignore_index=-100
                )
                total_loss = text_loss

            if audio_labels is not None:
                # Audio Codebook Loss across 8 heads
                audio_losses = []
                for k in range(self.config.num_audio_codebooks):
                    head_logits = audio_logits[k][..., :-1, :].contiguous()
                    head_targets = audio_labels[..., 1:, k].contiguous()
                    cb_loss = F.cross_entropy(
                        head_logits.view(-1, self.config.audio_vocab_size),
                        head_targets.view(-1),
                        ignore_index=-100
                    )
                    audio_losses.append(cb_loss)
                audio_loss = torch.stack(audio_losses).mean()

                if total_loss is not None:
                    total_loss = total_loss + self.config.audio_loss_weight * audio_loss
                else:
                    total_loss = audio_loss

            return {
                "loss": total_loss,
                "text_loss": text_loss,
                "audio_loss": audio_loss,
                "text_logits": text_logits,
                "audio_logits": audio_logits,
                "hidden_states": hidden_states
            }
