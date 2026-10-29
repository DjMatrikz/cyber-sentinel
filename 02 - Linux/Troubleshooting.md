---
tags: [linux,troubleshooting]
---

# Linux Troubleshooting
- **No network?** `ip a` (got IP?), `ping 8.8.8.8` (connectivity), `ping google.com` (DNS), check `/etc/resolv.conf`.
- **Service down?** `systemctl status <svc>`, `journalctl -xe`.
- **Disk full?** `df -h`, `du -sh /* | sort -rh | head`.
- **High load?** `top`/`htop`, `ps aux --sort=-%cpu | head`.
- **Permission denied?** check `ls -l`, ownership, SELinux/AppArmor.
- **Port in use?** `ss -tulpn | grep :80`.
