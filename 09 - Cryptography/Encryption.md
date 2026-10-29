---
tags: [crypto,encryption]
---

# Encryption
Reversible with a key. Confidentiality.
- **Symmetric:** one shared key, fast. AES (128/256), ChaCha20. Modes: GCM (authenticated), CBC.
- **Asymmetric:** public/private key pair. RSA, ECC. Slow; used for key exchange + signatures.
- **Hybrid:** asymmetric exchanges a symmetric session key (how TLS works).
- **Signatures:** sign with private, verify with public (integrity + non-repudiation).
See [[TLS-SSL]], [[Key Management]].
