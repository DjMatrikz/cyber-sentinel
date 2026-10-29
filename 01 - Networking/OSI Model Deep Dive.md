---
tags: [networking,osi]
---

# OSI Model Deep Dive
| # | Layer | Unit | Devices | Examples |
|---|-------|------|---------|----------|
|7|Application|Data|-|HTTP, DNS, SMTP|
|6|Presentation|Data|-|TLS, JPEG, encoding|
|5|Session|Data|-|RPC, NetBIOS|
|4|Transport|Segment|-|TCP, UDP (ports)|
|3|Network|Packet|Router|IP, ICMP|
|2|Data Link|Frame|Switch|Ethernet, MAC, ARP|
|1|Physical|Bits|Hub, NIC|cables, RJ45|
Troubleshoot bottom-up or top-down. Encapsulation adds a header at each layer going down.
