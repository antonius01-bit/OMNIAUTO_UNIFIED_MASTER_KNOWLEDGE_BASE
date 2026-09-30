"""
MiniMind-O Multimodal Omni Dataset Loader
Formats interleaved conversation text and Kyutai Mimi 8-codebook audio codec tokens.
"""

import os
import random
from typing import Dict, List, Optional, Any

try:
    import torch
    from torch.utils.data import Dataset, DataLoader
except ImportError:
    torch = None
    Dataset = object
    DataLoader = None

class SyntheticOmniDataset(Dataset):
    """
    Synthetic / Prototype Multimodal Dataset for MiniMind-O.
    Simulates:
    - Text tokens: Standard BPE/Byte token stream (32,000 vocab).
    - Audio tokens: 8-channel Kyutai Mimi discrete codebook tokens (2,048 codebook size).
    """
    def __init__(self, num_samples: int = 1000, seq_len: int = 256, vocab_size: int = 32000, audio_vocab_size: int = 2048):
        self.num_samples = num_samples
        self.seq_len = seq_len
        self.vocab_size = vocab_size
        self.audio_vocab_size = audio_vocab_size

    def __len__(self) -> int:
        return self.num_samples

    def __getitem__(self, idx: int) -> Dict[str, Any]:
        if torch is None:
            return {}
        
        # Synthetic input IDs
        input_ids = torch.randint(10, self.vocab_size, (self.seq_len,), dtype=torch.long)
        text_labels = input_ids.clone()
        
        # Mask 20% of text tokens as prompt (ignore_index = -100)
        prompt_len = self.seq_len // 5
        text_labels[:prompt_len] = -100

        # Synthetic 8-channel Mimi audio codec tokens
        audio_labels = torch.randint(0, self.audio_vocab_size, (self.seq_len, 8), dtype=torch.long)
        # Only compute audio loss on the assistant response segment
        audio_labels[:prompt_len, :] = -100

        return {
            "input_ids": input_ids,
            "text_labels": text_labels,
            "audio_labels": audio_labels
        }

def create_omni_dataloader(batch_size: int = 4, seq_len: int = 256, num_samples: int = 100) -> Any:
    if torch is None or DataLoader is None:
        return None
    ds = SyntheticOmniDataset(num_samples=num_samples, seq_len=seq_len)
    return DataLoader(ds, batch_size=batch_size, shuffle=True, pin_memory=True if torch.cuda.is_available() else False)
