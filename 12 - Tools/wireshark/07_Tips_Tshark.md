---
tags: [wireshark, tshark, cli, tips]
tool: wireshark
---
# Wireshark Tips + tshark (CLI)

## Must-know GUI moves
- **Follow stream:** right-click a packet -> Follow -> TCP/UDP/HTTP Stream. Reassembles the full conversation.
- **Statistics menu:** Protocol Hierarchy (what's in the capture), Conversations (who talks to whom), Endpoints (all hosts).
- **Colorize:** View -> Coloring Rules. Red/black usually = problems.
- **Add a column:** right-click a field -> Apply as Column (e.g. make SNI or HTTP host a column).
- **Expert Info:** Analyze -> Expert Information (errors, warnings, retransmits).
- **Decrypt WPA2:** Preferences -> Protocols -> IEEE 802.11 -> add the PSK; needs the 4-way handshake (eapol) in the capture.

## tshark — Wireshark on the command line
```
tshark -D                                  # list interfaces
tshark -i eth0                             # live capture
tshark -i eth0 -f "tcp port 80"            # with a capture filter
tshark -r capture.pcap -Y "http.request"   # read file, apply display filter
tshark -r capture.pcap -Y "dns" -T fields -e dns.qry.name   # extract just field values
tshark -i eth0 -w out.pcap                 # write to file
```
`-f` = capture filter (BPF), `-Y` = display filter, `-T fields -e <field>` = pull specific fields (great for scripting/CSV).

## Quick reference
| Goal                | Filter                                 |
| ------------------- | -------------------------------------- |
| One conversation    | `tcp.stream == N`                      |
| Only errors         | `tcp.analysis.flags`                   |
| Find a string       | `frame contains "text"`                |
| Exclude noise       | `!(arp \|\| dns \|\| stp)`             |
| HTTPS domains (SNI) | `tls.handshake.extensions_server_name` |
