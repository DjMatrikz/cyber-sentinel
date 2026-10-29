---
tags: [kismet, devices, classification, analysis]
tool: kismet
---
# Device Identification & Classification

## What Kismet shows per device
SSID, BSSID, manufacturer (OUI lookup), channel, frequency, signal (RSSI), encryption, associated clients, first/last seen, packet counts, advertised capabilities.

## SSID vs BSSID
- **SSID** = network name.
- **BSSID** = a specific AP radio/virtual-AP MAC. Multiple BSSIDs can share one SSID (multi-radio gateway).

## Client identification
- **OUI lookup** (first 3 MAC octets) reveals the vendor -> often identifies IoT (e.g. "GD Midea" = an A/C / dehumidifier).
- **Randomized / locally-administered MACs:** modern phones randomize MACs for privacy -> vendor lookup unreliable. Check the "locally administered" bit.

## Classifications
- **Wi-Fi AP / Client / Bridged.**
- **Wi-Fi Bridged** = an address seen in traffic crossing a wireless link, not a normal associated station. Not inherently malicious.

## Row highlighting (why a row turns red)
Settings -> **Device Row Highlighting**:
| Rule | Color | Meaning |
|------|-------|---------|
| WPA Handshake | Red | captured EAPOL handshake material |
| RSN PMKID | Red | captured PMKID |
**Important:** a captured handshake/PMKID does NOT mean the password is recovered or the network is compromised — it's just the material present. Cracking is a separate, offline, authorized step.
Related: [[EAPOL Handshakes]], [[Hashcat]]
