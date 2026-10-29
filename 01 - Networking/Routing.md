---
tags: [networking,routing]
---

# Routing
Moves packets between networks (Layer 3).
- **Static** — manually set. **Dynamic** — protocols share routes.
- **Interior:** RIP (hop count), OSPF (link-state, cost), EIGRP. **Exterior:** BGP (the internet).
- **Default route** 0.0.0.0/0 — where unknown traffic goes.
- **NAT/PAT** — private <-> public IP translation.
`ip route` / `route print` / `traceroute` to inspect paths.
