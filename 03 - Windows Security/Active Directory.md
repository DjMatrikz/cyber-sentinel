---
tags: [windows,activedirectory,ad,redteam]
---

# Active Directory
Central identity/auth for Windows domains. Core: Domain Controllers, OUs, GPOs, Kerberos.
## Attack path concepts
- **Enumeration:** BloodHound/SharpHound map attack paths; `net user /domain`, `net group`.
- **Kerberoasting:** request service tickets, crack offline (SPN accounts).
- **AS-REP roasting:** accounts without pre-auth.
- **Pass-the-Hash / Pass-the-Ticket:** reuse NTLM hash / Kerberos ticket (T1550).
- **DCSync:** replicate credentials from DC (needs rights).
- **Golden/Silver tickets:** forge Kerberos tickets with krbtgt hash.
Defense: tiered admin, LAPS, disable NTLM, monitor 4768/4769/4624 events.
Related: [[MITRE ATT&CK Overview]], [[Event Logs]]
