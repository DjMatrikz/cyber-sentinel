---
tags: [threatintel,ioc]
---

# Indicators of Compromise (IOCs)
Evidence of intrusion.
- **Atomic:** IPs, domains, URLs, file hashes (MD5/SHA256), emails.
- **Behavioral:** registry keys, mutexes, process trees, C2 patterns.
- **Pyramid of Pain:** hashes trivial to change -> TTPs hardest (focus there).
- Share via **STIX/TAXII**, threat feeds, MISP.
- Match IOCs in SIEM/EDR; enrich alerts.
