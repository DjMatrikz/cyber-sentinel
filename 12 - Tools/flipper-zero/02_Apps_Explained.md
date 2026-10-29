---
tags: [flipper, apps, momentum]
tool: flipper-zero
---
# Flipper Apps — What Each One Does

## Sub-GHz
Capture, analyze, save, and (where legal) replay 300–928 MHz signals.
- **Read / Read RAW** — capture a signal (RAW grabs anything, decoded parses known protocols).
- **Saved** — replay stored signals.
- **Frequency Analyzer** — find the frequency a nearby remote transmits on.
- **Protocols:** fixed-code (replayable) vs **rolling code** (e.g. KeeLoq — NOT trivially replayable; cloning modern garages/cars is blocked/illegal).
Use: your own garage/gate/remote testing, RF learning. Region limits apply.

## 125 kHz RFID
Low-frequency access cards.
- **Read** an EM4100/HID Prox/Indala card → **Save** → **Emulate** or write to a T5577 blank.
- Use: clone *your own* access fob for testing.

## NFC (13.56 MHz)
High-frequency cards.
- **Read** MIFARE Classic/Ultralight, NTAG, bank-card UID (read-only; can't clone EMV).
- Save / emulate / write (depends on card type & keys).
- **Mifare Classic** keys via dictionary/nested attacks (Momentum extras). Use: your own cards.

## Infrared
- **Universal Remote** — TVs, ACs, projectors (great party trick, legit utility).
- **Learn** a remote → save → replay.

## iButton (1-Wire / Dallas)
- Read / save / emulate Dallas keys (some building/elevator/gym keys). Your own keys.

## GPIO / Hardware
- **GPIO pins** power/connect add-ons: ESP32 (Wi-Fi via Marauder), NRF24 (2.4 GHz), sensors.
- UART/SPI/I2C for debugging and connecting your AC Dual C5. See [[ESP32 Marauder Basics]].

## BadUSB
- Runs **Rubber Ducky-style** scripts (`.txt` DuckyScript) — Flipper emulates a keyboard and types/executes fast.
- Use: authorized red-team/awareness demos on your own machines only.

## U2F
- Acts as a hardware **2FA security key** (FIDO U2F) for your own accounts. Legit security use.

## Apps (FAP) / Momentum extras
- Extra community apps from the **Apps catalog** / Momentum asset packs: games, tools, NRF24 sniffers, sub-ghz playlist, etc. Stored in `/apps` on SD.
