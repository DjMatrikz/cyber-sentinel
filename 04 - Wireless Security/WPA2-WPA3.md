---
tags: [wireless,wpa2,wpa3,crypto]
---

# WPA2 / WPA3
- **WEP** — broken, never use. **WPA/TKIP** — weak. **WPA2 (AES-CCMP)** — standard. **WPA3 (SAE)** — current best.
- **WPA2-Personal** = PSK (shared password). **WPA2-Enterprise** = 802.1X/RADIUS per-user auth.
- **WPA2 weakness:** capture the 4-way handshake (EAPOL) -> offline dictionary/brute attack on the PSK.
- **WPA3 (SAE / Dragonfly)** — resists offline cracking, forward secrecy; downgrade/side-channel (Dragonblood) research exists.
Related: [[EAPOL Handshakes]], [[Aircrack-ng]], [[Hashcat]]
