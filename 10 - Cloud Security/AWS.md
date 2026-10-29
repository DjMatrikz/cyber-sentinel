---
tags: [cloud,aws]
---

# AWS Security
- **IAM** — users/roles/policies; least privilege; MFA on root; no root for daily use.
- **Common risks:** public S3 buckets, over-permissive IAM, exposed keys, open security groups.
- **Services:** GuardDuty (threat detection), CloudTrail (audit logs), Config, Security Hub.
- **Recon (authorized):** `aws sts get-caller-identity`, enumerate with Pacu/ScoutSuite.
- Shared responsibility: AWS secures the cloud, you secure what's in it.
