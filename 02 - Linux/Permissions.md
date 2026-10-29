---
tags: [linux,permissions,security]
---

# Linux Permissions
`rwx` for owner/group/other. `chmod 755` = rwxr-xr-x.
|Octal|Perms|
|-----|-----|
|7|rwx|
|6|rw-|
|5|r-x|
|4|r--|
- `chmod u+x file` · `chown user:group file`
- **Special bits:** SUID (run as owner) — pentest goldmine for privesc; SGID; sticky bit (/tmp).
- Find SUID binaries: `find / -perm -4000 2>/dev/null` (privesc recon).
Related: [[Linux Privilege Escalation]]
