---
tags: [tools,wireshark,analysis]
---

# Wireshark
Packet capture + analysis. Capture filters (BPF) vs display filters.
```
ip.addr == 10.0.0.5
http.request.method == "POST"
tls.handshake.extensions_server_name   # SNI
arp.duplicate-address-detected          # MITM
```
**Full pack lives in the `wireshark/` folder** (filters, threat hunting, tshark, Operation Pantera).
