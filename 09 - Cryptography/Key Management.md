---
tags: [crypto,keys,pki]
---

# Key Management
- **PKI:** CAs issue/sign certs; trust chains; CRL/OCSP for revocation.
- **Key lifecycle:** generate -> distribute -> store -> rotate -> revoke -> destroy.
- **Storage:** HSMs, KMS (AWS KMS, Azure Key Vault), never hardcode in source.
- **Secrets management:** Vault (HashiCorp), sealed secrets; scan repos for leaked keys.
- Principle: protect the key, not the algorithm (Kerckhoffs's principle).
