---
tags: [flipper, guide, decision]
tool: flipper-zero
---
# When To Use What (quick decision guide)

| Goal | Use |
|------|-----|
| Clone *your* access fob (building/gym) | 125 kHz RFID (if LF) or NFC (if HF 13.56) — read → save → emulate/write |
| Not sure if a card is LF or HF | try **125 kHz RFID** first, then **NFC**; HF cards are more common now |
| Test *your* garage/gate remote | Sub-GHz → Read/Read RAW → Saved (fixed-code only; rolling-code is blocked) |
| Find what frequency a remote uses | Sub-GHz → **Frequency Analyzer** |
| Control a TV/AC | **Infrared → Universal Remote** |
| Wi-Fi scanning / EAPOL capture | **GPIO + ESP32 Marauder** (external board) — see [[ESP32 Marauder Basics]] |
| 2.4 GHz (mice/keyboards) | GPIO + **NRF24** module app |
| Authorized keystroke-injection demo | **BadUSB** with a DuckyScript on your own machine |
| Hardware 2FA key | **U2F** |
| Dallas/iButton key (your own) | **iButton** |
| Debug a dev board (UART/SPI) | **GPIO** |

## Reality checks
- **Rolling code** (modern cars, newer garages) = you CANNOT clone/replay it. By design + by law.
- **Bank cards (EMV):** Flipper can read the UID only — it cannot clone or charge them.
- **Encrypted access cards:** many corporate badges use crypto you can't trivially clone.
- **Transmitting** (Sub-GHz TX, deauth via Marauder) on anything you don't own / aren't licensed for is illegal. Reading/learning your own gear is fine.

This is a learning + authorized-testing tool. Keep it legal, keep it yours.
