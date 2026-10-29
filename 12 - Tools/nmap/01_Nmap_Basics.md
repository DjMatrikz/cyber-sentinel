---
tags: [nmap, tools, scanning, recon]
tool: nmap
---
# Nmap Basics

Nmap (Network Mapper) — open-source tool for network discovery and security auditing.

## Syntax
```
nmap [scan type] [options] {target}
```

## Target specification
| Example | Meaning |
|---------|---------|
| `nmap 192.168.1.1` | Single host |
| `nmap 192.168.1.1-50` | Range |
| `nmap 192.168.1.0/24` | Whole subnet (CIDR) |
| `nmap scanme.nmap.org` | Hostname |
| `nmap -iL targets.txt` | Read targets from a file |
| `nmap 192.168.1.0/24 --exclude 192.168.1.1` | Exclude a host |

## First commands to know
```
nmap 192.168.1.1              # quick scan of top 1000 ports
nmap -v 192.168.1.1           # verbose
nmap -A 192.168.1.1           # aggressive: OS, version, scripts, traceroute
nmap -sn 192.168.1.0/24       # ping sweep — just find live hosts
```

**Authorized use only. Scan only networks and hosts you own or have written permission to test.**
