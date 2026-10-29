---
tags: [flipper, momentum, firmware, flashing]
tool: flipper-zero
---
# Flashing Momentum Firmware
**Momentum** = feature-rich custom firmware (customization, extra apps, extended region options, UI tweaks). Successor-era community FW.

## Before you flash
- **Charge the Flipper** (>50%).
- **Back up** first: in qFlipper or the mobile app, back up your `/int` + SD. Saved keys/signals live on the SD — keep a copy.
- Know the risk: custom FW is community-maintained; flashing is generally safe and reversible, but back up anyway.

## Easiest: Web Updater (recommended)
1. On a desktop Chrome/Edge, go to Momentum's official web updater (momentum-fw.dev).
2. Connect the Flipper via USB-C.
3. Click **Install/Update via Web** → select your channel (Release vs Dev) → let it flash.
4. Flipper reboots into Momentum.

## Alternative: qFlipper + .tgz
1. Download the Momentum **.tgz** from the official site/GitHub releases.
2. Open **qFlipper** → connect Flipper → **Install from file** → pick the .tgz.
3. Wait for flash + reboot.

## Alternative: mobile app
- Flipper mobile app → firmware channel → (point to Momentum where supported) → update over BLE/USB.

## Recovery (if it won't boot)
- Enter DFU: hold **LEFT + BACK** ~5s to reboot; for DFU hold **OK+BACK** then release BACK while holding OK/LEFT per current docs.
- Use **qFlipper → Repair** to restore. If bricked, qFlipper's recovery reflashes the bootloader.

## Going back to official FW
- Same web updater / qFlipper, choose **Official (lab.flipper.net)** firmware.

**Only flash from official Momentum sources.** Random .tgz files from forums can be malicious.
