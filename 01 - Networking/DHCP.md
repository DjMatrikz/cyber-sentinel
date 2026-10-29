---
tags: [networking,dhcp]
---

# DHCP
Auto-assigns IP config. Ports 67 (server) / 68 (client). Process = **DORA**: Discover, Offer, Request, Acknowledge.
Provides: IP, subnet mask, gateway, DNS, lease time.
- **Scope** = pool of addresses. **Reservation** = fixed IP by MAC.
- No DHCP -> APIPA (169.254.x.x).
**Attacks:** DHCP starvation, rogue DHCP server (MITM). Defense: DHCP snooping.
