---
tags: [nmap, version-detection, os-detection, fingerprinting]
tool: nmap
---
# Nmap Service & OS Detection

| Flag | Purpose |
|------|---------|
| `-sV` | Service/version detection (what's running on each port) |
| `--version-intensity 0-9` | How hard to probe (9 = most thorough) |
| `-O` | OS detection (needs root) |
| `--osscan-guess` | Guess OS aggressively |
| `-A` | Aggressive: `-sV -O` + default scripts + traceroute |

## Examples
```
sudo nmap -sV 192.168.1.1              # what versions are running
sudo nmap -O 192.168.1.1               # what OS
sudo nmap -A 192.168.1.1               # the "everything" scan
sudo nmap -sV --version-intensity 9 192.168.1.1
```

**Why it matters:** version numbers map to known CVEs. Finding "Apache 2.4.49" tells you
to check that version for vulnerabilities (ties into MITRE recon tactics).
