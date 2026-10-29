---
tags: [networking,arp]
---

# ARP (Address Resolution Protocol)
Maps IPv4 -> MAC on the local network. No authentication (the core weakness).
- `arp -a` shows the ARP cache.
- **Gratuitous ARP** — unsolicited reply, used legitimately and in spoofing.
**ARP spoofing / poisoning (MITRE T1557):** attacker claims to be the gateway -> MITM.
Detect: two IPs sharing one MAC; Wireshark `arp.duplicate-address-detected`.
Defense: Dynamic ARP Inspection (DAI), static ARP, port security.
Related: [[Bettercap]], [[MITRE ATT&CK Overview]]
