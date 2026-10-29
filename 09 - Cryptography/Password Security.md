---
tags: [crypto,passwords,security]
---

# Password Security
- **Store** as salted slow hashes (bcrypt/Argon2/scrypt) — never plaintext or MD5.
- **Policy:** length > complexity; passphrases; MFA; block breached passwords (HaveIBeenPwned).
- **Attacks:** dictionary, brute force, credential stuffing, rainbow tables (defeated by salt), password spraying.
- **Managers:** Bitwarden/KeePass — unique passwords everywhere.
See [[Hashcat]], [[John the Ripper]].
