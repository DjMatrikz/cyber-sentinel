---
tags: [web,sqli,injection]
---

# SQL Injection
Untrusted input reaches a SQL query. **Authorized labs only.**
- Test: `'` triggers errors; `' OR '1'='1` classic.
- Types: in-band (error/union), blind (boolean/time `SLEEP(5)`), out-of-band.
- Tool: `sqlmap -u "http://site/x?id=1" --dbs`.
- **Defense:** parameterized queries / prepared statements, input validation, least-privilege DB user, WAF.
Practice: DVWA, PortSwigger Web Security Academy.
