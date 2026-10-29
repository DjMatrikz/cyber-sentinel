---
tags: [networkplus, subnetting, ipv4]
exam: Network+
---
# Subnetting & IP Addressing

## IPv4 classes
| Class | Range (1st octet) | Default mask | Default CIDR |
|-------|-------------------|--------------|--------------|
| A | 1–126 | 255.0.0.0 | /8 |
| B | 128–191 | 255.255.0.0 | /16 |
| C | 192–223 | 255.255.255.0 | /24 |
(127 = loopback. D=multicast, E=experimental.)

## Private ranges (RFC 1918)
- 10.0.0.0 – 10.255.255.255 (/8)
- 172.16.0.0 – 172.31.255.255 (/12)
- 192.168.0.0 – 192.168.255.255 (/16)
- APIPA (no DHCP): 169.254.0.0/16

## CIDR quick reference
| CIDR | Mask | Hosts usable |
|------|------|--------------|
| /24 | 255.255.255.0 | 254 |
| /25 | 255.255.255.128 | 126 |
| /26 | 255.255.255.192 | 62 |
| /27 | 255.255.255.224 | 30 |
| /28 | 255.255.255.240 | 14 |
| /29 | 255.255.255.248 | 6 |
| /30 | 255.255.255.252 | 2 |

**Formula:** usable hosts = 2^(host bits) − 2 (subtract network + broadcast).
**Subnets:** 2^(borrowed bits).
