---
tags: [linux,commands,cli]
---

# Essential Linux Commands
## Navigation / files
`pwd ls cd cp mv rm mkdir find locate` · `cat less head tail` · `grep awk sed`
## System / processes
`ps aux` `top htop` `kill` `systemctl` `df -h` `du -sh` `free -h` `uname -a`
## Networking
`ip a` `ip route` `ss -tulpn` `ping` `curl` `wget` `dig` `netstat`
## Users / perms
`whoami id sudo su chmod chown` · `/etc/passwd /etc/shadow`
## Packages
`apt install` `apt search` `dpkg -i` `which`
## Piping power
`cat file | grep error | awk '{print $1}' | sort | uniq -c | sort -rn`
