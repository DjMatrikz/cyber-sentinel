---
tags: [blueteam,forensics,dfir]
---

# Digital Forensics (DFIR)
- **Order of volatility:** memory > network state > disk > logs > archives.
- **Memory:** capture (WinPMEM/Magnet) -> analyze with **Volatility**.
- **Disk:** image with `dd`/FTK Imager; analyze with Autopsy/Sleuth Kit.
- **Artifacts (Windows):** prefetch, shimcache, amcache, $MFT, registry, event logs, browser history.
- **Chain of custody** + hashing (verify integrity) are mandatory.
