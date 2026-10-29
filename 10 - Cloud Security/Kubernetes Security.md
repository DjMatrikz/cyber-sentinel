---
tags: [cloud,kubernetes,k8s,containers]
---

# Kubernetes Security
- **RBAC** — restrict who can do what in the cluster.
- **Pod Security** — standards (restricted/baseline), no privileged pods, drop caps.
- **Network Policies** — default-deny east-west traffic.
- **Secrets** — encrypt at rest, use external secret stores.
- **Risks:** exposed API server/dashboard, over-permissive service accounts, vulnerable images.
- Tools: kube-bench (CIS), kube-hunter, Trivy, Falco (runtime).
