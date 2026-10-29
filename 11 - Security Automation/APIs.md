---
tags: [automation,api]
---

# Working with Security APIs
- **REST basics:** GET/POST/PUT/DELETE, headers, auth (API key, Bearer/JWT, OAuth2).
- **Common security APIs:** VirusTotal, Shodan, AbuseIPDB, MISP, your SIEM's API.
- Authenticate, respect rate limits, handle pagination, parse JSON.
- Automate enrichment: hash -> VirusTotal verdict; IP -> AbuseIPDB score.
`curl -H "x-apikey: KEY" https://www.virustotal.com/api/v3/...`
