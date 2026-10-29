---
tags: [nmap, output, recipes, cheatsheet]
tool: nmap
---
# Nmap Output & Go-To Recipes

## Output formats
| Flag | Format |
|------|--------|
| `-oN file` | Normal (human-readable) |
| `-oX file` | XML |
| `-oG file` | Greppable |
| `-oA base` | All three at once |
| `-v` / `-vv` | Verbose |
| `--open` | Show only open ports |
| `--reason` | Why a port is in its state |

## Go-to command recipes
```
# Quick network inventory
nmap -sn 192.168.1.0/24

# Full TCP scan with versions + default scripts, saved
sudo nmap -sS -sV -sC -p- -T4 -oA fullscan 192.168.1.10

# Fast "what is this box" scan
sudo nmap -A -T4 192.168.1.10

# Find web servers on a subnet
nmap -p 80,443,8080 --open 192.168.1.0/24

# Vuln sweep of a single host
sudo nmap -sV --script vuln 192.168.1.10

# UDP top ports (DNS, SNMP, etc.)
sudo nmap -sU --top-ports 20 192.168.1.10
```

**Workflow:** discover hosts (-sn) -> scan ports (-p-) -> ID services (-sV) ->
check vulns (--script vuln) -> document (-oA).
