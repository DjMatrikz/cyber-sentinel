---
tags: [web,burp,tools]
---

# Burp Suite
The web pentest proxy. Community (free) vs Pro.
- **Proxy** — intercept/modify requests (set browser proxy to 127.0.0.1:8080, install Burp CA).
- **Repeater** — replay/tweak a request manually.
- **Intruder** — automated fuzzing/brute (throttled in Community).
- **Decoder / Comparer / Sequencer**.
- **Target site map + scope**.
Workflow: browse through proxy -> find interesting request -> Repeater to test -> confirm vuln.
