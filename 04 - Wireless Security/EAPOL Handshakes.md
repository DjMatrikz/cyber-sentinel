---
tags: [wireless,eapol,handshake]
---

# EAPOL / 4-Way Handshake
WPA2 key exchange proving both sides know the PSK (without sending it).
- 4 EAPOL messages derive the PTK from PMK + nonces + MACs.
- **Capture it** (monitor mode) to attempt offline PSK recovery.
- Force a client to reconnect with a **deauth** to catch the handshake.
- Wireshark filter: `eapol`. Then crack with aircrack-ng/hashcat (mode 22000).
**Lab/authorized networks only.**
