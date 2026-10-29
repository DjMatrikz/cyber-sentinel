---
tags: [flipper, hardware, basics]
tool: flipper-zero
---
# Flipper Zero — Basics
Portable multi-tool for pentesting, hardware hacking, and RF hobby work. Built around radios + GPIO.

## Hardware radios/interfaces
- **Sub-GHz** (300–928 MHz, CC1101 chip) — remotes, sensors, some IoT.
- **125 kHz RFID** — low-freq access cards/fobs (EM4100, HID Prox, Indala).
- **NFC / 13.56 MHz** — high-freq cards (MIFARE Classic/Ultralight, NTAG, some access).
- **Infrared** — universal remote (TVs, ACs).
- **iButton / 1-Wire** — Dallas keys (some building/elevator keys).
- **GPIO pins** — connect modules (ESP32/Marauder, NRF24, sensors, debugging).
- **BadUSB** — acts as a USB keyboard (HID) to run scripts.
- **Bluetooth LE + USB-C + microSD.**

## Navigation
D-pad + OK + Back. Apps live in the main menu; extra apps on the SD card (`/apps`). Settings under the gear.

**Golden rule:** use only on devices/cards/frequencies you own or are authorized + legally allowed to use. Transmitting on some frequencies is illegal.
Related: [[02_Apps_Explained]], [[03_Flashing_Momentum]], [[04_Settings_and_Fixes]], [[05_When_To_Use_What]]
