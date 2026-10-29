---
tags: [wireless,recon,scanning]
---

# Wireless Reconnaissance
1. Put adapter in monitor mode: `airmon-ng start wlan0`.
2. Survey: `airodump-ng wlan0mon` — lists APs (BSSID, channel, ENC) and clients.
3. Target a channel/BSSID: `airodump-ng -c 6 --bssid AA:BB:.. -w cap wlan0mon`.
4. Capture handshake (optionally deauth to speed it).
Tools: airodump-ng, Kismet, Wireshark (monitor mode), ESP32 Marauder, Flipper.
Wireshark beacon filter: `wlan.fc.type_subtype == 0x08`.
