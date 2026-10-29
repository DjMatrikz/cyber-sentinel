---
tags: [kismet, filters, views, webui]
tool: kismet
---
# Kismet Filtering, Views & Alerts

Kismet filters mostly in the **web UI** (and via config/REST), unlike Wireshark's text filter bar.

## Web UI device table
- **Search box** — filter by SSID, MAC, manufacturer, type.
- **Views (top dropdown):** All devices, Wi-Fi Access Points, Wi-Fi Clients, Wi-Fi Bridged, Bluetooth, etc.
- **Columns:** right-click header to add/remove (channel, crypto, signal, packets, manuf, first/last seen).
- **Sort** by signal (find closest), packets, last-seen.
- Click a device -> details, associated clients, signal graph, raw fields.

## Config-file capture filters (kismet_site.conf)
Put overrides in `~/.kismet/kismet_site.conf` (or `/etc/kismet/`):
```text
# only log/track specific BSSIDs
filter_tracker=bssid(AA:BB:CC:DD:EE:FF)
# block a device from capture
filter_tracker=bssid(11:22:33:44:55:66),block
# restrict a source to channels
source=wlan0:channels="1,6,11"
# lock a source to one channel
source=wlan0:channel=11
```
Apply by restarting Kismet.

## Alerts (IDS)
- **Alerts** dashboard flags events (deauth floods, spoofed APs, etc.).
- `0 alerts` != secure — depends on enabled rules, monitored channels, capture time, adapter.
- Alert rules configured in `kismet_alerts.conf`.

## REST API (automation)
```bash
curl http://localhost:2501/system/status.json
curl http://localhost:2501/devices/views/all/devices.json
```
Great for scripting with Python. See [[APIs]].

## Pulling it into other tools
```bash
kismetdb_to_pcap --in capture.kismet --out cap.pcapng   # -> open in Wireshark
```
Then apply Wireshark filters like `eapol`, `wlan.fc.type_subtype == 0x08`.
Related: [[Wireshark]], [[05_Wireless_80211_OperationPantera]]
