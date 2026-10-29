---
tags: [crypto,hashing]
---

# Hashing
One-way function; same input -> same fixed-length digest. Not reversible.
- **Algorithms:** MD5 (broken), SHA-1 (broken), SHA-256/512 (good), bcrypt/scrypt/Argon2 (password hashing — slow by design).
- **Uses:** integrity verification, password storage, digital signatures.
- **Salting** — random per-password value stops rainbow tables.
- Collisions = two inputs, same hash (MD5/SHA1 vulnerable).
`sha256sum file` · `md5sum file`. See [[Password Security]], [[Hashcat]].
