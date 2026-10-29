---
tags: [cloud,docker,containers]
---

# Docker Security
- **Don't run as root** in containers; drop capabilities; read-only FS where possible.
- **Images:** use minimal/official bases, scan (Trivy, Docker Scout), pin versions, no secrets in layers.
- **Isolation:** containers share the host kernel — not a full security boundary.
- **Risks:** exposed Docker socket (= host root), privileged containers, leaked env vars.
- Harden: user namespaces, seccomp/AppArmor, `--no-new-privileges`.
Ties to your RobLab/HomeLab Docker stacks.
