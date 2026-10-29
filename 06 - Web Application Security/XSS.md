---
tags: [web,xss,injection]
---

# Cross-Site Scripting (XSS)
Injecting JS that runs in victims' browsers.
- **Reflected** (in the request), **Stored** (persisted), **DOM-based** (client-side).
- Test: `<script>alert(1)</script>`, or context-aware payloads.
- Impact: steal cookies/sessions, keylog, pivot.
- **Defense:** output encoding, Content-Security-Policy, HttpOnly cookies, input validation, frameworks that auto-escape.
Practice: PortSwigger Academy, DVWA.
