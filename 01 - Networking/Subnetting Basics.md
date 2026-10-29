---
tags: [networking,subnetting]
---

# Subnetting
## Private ranges (RFC 1918)
10.0.0.0/8 · 172.16.0.0/12 · 192.168.0.0/16 · APIPA 169.254.0.0/16
## CIDR cheat
|CIDR|Mask|Hosts|
|----|----|-----|
|/24|255.255.255.0|254|
|/25|.128|126|
|/26|.192|62|
|/27|.224|30|
|/28|.240|14|
|/29|.248|6|
|/30|.252|2|
Usable hosts = 2^(host bits) - 2. Subnets = 2^(borrowed bits).
