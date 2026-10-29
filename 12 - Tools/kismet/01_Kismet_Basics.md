---
tags: [kismet, wireless, recon, fundamentals]
tool: kismet
---
# Kismet Basics
Kismet is a passive wireless detector, sniffer, and IDS for Wi-Fi (plus Bluetooth, SDR, and more with plugins). It never transmits — it listens.

## What it does
- Discovers APs and clients without associating (passive).
- Extracts SSID, BSSID, channel, encryption, manufacturer, signal, capabilities.
- Captures management/data frames; flags WPA handshakes & PMKIDs.
- Logs to a `.kismet` database (SQLite) you can convert to pcap/CSV.
- Web UI dashboard at **http://localhost:2501**.

## Architecture
- **kismet_server** — the capturing/processing engine.
- **Data sources** — your capture interfaces (e.g. `wlan0`).
- **Web UI** — control + view (served on port 2501).
- **Logs** — `*.kismet` DB in your working directory.

## Needs
- A monitor-mode capable adapter (your **Alfa AWUS036ACH** / RTL8812AU).
- Monitor mode (Kismet can create `wlan0mon` for you).
**Passive/authorized use only.**
Related: [[02_Kismet_Commands]], [[05_Kismet_Filters_Views]], [[Aircrack-ng]], [[Wireshark]]
