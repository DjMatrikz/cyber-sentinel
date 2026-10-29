---
tags: [wireless,alfa,adapter,hardware]
---

# Alfa AWUS036ACH
Popular pentest Wi-Fi adapter — RTL8812AU chipset, dual-band, monitor mode + packet injection.
- Needs the `rtl8812au` driver (DKMS) on Kali: `sudo apt install realtek-rtl88xxau-dkms`.
- Verify: `iwconfig` / `airmon-ng`. Enable monitor: `airmon-ng start wlan0`.
- Confirm injection: `aireplay-ng --test wlan0mon`.
- Interface often becomes `wlan0mon` in monitor mode.
Used in [[Wireless Reconnaissance]] and Operation Pantera capture.
