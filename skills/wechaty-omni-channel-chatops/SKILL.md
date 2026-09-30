---
name: wechaty-omni-channel-chatops
description: Universal conversational AI agent gateway and ChatOps automation across WhatsApp, Telegram, WeChat, Lark, and Slack powered by Wechaty SDK.
---

# 💬 Wechaty Omni-Channel ChatOps (S122)

Universal Conversational Bot and ChatOps Gateway powered by **Wechaty** (`wechaty/wechaty` - 23.0k★). Unifies AI agent interactions across multiple enterprise and consumer messaging protocols through a single, typed SDK.

---

## 🌐 1. Supported Puppet Protocols

Wechaty abstracts different chat platforms via pluggable Puppets:
- **WhatsApp**: `@wechaty/puppet-whatsapp` (Web / Business API)
- **Telegram**: `@wechaty/puppet-telegram` (Bot API)
- **Lark / Feishu**: `@wechaty/puppet-lark`
- **Slack**: `@wechaty/puppet-slack`
- **WeChat**: `@wechaty/puppet-wechat` / `wechat4u`
- **Discord**: Pluggable community puppet bridges

---

## 🤖 2. Event-Driven Agent Lifecycle

```typescript
import { WechatyBuilder } from 'wechaty';

const bot = WechatyBuilder.build({
  name: 'dola-chatops-bot',
  puppet: 'wechaty-puppet-whatsapp',
});

bot.on('scan', (qrcode, status) => {
  console.log(`Scan QR Code to login: ${status}\nhttps://wechaty.js.org/qrcode/${encodeURIComponent(qrcode)}`);
});

bot.on('login', user => console.log(`User ${user} logged in`));

bot.on('message', async message => {
  if (message.self()) return;
  const text = message.text();
  
  // Route to Dola Omni-Auto Meta-Router
  if (text.startsWith('/omni-auto')) {
    const reply = await executeOmniAutoWorkflow(text);
    await message.say(reply);
  }
});

await bot.start();
```

---

## 🚀 3. Trigger & Workflows
- **Trigger**: `/omni-auto wechaty` atau `/chatops-gateway`
- **Sub-skills**:
  - `wechaty_bot_dispatcher`: Dispatcher pesan multi-kanal dengan deduplikasi pesan.
  - `wechaty_media_bridge`: Pengiriman dokumen PDF, presentasi PPTX, dan gambar hasil agen ke ruang chat.
  - `wechaty_room_moderator`: Manajemen interaksi grup dan izin eksekusi perintah admin.
