---
tags: [esp32, esptool, flashing, commands, cheatsheet]
tool: esp32-marauder
---
# esptool Command Reference
esptool = the CLI to talk to / flash ESP32 chips. On Windows use `py -m esptool`.

## Setup
```powershell
py --version                         # confirm Python
py -m esptool version                # confirm esptool
py -m pip install --upgrade esptool  # install / update
```

## Identify the board
- **Device Manager → Ports (COM & LPT)** to find the COM port (can change on reconnect — always re-check).
- Chip types: `esp32`, `esp32s2`, `esp32s3`, `esp32c3`, `esp32c5`, `esp32c6`.

## Core commands
```powershell
# verify communication (does NOT flash) -- key for the AC Dual C5
py -m esptool --chip esp32c5 --port COM5 --before no-reset chip-id

# read chip info / flash id
py -m esptool --chip esp32c5 --port COM5 flash-id
py -m esptool --chip esp32c5 --port COM5 read-mac

# erase the whole flash (clean slate before a stubborn install)
py -m esptool --chip esp32c5 --port COM5 erase-flash

# write firmware at an offset (bootloader/partitions/app vary by board)
py -m esptool --chip esp32c5 --port COM5 --baud 460800 write-flash 0x0 firmware.bin

# read current flash back to a file (backup)
py -m esptool --chip esp32c5 --port COM5 read-flash 0x0 0x400000 backup.bin
```

## Useful flags
| Flag | Purpose |
|------|---------|
| `--chip esp32c5` | specify the microcontroller |
| `--port COM5` | serial port (check Device Manager) |
| `--before no-reset` | skip auto-reset (use when you entered download mode manually) |
| `--after no-reset` | don't reset after the operation |
| `--baud 460800` | faster flashing (default 115200) |

**Note:** `chip-id` only proves communication — it does NOT install firmware.
Most people flash Marauder via the **web/desktop installer**; esptool is the manual/recovery path.
