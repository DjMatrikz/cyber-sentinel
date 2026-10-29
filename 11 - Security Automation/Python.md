---
tags: [automation,python,scripting]
---

# Python for Security
- **Libs:** `requests` (HTTP), `scapy` (packets), `socket`, `paramiko` (SSH), `beautifulsoup4` (scraping), `pwntools` (exploit dev).
- **Use cases:** port scanners, log parsers, API clients, automation glue, PoCs.
```python
import requests
for sub in ["www","mail","dev"]:
    try: requests.get(f"https://{sub}.example.com", timeout=3); print(sub,"up")
    except: pass
```
Ties to your Python learning + the cyber-sentinel RAG script.
