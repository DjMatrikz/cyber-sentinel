---
tags: [nmap, nse, scripts, vulnerability]
tool: nmap
---
# Nmap Scripting Engine (NSE)

NSE runs Lua scripts for advanced detection, vuln checks, and even exploitation.
Scripts live in categories: auth, broadcast, brute, default, discovery, dos,
exploit, external, fuzzer, intrusive, malware, safe, version, vuln.

| Flag | Purpose |
|------|---------|
| `-sC` | Run default scripts (safe, useful) |
| `--script <name>` | Run a specific script |
| `--script <category>` | Run a whole category |
| `--script-args <args>` | Pass arguments |
| `--script-help <name>` | Explain a script |

## Examples
```
nmap -sC 192.168.1.1                        # default scripts
nmap --script vuln 192.168.1.1              # check known vulnerabilities
nmap --script http-enum 192.168.1.1         # enumerate web dirs
nmap --script smb-os-discovery 192.168.1.1  # SMB/Windows info
nmap --script ssl-cert -p 443 192.168.1.1   # TLS cert details
nmap -p 445 --script smb-vuln-ms17-010 192.168.1.1  # EternalBlue check
```

**Note:** `vuln`, `exploit`, `brute`, `dos` are intrusive — only on authorized targets.
