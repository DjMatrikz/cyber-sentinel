---
tags: [networking,vlans]
---

# VLANs
Logically segment one physical switch into separate broadcast domains.
- **Access port** — one VLAN (end device). **Trunk port** — carries many VLANs (802.1Q tagging).
- **Native VLAN** — untagged traffic on a trunk (set it to an unused VLAN for security).
**Why:** isolate IoT, guests, servers; limit blast radius; enforce policy.
**Attacks:** VLAN hopping (double-tagging, switch spoofing). Defense: disable DTP, set native VLAN unused, restrict trunks.
