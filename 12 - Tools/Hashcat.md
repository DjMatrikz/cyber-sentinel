---
tags: [tools,hashcat,cracking]
---

# Hashcat
GPU password/hash cracker.
```
hashcat -m 1000 ntlm.txt rockyou.txt       # NTLM + wordlist
hashcat -m 22000 wpa.hc22000 rockyou.txt   # WPA2
```
`-m` mode, `-a` attack (0 wordlist / 3 mask), `-r` rules. **Authorized hashes only.** See [[Hashcat]] in Cryptography.
