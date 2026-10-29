---
tags: [networkplus, troubleshooting, methodology]
exam: Network+
---
# Network Troubleshooting

## CompTIA 7-step methodology
1. **Identify the problem** (gather info, question users, check changes).
2. **Establish a theory** of probable cause (think OSI, top-to-bottom or bottom-to-top).
3. **Test the theory.** If confirmed → next step. If not → form a new theory or escalate.
4. **Establish a plan of action** and identify potential effects.
5. **Implement the solution** or escalate.
6. **Verify full system functionality** (and implement preventive measures).
7. **Document** findings, actions, and outcomes.

## Key CLI tools
| Tool | Purpose |
|------|---------|
| `ping` | Test reachability (ICMP) |
| `ipconfig` / `ifconfig` / `ip` | Show IP config |
| `tracert` / `traceroute` | Path/hops to destination |
| `nslookup` / `dig` | DNS queries |
| `netstat` | Active connections/ports |
| `arp -a` | MAC-to-IP table |
| `nmap` | Port/host scanning |

**Common issues:** APIPA address (169.254.x.x) = DHCP failure. No DNS = can ping IP but not name. Duplex/speed mismatch = slow/errors.
