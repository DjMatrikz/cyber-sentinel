---
tags: [networking,dns]
---

# DNS (Domain Name System)
Resolves names -> IPs. Port 53 (UDP queries, TCP zone transfers / large responses).
## Record types
| Record | Purpose |
|--------|---------|
|A|name -> IPv4|
|AAAA|name -> IPv6|
|CNAME|alias|
|MX|mail server|
|PTR|reverse (IP -> name)|
|TXT|SPF/DKIM/verification|
|NS|nameserver|
|SOA|zone authority|
## Tools
`nslookup example.com` · `dig example.com ANY` · `dig +short A example.com`
**Security:** DNS tunneling (exfil), cache poisoning, DNSSEC for integrity.
