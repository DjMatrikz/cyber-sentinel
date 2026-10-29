---
tags: [blueteam,siem]
---

# SIEM (Security Information & Event Management)
Centralizes logs, correlates, alerts.
- **Pipeline:** collect -> normalize/parse -> correlate (rules) -> alert -> dashboard.
- **Use cases:** failed logons spike, impossible travel, new admin, malware IOC match.
- Products: Splunk, Elastic/ELK, Microsoft Sentinel, Wazuh (open source), QRadar.
- Quality depends on log coverage + tuned rules (reduce false positives).
See [[Splunk]], [[Wazuh]].
