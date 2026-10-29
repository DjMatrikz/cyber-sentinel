---
tags: [wireshark, display-filters, tcp, udp, ip, icmp]
tool: wireshark
---
# Core Protocol Display Filters

## IP / addressing
```
ip.addr == 10.0.0.5          # source or destination
ip.src == 10.0.0.5
ip.dst == 10.0.0.5
ip.addr == 192.168.1.0/24    # whole subnet
!(ip.addr == 10.0.0.5)       # exclude a host
ip.ttl < 10                  # low TTL (traceroute, possible spoofing)
eth.addr == aa:bb:cc:dd:ee:ff
```

## TCP
```
tcp.port == 443
tcp.flags.syn == 1 && tcp.flags.ack == 0    # SYN only = connection attempts / scans
tcp.flags.reset == 1                        # RST = refused/closed
tcp.analysis.retransmission                 # retransmits (packet loss / problems)
tcp.analysis.flags                          # all TCP "expert" problems
tcp.stream == 3                             # one specific conversation
tcp.len > 0                                 # packets carrying data
```

## UDP / ICMP
```
udp.port == 53
icmp                     # all ICMP
icmp.type == 8           # echo request (ping out)
icmp.type == 0           # echo reply
icmp.type == 3           # destination unreachable
```

## Frame-level
```
frame contains "login"
frame.len > 1000
frame.time >= "2026-10-29 00:00:00"
```
