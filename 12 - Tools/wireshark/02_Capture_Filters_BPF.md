---
tags: [wireshark, capture-filters, bpf]
tool: wireshark
---
# Capture Filters (BPF syntax)

Applied before capturing. Keywords: `host net port` + direction `src dst` + protocol.

| Filter | Captures |
|--------|----------|
| `host 10.0.0.5` | To/from that host |
| `src host 10.0.0.5` | From that host only |
| `dst host 10.0.0.5` | To that host only |
| `net 192.168.1.0/24` | That subnet |
| `port 80` | Any traffic on port 80 |
| `tcp port 443` | TCP 443 only |
| `udp port 53` | DNS |
| `portrange 1-1024` | Port range |
| `tcp` / `udp` / `icmp` / `arp` | Protocol only |
| `host 10.0.0.5 and port 80` | Combine with and/or/not |
| `not port 22` | Everything except SSH |
| `ether host aa:bb:cc:dd:ee:ff` | By MAC |
| `broadcast` / `multicast` | Broadcast/multicast only |

## Examples
```
host 10.0.0.5 and not port 22        # all of a host's traffic except SSH
net 192.168.1.0/24 and tcp port 80   # web traffic on the subnet
udp port 53                          # DNS only (small captures)
```
