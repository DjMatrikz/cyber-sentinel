---
tags: [kismet, commands, cli, cheatsheet]
tool: kismet
---
# Kismet Commands (CLI)

## Install & setup (Kali/Debian)
```bash
sudo apt update && sudo apt upgrade -y
sudo apt install kismet -y
sudo usermod -aG kismet "$USER"     # run without full root
sudo reboot                         # apply group membership
```

## Working directory (logs land here)
```bash
mkdir -p ~/CyberLab/Kismet
cd ~/CyberLab/Kismet
```

## Check interfaces / monitor mode
```bash
iw dev                              # list wireless interfaces
iwconfig                            # show modes
sudo airmon-ng start wlan0          # manual monitor mode -> wlan0mon
sudo airmon-ng check kill           # stop interfering services (NetworkManager)
```

## Start Kismet
```bash
kismet                              # start, add sources in the web UI
kismet -c wlan0                     # start with a capture source
kismet -c wlan0mon                  # use an existing monitor interface
kismet -c wlan0:name=alfa           # name the source
kismet -c wlan0:channel=11          # lock to a channel at launch
kismet -c wlan0:hop=true,channels="1,6,11"   # custom hop list
kismet -t mycapture                 # set log file prefix
kismet -n                           # no logging (just live view)
```
Then open **http://localhost:2501** (first run: set an admin user/password).

## Add a source while running
```bash
kismet_cap_linux_wifi --list        # list capture-capable interfaces
# (or add via Web UI -> Data Sources -> +)
```

## MAC manufacturer lookup (manuf2)
```bash
curl -L https://raw.githubusercontent.com/joshschmelzle/manuf2/refs/heads/master/manuf2/manuf -o ~/Desktop/manuf.txt
ls -lh ~/Desktop/manuf.txt
grep -i '^AA:BB:CC' ~/Desktop/manuf.txt     # first 3 octets of the MAC
```

## Working with Kismet logs (.kismet DB)
```bash
kismetdb_statistics *.kismet                 # summary of a capture
kismetdb_dump_devices --in *.kismet          # dump devices (JSON)
kismetdb_to_pcap --in *.kismet --out cap.pcapng   # convert to pcap for Wireshark
kismetdb_to_wiglecsv --in *.kismet --out out.csv  # export for WiGLE mapping
```

## Web interface
```text
http://localhost:2501
```
Stop Kismet: `Ctrl+C` in its terminal (or Server -> Stop in the UI).
