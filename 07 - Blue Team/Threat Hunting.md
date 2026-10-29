---
tags: [blueteam,threathunting]
---

# Threat Hunting
Proactively searching for threats that evaded detection (assume breach).
- **Hypothesis-driven:** "If an attacker used X (ATT&CK technique), I'd see Y."
- Hunt on: process creation (4688/Sysmon 1), network (Sysmon 3), DNS, PowerShell logs, LOLBins.
- Pyramid of Pain — hashes easy to change, TTPs hard.
- Outputs feed new detections. See [[Detection Engineering]], [[MITRE ATT&CK Overview]].
