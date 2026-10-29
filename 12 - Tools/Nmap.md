---
tags: [tools,nmap,scanning]
---

# Nmap
Network mapper — host discovery, port scanning, service/OS detection, NSE scripts.
```
nmap -sn 10.0.0.0/24          # live hosts
nmap -sV -sC -p- -T4 TARGET   # full scan + versions + scripts
nmap --script vuln TARGET     # vuln checks
```
**Full cheat-sheet pack lives in the `nmap/` folder** (scan types, NSE, evasion, recipes).
