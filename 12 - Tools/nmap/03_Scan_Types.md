---
tags: [nmap, scan-types, tcp, udp]
tool: nmap
---
# Nmap Scan Types

| Flag | Scan | Notes |
|------|------|-------|
| `-sS` | TCP SYN (stealth) | Default when root; fast, half-open, doesn't complete handshake |
| `-sT` | TCP connect | Full handshake; used when not root |
| `-sU` | UDP scan | Slow but finds UDP services (DNS, SNMP, DHCP) |
| `-sA` | TCP ACK | Maps firewall rules (filtered vs unfiltered) |
| `-sN` | TCP Null | No flags set — firewall evasion |
| `-sF` | TCP FIN | FIN flag only — evasion |
| `-sX` | Xmas | FIN+PSH+URG flags — evasion |
| `-sW` | TCP Window | Like ACK, uses window field |
| `-sO` | IP protocol | Which IP protocols a host supports |

## Examples
```
sudo nmap -sS 192.168.1.1        # stealth SYN scan
nmap -sT 192.168.1.1             # connect scan (no root)
sudo nmap -sU -top-ports 50 192.168.1.1   # top 50 UDP ports
sudo nmap -sS -sU 192.168.1.1    # TCP + UDP together
```
