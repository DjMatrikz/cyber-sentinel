---
tags: [nmap, timing, evasion, firewall]
tool: nmap
---
# Nmap Timing & Firewall Evasion

## Timing templates (-T)
| Flag | Name | Use |
|------|------|-----|
| `-T0` | Paranoid | IDS evasion, extremely slow |
| `-T1` | Sneaky | Slow, low profile |
| `-T2` | Polite | Less bandwidth |
| `-T3` | Normal | Default |
| `-T4` | Aggressive | Fast, reliable networks (common for labs) |
| `-T5` | Insane | Fastest, may miss results |

## Evasion / firewall options
| Flag | Purpose |
|------|---------|
| `-f` | Fragment packets |
| `-D RND:10` | Decoy scan (hide among fake source IPs) |
| `-S <IP>` | Spoof source address |
| `--source-port 53` | Scan from a trusted-looking port |
| `--data-length 25` | Append random data |
| `--mtu 16` | Custom fragment size |
| `--randomize-hosts` | Scan hosts in random order |

## Examples
```
nmap -T4 192.168.1.0/24          # fast lab scan
nmap -T2 -f 10.0.0.5             # slow + fragmented
nmap -D RND:5 10.0.0.5           # decoys
```
