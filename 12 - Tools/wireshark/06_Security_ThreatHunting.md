---
tags: [wireshark, security, threat-hunting, forensics]
tool: wireshark
---
# Security & Threat-Hunting Filters

## Scan detection
```
tcp.flags.syn == 1 && tcp.flags.ack == 0      # SYN scan / connection attempts
tcp.flags == 0x000                            # NULL scan
tcp.flags.fin == 1 && tcp.flags.ack == 0      # FIN scan
tcp.flags.fin==1 && tcp.flags.push==1 && tcp.flags.urg==1   # Xmas scan
tcp.flags.reset == 1                          # lots of RSTs = closed ports being probed
```

## ARP spoofing / MITM (T1557)
```
arp.duplicate-address-detected                # Wireshark flags ARP poisoning
arp.opcode == 2                               # ARP replies (gratuitous = suspicious)
```
Two IPs mapping to one MAC in the ARP traffic = man-in-the-middle.

## Suspicious traffic
```
http.request.method == "POST" && http contains "cmd="   # possible webshell
dns.qry.name.len > 50                                    # possible DNS tunneling
tcp.port == 4444                                         # common reverse-shell port (Metasploit default)
tcp.flags.push == 1 && tcp.len > 0                       # interactive shells push small packets
 smb || smb2                                             # lateral movement / file shares
kerberos                                                 # AD auth (kerberoasting recon)
```

## Cleartext credentials (lab exercises)
```
http.authbasic                                # HTTP Basic auth (base64 creds)
ftp.request.command == "PASS"
telnet
frame contains "password"
```

**Workflow:** capture -> filter to the protocol -> right-click a packet -> **Follow > TCP Stream** to reassemble the whole conversation (see full HTTP request, login exchange, etc.).
