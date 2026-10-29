---
tags: [linux,bash,scripting,automation]
---

# Bash Scripting
```bash
#!/bin/bash
TARGET=$1
for ip in 192.168.1.{1..10}; do
  ping -c1 -W1 $ip &>/dev/null && echo "$ip is up"
done
```
- Variables: `NAME=value` -> `$NAME`. Args: `$1 $2 $@ $#`.
- Conditionals: `if [ "$x" -eq 1 ]; then ... fi`
- Loops: `for i in ...; do ... done` / `while ...; do ... done`
- Make executable: `chmod +x script.sh` then `./script.sh`
- `$(command)` captures output. `&&` / `||` chain on success/failure.
