---
tags: [networkplus, services, dns, dhcp]
exam: Network+
---
# Core Network Services

## DNS (Domain Name System)
Resolves names → IPs. Port 53.
| Record | Purpose |
|--------|---------|
| A | Hostname → IPv4 |
| AAAA | Hostname → IPv6 |
| CNAME | Alias to another name |
| MX | Mail server |
| PTR | Reverse (IP → name) |
| TXT | Text (SPF, DKIM, verification) |
| NS | Name server for the zone |

## DHCP (Dynamic Host Configuration Protocol)
Auto-assigns IP config. Ports 67/68. Process = **DORA**:
**D**iscover → **O**ffer → **R**equest → **A**cknowledge.
Provides: IP, subnet mask, default gateway, DNS. **Scope** = pool of addresses. **Reservation** = fixed IP by MAC.

## NAT (Network Address Translation)
Maps private IPs → public IP. **PAT** (overload) = many private to one public via ports (home routers).
