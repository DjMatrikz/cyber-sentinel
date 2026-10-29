---
tags: [windows,internals]
---

# Windows Internals
- **Processes/threads**, handles, DLLs. Tools: Process Explorer, Process Monitor.
- **Registry:** HKLM, HKCU; Run keys = persistence (`...\CurrentVersion\Run`).
- **LSASS** holds credentials in memory -> Mimikatz target (T1003.001).
- **Tokens** — access tokens, impersonation, privilege escalation.
- **Services** — `services.msc`, `sc query`; misconfigured services = privesc.
- **UAC** — elevation prompts; bypass techniques exist.
