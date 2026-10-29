---
tags: [web,auth,appsec]
---

# Authentication & Session Security
- **MFA**, strong password policy, lockout/throttling.
- **Sessions:** secure/HttpOnly/SameSite cookies, rotate on login, proper logout.
- **JWT:** verify signature, check `exp`, reject `alg:none`, don't store secrets in payload.
- **OAuth2 / OIDC** — delegated auth; watch redirect_uri validation.
- Attacks: credential stuffing, session fixation/hijacking, password reset flaws.
