---
tags: [pentest,privesc]
---

# Privilege Escalation
## Linux
- `sudo -l` (misconfigured sudo), SUID `find / -perm -4000 2>/dev/null`.
- Kernel exploits, cron jobs, writable PATH, capabilities, `/etc/passwd` writable.
- Tools: LinPEAS, linux-smart-enumeration.
## Windows
- Unquoted service paths, weak service perms, AlwaysInstallElevated, token impersonation.
- Stored creds, GPP passwords, DLL hijacking.
- Tools: WinPEAS, PowerUp, Seatbelt.
Map to MITRE TA0004.
