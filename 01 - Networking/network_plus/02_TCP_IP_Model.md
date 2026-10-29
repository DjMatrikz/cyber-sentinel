---
tags: [networkplus, tcpip, fundamentals]
exam: Network+
---
# TCP/IP Model (4 Layers) vs OSI

| TCP/IP Layer | Maps to OSI | Examples |
|--------------|-------------|----------|
| Application | OSI 5,6,7 | HTTP, DNS, FTP, SMTP |
| Transport | OSI 4 | TCP, UDP |
| Internet | OSI 3 | IP, ICMP, routing |
| Link / Network Access | OSI 1,2 | Ethernet, MAC, cabling |

## TCP vs UDP
| | TCP | UDP |
|---|-----|-----|
| Connection | Connection-oriented (3-way handshake) | Connectionless |
| Reliability | Guaranteed, ordered, retransmits | Best-effort, no guarantee |
| Speed | Slower, more overhead | Faster, lightweight |
| Use cases | Web, email, file transfer | DNS, DHCP, VoIP, streaming, games |

**3-way handshake:** SYN → SYN-ACK → ACK.
