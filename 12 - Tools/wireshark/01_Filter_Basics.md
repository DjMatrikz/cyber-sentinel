---
tags: [wireshark, filters, fundamentals]
tool: wireshark
---
# Wireshark Filter Basics

Two completely different filter types — don't mix them up:

| | Capture filter | Display filter |
|---|----------------|----------------|
| When | BEFORE capture (what to record) | AFTER capture (what to show) |
| Syntax | BPF (`tcp port 80`) | Wireshark (`tcp.port == 80`) |
| Box color | Green field, top (interface setup) | Green bar below toolbar |
| Reversible | No — unrecorded = gone | Yes — just change the filter |

**Rule of thumb:** capture filters to keep file size down on big/long captures; display filters for everything else (keeps all data, lets you slice it freely).

## Display filter operators
| Operator | Meaning | Alt |
|----------|---------|-----|
| `==` | equal | `eq` |
| `!=` | not equal | `ne` |
| `>` `<` `>=` `<=` | compare | `gt lt ge le` |
| `&&` | and | `and` |
| `\|\|` | or | `or` |
| `!` | not | `not` |
| `contains` | byte/string present | |
| `matches` | regex match | `~` |
| `in` | value in set | `tcp.port in {80 443 8080}` |

## Examples
```
ip.addr == 10.0.0.5                    # to OR from this IP
ip.src == 10.0.0.5 && tcp.port == 443  # from this IP, HTTPS
!(arp || dns)                          # hide ARP and DNS noise
http.request.method == "POST"
frame contains "password"              # raw bytes anywhere in frame
tcp.port in {80 443 8080}
```
