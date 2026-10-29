---
tags: [networkplus, osi, fundamentals]
exam: Network+
---
# The OSI Model (7 Layers)

Mnemonic (top-down): **A**ll **P**eople **S**eem **T**o **N**eed **D**ata **P**rocessing.
Bottom-up: **P**lease **D**o **N**ot **T**hrow **S**ausage **P**izza **A**way.

| # | Layer | Role | Data unit | Examples |
|---|-------|------|-----------|----------|
| 7 | Application | User-facing services | Data | HTTP, FTP, DNS, SMTP |
| 6 | Presentation | Format, encrypt, compress | Data | TLS/SSL, JPEG, ASCII |
| 5 | Session | Open/maintain/close sessions | Data | NetBIOS, RPC, sockets |
| 4 | Transport | End-to-end delivery, ports | Segment (TCP) / Datagram (UDP) | TCP, UDP |
| 3 | Network | Logical addressing & routing | Packet | IP, ICMP, routers |
| 2 | Data Link | Physical addressing (MAC), framing | Frame | Ethernet, switches, ARP |
| 1 | Physical | Bits on the wire | Bits | Cables, hubs, NICs, RJ45 |

**Exam tips:**
- A **router** works at Layer 3; a **switch** at Layer 2; a **hub** at Layer 1.
- **Layer 3 switch** = switch that can also route.
- Encryption/formatting = Layer 6. Ports = Layer 4. MAC = Layer 2. IP = Layer 3.
