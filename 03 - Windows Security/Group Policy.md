---
tags: [windows,grouppolicy,gpo]
---

# Group Policy (GPO)
Centralized config/policy for domain machines. `gpmc.msc`, `gpupdate /force`, `gpresult /r`.
- Enforce password policy, account lockout, audit policy, software restriction.
- **Security angle:** GPOs can push logging (good) but misconfigured/abusable GPOs = attack path (modify rights -> code exec on all targets).
- Store: SYSVOL share. Historically GPP passwords (cpassword) were crackable.
