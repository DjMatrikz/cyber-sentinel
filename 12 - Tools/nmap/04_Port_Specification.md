---
tags: [nmap, ports]
tool: nmap
---
# Nmap Port Specification

| Flag | Meaning |
|------|---------|
| `-p 80` | Single port |
| `-p 80,443,3389` | Specific ports |
| `-p 1-1000` | Range |
| `-p-` | All 65535 ports |
| `-p U:53,T:80` | UDP 53 and TCP 80 |
| `-F` | Fast — top 100 ports |
| `--top-ports 20` | Scan the N most common ports |
| `-r` | Scan ports in order (not randomized) |

## Examples
```
nmap -p- 192.168.1.1             # every port
nmap -p 22,80,443 192.168.1.1    # just these
nmap -F 192.168.1.1              # quick top 100
nmap --top-ports 1000 192.168.1.1
```
