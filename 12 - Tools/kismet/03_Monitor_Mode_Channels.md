---
tags: [kismet, monitor-mode, channels, wireless]
tool: kismet
---
# Monitor Mode & Channel Control

## Monitor mode
- Lets the adapter observe ALL frames without joining a network.
- Kismet auto-creates `wlan0mon`; `wlan0` and `wlan0mon` share ONE physical radio.
- Manual: `sudo airmon-ng start wlan0` (and `airmon-ng check kill` to stop NetworkManager).

## Channel Hopping vs Locking
| | Hopping | Locking |
|---|---------|---------|
| Coverage | Cycles channels — finds many networks | One channel only |
| Trade-off | May miss packets while elsewhere | Consistent, complete capture of that AP |
| Use for | Discovery / survey | Analyzing a specific AP + its clients |

- Set in Web UI: **Data Sources -> (your source) -> Hop / Lock**.
- Default hop ~5 channels/sec.
- Lock example: pick **Channel 11** for a 2.4 GHz AP.

## Bands
- **2.4 GHz:** channels 1-11 (US); non-overlapping 1, 6, 11.
- **5 GHz:** many channels (36-165); one AP may use several (e.g. 1, 44, 153 for a multi-radio gateway).
Related: [[WiFi Fundamentals]], [[Wireless Reconnaissance]]
