---
tags: [cloud,misconfig]
---

# Cloud Misconfigurations
The #1 cause of cloud breaches.
- Public storage buckets/blobs, open security groups (0.0.0.0/0), exposed databases.
- Over-permissive IAM, unused credentials, no MFA, hardcoded/leaked keys.
- Missing logging/encryption, default settings.
- **Tools:** ScoutSuite, Prowler (AWS), CloudSploit, Steampipe; CSPM platforms.
- Fix: least privilege, infra-as-code with policy checks, continuous posture scanning.
