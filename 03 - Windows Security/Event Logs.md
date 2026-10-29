---
tags: [windows,logs,blueteam,forensics]
---

# Windows Event Logs
`eventvwr.msc` or `Get-WinEvent`. Key IDs for security:
|ID|Meaning|
|--|-------|
|4624|Successful logon|
|4625|Failed logon|
|4634/4647|Logoff|
|4672|Admin logon (special privileges)|
|4688|Process creation|
|4720|User account created|
|4728/4732|Added to security group|
|4768/4769|Kerberos TGT/service ticket|
|7045|Service installed (persistence)|
|1102|Audit log cleared (suspicious!)|
Logon types: 2=interactive, 3=network, 10=RDP. Ship to a SIEM for hunting.
