---
tags: [crypto,tls,ssl]
---

# TLS / SSL
Encrypts data in transit (HTTPS, etc.). SSL is dead; use TLS 1.2/1.3.
- **Handshake:** client hello -> server hello + cert -> key exchange -> encrypted.
- **Certificates:** prove identity, signed by a CA; chain of trust.
- **TLS 1.3** — faster (1-RTT), drops weak ciphers, forward secrecy.
- Inspect: Wireshark `tls.handshake.extensions_server_name` (SNI visible), `openssl s_client -connect host:443`.
Attacks: expired/self-signed certs, downgrade, weak ciphers.
