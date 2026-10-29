---
tags: [tools,tcpdump,capture,cli]
---

# tcpdump
CLI packet capture (no GUI — great on servers/SSH).
```
tcpdump -i eth0                      # live
tcpdump -i eth0 -w out.pcap          # save to file
tcpdump -r out.pcap                  # read file
tcpdump -i eth0 'tcp port 80'        # BPF filter
tcpdump -i eth0 host 10.0.0.5 -nn    # one host, no DNS/port name resolution
```
Same BPF syntax as Wireshark capture filters. Open the .pcap in Wireshark later.
