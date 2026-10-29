---
tags: [networkplus, security, networksecurity]
exam: Network+
---
# Network Security Essentials (shared with Security+)

## Core concepts
- **CIA Triad:** Confidentiality, Integrity, Availability.
- **AAA:** Authentication, Authorization, Accounting (RADIUS, TACACS+).
- **Defense in depth:** layered controls.
- **Zero Trust:** never trust, always verify.

## Segmentation
- **VLAN** — logically separate networks on the same switch (isolate IoT, guests, etc.).
- **DMZ / screened subnet** — public-facing servers isolated from the internal LAN.
- **802.1X** — port-based network access control (authenticate before network access).

## Common attacks (Network+ level)
| Attack | What it does |
|--------|--------------|
| DoS / DDoS | Floods target to exhaust resources |
| MITM / on-path | Intercepts traffic between two parties |
| ARP spoofing | Poisons ARP cache to redirect traffic |
| DNS poisoning | Corrupts DNS to redirect users |
| VLAN hopping | Jumps between VLANs |
| Rogue AP / evil twin | Fake access point to capture traffic |
| MAC spoofing / flooding | Fakes/overwhelms MAC table |

## Hardening
Disable unused ports, change default creds, patch firmware, use strong encryption (WPA3, TLS), enable logging, implement MFA.
