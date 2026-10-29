---
tags: [flipper, settings, troubleshooting, momentum]
tool: flipper-zero
---
# Settings & Common Fixes (Momentum)

## Momentum app (customization)
Main menu → **Momentum**:
- **Device name**, boot animation, asset packs (icons/animations), level/XP display.
- **Interface tweaks:** menu style (list vs grid), font, status bar.
- **Sub-GHz settings:** frequency ranges / hopping lists, external CC1101 toggle.

## Sub-GHz region / frequencies
- Region is governed by `/int` region settings. Momentum can expose extended ranges, **but transmitting outside your legal allocation is illegal** — only enable what's lawful where you are.
- Add custom frequencies: Sub-GHz → Read → **Config** → set frequency/modulation.
- Using an **external CC1101** module: enable it in Sub-GHz settings (better range).

## Common fixes
| Problem | Fix |
|---------|-----|
| SD card not detected | reseat card; format **FAT32** in the Flipper (Settings → Storage → Format); re-copy assets |
| Apps missing after update | re-download the matching **asset pack / apps** for your FW version (FAPs are version-tied) |
| "Firmware mismatch" on an app | update the app from the catalog built for your current Momentum version |
| Flipper won't turn on | hold **LEFT + BACK** ~5s to force reboot; charge it |
| Stuck/boot loop | qFlipper → Repair; or reflash via web updater |
| NFC/RFID won't read | hold card flat against the back; try slow repositioning; some cards are unsupported/encrypted |
| IR remote weak | aim directly, close range; Flipper IR is low-power |
| BLE won't pair | Settings → Bluetooth → forget/re-pair; toggle BT off/on |
| Battery drains fast | lower backlight/brightness + timeout; disable always-on sub-ghz listening |

## Housekeeping
- Keep assets on the SD; back up `/int` + SD before major updates.
- Update apps **after** a firmware update (they must match the FW version).
