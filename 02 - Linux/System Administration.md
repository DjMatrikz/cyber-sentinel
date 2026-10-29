---
tags: [linux,sysadmin]
---

# Linux System Administration
- **Services:** `systemctl start/stop/enable/status <svc>`; logs via `journalctl -u <svc>`.
- **Cron:** `crontab -e` — scheduled jobs (`* * * * * cmd`). Also a persistence vector.
- **Users:** `useradd` `passwd` `usermod -aG group user` `deluser`.
- **Logs:** `/var/log/` — `auth.log` (logins), `syslog`, `dmesg`.
- **Disk:** `df -h` `lsblk` `mount` `fdisk -l`.
- **Network config:** `/etc/netplan/`, `/etc/resolv.conf`, `/etc/hosts`.
