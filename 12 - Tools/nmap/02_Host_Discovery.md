---
tags: [nmap, host-discovery, recon]
tool: nmap
---
# Nmap Host Discovery

Finding which hosts are up before scanning ports.

| Flag | Purpose |
|------|---------|
| `-sn` | Ping scan — discover hosts, no port scan |
| `-Pn` | Skip discovery — treat all hosts as online (use when ping is blocked) |
| `-PS<ports>` | TCP SYN ping (e.g. `-PS22,80,443`) |
| `-PA<ports>` | TCP ACK ping |
| `-PU<ports>` | UDP ping |
| `-PE` | ICMP echo request ping |
| `-PR` | ARP ping (default on local LAN — very fast/reliable) |
| `-n` | No DNS resolution (faster) |
| `-R` | Always resolve DNS |

## Examples
```
nmap -sn 192.168.1.0/24          # who's alive on my subnet
nmap -Pn 10.0.0.5                # scan even if it won't respond to ping
nmap -sn -PR 192.168.1.0/24      # ARP sweep (local network)
```
