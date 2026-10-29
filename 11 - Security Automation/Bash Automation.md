---
tags: [automation,bash]
---

# Bash Automation
- Glue for Linux tooling: loop targets, chain tools, parse output.
```bash
for ip in $(cat hosts.txt); do nmap -F $ip -oG - | grep open; done
```
- `cron` for scheduling; `jq` for JSON APIs; `curl` for web.
- Combine nmap/ffuf/etc. into recon pipelines.
