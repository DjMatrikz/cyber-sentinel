---
tags: [esp32, marauder, wireless, hardware]
tool: esp32-marauder
---
# ESP32 Marauder — Basics
Open-source Wi-Fi/Bluetooth testing firmware for ESP32 boards. Pairs well with a Flipper Zero or runs standalone (screen + SD).

## What it does (authorized/lab only)
- **Wi-Fi:** scan APs & stations, list SSIDs, sniff probe requests, capture **EAPOL handshakes** → PCAP, beacon analysis, channel hopping.
- **Packet capture** to SD → analyze in [[Wireshark]].
- **Bluetooth/BLE:** scan/sniff.
- Deauth/beacon features exist but are **illegal on networks you don't own** — lab only.

## Common boards
- ESP32-WROOM / WROVER dev kits
- **AC Dual C5** (ESP32-C5HR8) — dual-band Wi-Fi 6, used with Flipper (your board)
- Marauder-ready devices (M5Stack, etc.)

## Board + Flipper
The ESP32 runs Marauder; the Flipper acts as screen/controller over GPIO/serial. Captures land on the Flipper SD or the board's SD.
Related: [[02_esptool_Reference]], [[03_Download_Mode_Recovery]], [[Wireshark]], [[EAPOL Handshakes]]
