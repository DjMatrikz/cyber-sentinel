---
tags: [pentest,enumeration]
---

# Enumeration
Extract detail from discovered services:
- **SMB:** `enum4linux -a`, `smbclient -L`, `crackmapexec smb`.
- **Web:** `gobuster dir`, `ffuf`, `nikto`, `whatweb`.
- **DNS:** zone transfer `dig axfr`, subdomain brute.
- **SNMP:** `snmpwalk -c public`.
- **Users:** AD enum, RID cycling.
Goal: usernames, shares, versions, misconfigs -> attack surface. See [[Nmap]], [[Service OS Detection]].
