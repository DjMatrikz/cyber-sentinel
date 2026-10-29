---
tags: [web,api,appsec]
---

# API Security (OWASP API Top 10)
- **BOLA / IDOR** — accessing other users' objects by changing an ID (#1 API risk).
- **Broken auth**, excessive data exposure, mass assignment, rate-limit abuse.
- Test: intercept API calls (Burp/Postman), fuzz IDs, check authz on every endpoint.
- Auth: OAuth2, JWT (verify signature + expiry; watch `alg:none`), API keys.
See [[Authentication]].
