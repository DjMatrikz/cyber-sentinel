---
tags: [blueteam,splunk,siem]
---

# Splunk
Log analytics / SIEM. Core language = **SPL**.
```
index=windows EventCode=4625 | stats count by Account_Name | sort -count
index=* sourcetype=firewall action=blocked | timechart count
```
- `search` -> `stats`/`timechart`/`table` -> `sort`/`where`.
- Fields auto-extracted; use `| eval`, `| rex` for custom.
- Apps: Splunk Security Essentials, ES. Free dev license for home lab.
Great home-lab SIEM alongside Sysmon.
