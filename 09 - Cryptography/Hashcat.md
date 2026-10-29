---
tags: [crypto,hashcat,cracking,tools]
---

# Hashcat
GPU password cracker (your RTX helps here).
```
hashcat -m 0 hashes.txt rockyou.txt          # MD5 + wordlist
hashcat -m 1000 ntlm.txt rockyou.txt          # NTLM
hashcat -m 22000 wpa.hc22000 rockyou.txt      # WPA2 handshake
hashcat -m 0 -a 3 hash ?d?d?d?d?d?d            # brute 6 digits
```
- `-m` hash mode, `-a` attack (0=wordlist, 3=brute/mask).
- Rules (`-r`) mutate wordlists. **Authorized hashes only.**
