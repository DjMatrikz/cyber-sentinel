---
tags: [networkplus, ports, protocols]
exam: Network+
---
# Common Ports & Protocols (memorize these cold)

| Port | Protocol | TCP/UDP | Purpose |
|------|----------|---------|---------|
| 20/21 | FTP | TCP | File transfer (20=data, 21=control) |
| 22 | SSH / SCP / SFTP | TCP | Secure remote access |
| 23 | Telnet | TCP | Remote access (insecure) |
| 25 | SMTP | TCP | Sending email |
| 53 | DNS | TCP/UDP | Name resolution |
| 67/68 | DHCP | UDP | IP address assignment |
| 69 | TFTP | UDP | Trivial file transfer |
| 80 | HTTP | TCP | Web (unencrypted) |
| 110 | POP3 | TCP | Receiving email |
| 123 | NTP | UDP | Time sync |
| 143 | IMAP | TCP | Receiving email (sync) |
| 161/162 | SNMP | UDP | Network management |
| 389 | LDAP | TCP/UDP | Directory services |
| 443 | HTTPS | TCP | Web (encrypted/TLS) |
| 445 | SMB | TCP | Windows file sharing |
| 636 | LDAPS | TCP | Secure LDAP |
| 3389 | RDP | TCP | Remote Desktop |

**Secure vs insecure pairs:** Telnet(23)→SSH(22), HTTP(80)→HTTPS(443), FTP(21)→SFTP(22), LDAP(389)→LDAPS(636).
