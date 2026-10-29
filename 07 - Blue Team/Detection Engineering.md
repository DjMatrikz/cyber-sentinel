---
tags: [blueteam,detection,sigma]
---

# Detection Engineering
Building/tuning the rules that catch attacks.
- Write detections as code; **Sigma** = vendor-agnostic rule format -> compiles to Splunk/Elastic/etc.
- Map each rule to MITRE ATT&CK; track coverage gaps.
- Test with atomic attacks (**Atomic Red Team**, Caldera).
- Balance true positives vs noise; version-control rules.
