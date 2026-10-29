---
tags: [esp32, downloadmode, recovery, troubleshooting, acdualc5]
tool: esp32-marauder
---
# Download Mode & Recovery (AC Dual C5 / ESP32-C5)
When auto-reset fails, force the chip into firmware download mode by hand.

## Manual download-mode sequence (AC Dual C5)
Connect USB-C to the port labeled **SCREEN**, then:
```text
1. Hold  SCREEN BOOT
2. Press SCREEN RESET   (while holding BOOT)
3. Release SCREEN RESET
4. Keep holding BOOT ~2 seconds
5. Release SCREEN BOOT
```
Chip is now in download mode.

## Verify it worked
```powershell
py -m esptool --chip esp32c5 --port COM5 --before no-reset chip-id
```
Success = it reports ESP32-C5HR8 + crystal/PSRAM info.

## Troubleshooting
| Problem | Fix |
|---------|-----|
| Device not detected | reconnect USB-C, re-check COM port in Device Manager |
| Chip not responding | redo the manual download-mode sequence |
| Auto-reset fails | add `--before no-reset` after manual download mode |
| COM port changed | Windows reassigned it — update `--port COMx` to the current one |
| Still failing | `erase-flash` first, lower `--baud` to 115200, try another USB cable/port (data cable, not charge-only) |

## Quick recovery checklist
1. Connect via SCREEN USB-C.
2. Enter download mode (sequence above).
3. Confirm COM port in Device Manager.
4. `chip-id` to verify comms.
5. Run the firmware installer.
6. Restart board → verify version in the Marauder UI.
