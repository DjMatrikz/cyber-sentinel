---
tags: [tools,john,cracking]
---

# John the Ripper
CPU-focused password cracker (great for varied hash formats).
```
john --wordlist=rockyou.txt hashes.txt
john --show hashes.txt
unshadow /etc/passwd /etc/shadow > creds.txt   # combine for cracking
zip2john file.zip > ziphash   # extract crackable hash
```
`*2john` helpers extract hashes from many file types. **Authorized only.**
