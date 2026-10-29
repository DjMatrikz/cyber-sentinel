---
tags: [networkplus, devices, hardware]
exam: Network+
---
# Network Devices

| Device | OSI Layer | Function |
|--------|-----------|----------|
| Hub | 1 | Repeats signal to all ports (dumb, obsolete) |
| Switch | 2 | Forwards frames by MAC address |
| Router | 3 | Routes packets between networks by IP |
| Firewall | 3–7 | Filters traffic by rules (ports, IPs, apps) |
| Access Point (AP) | 2 | Provides wireless connectivity |
| Load balancer | 4–7 | Distributes traffic across servers |
| Proxy | 7 | Intermediary for requests (caching, filtering) |
| IDS/IPS | 3–7 | Detects (IDS) or blocks (IPS) malicious traffic |

**Key distinctions:**
- **Switch vs Hub:** switch is smart (MAC table, one collision domain per port); hub is dumb (one shared collision domain).
- **IDS vs IPS:** IDS *alerts* (passive, out-of-band); IPS *blocks* (active, in-line).
- **Router vs Firewall:** router connects networks; firewall controls what's allowed.
