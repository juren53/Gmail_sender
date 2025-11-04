# Version History

This document tracks the version history and changes for Quick Gmail Sender (quickmail.py).

---

## Version 0.2.0 (2025-11-04)

**Commit:** 4c7e3f1

### Features Added
- Added `-e` / `--edit` flag for using text editor to compose email body (commit ac3faf5)
  - Opens user's preferred editor ($EDITOR or $VISUAL environment variable)
  - Falls back to notepad (Windows) or nano (Unix/Linux/macOS)
  - Supports composing longer, multi-line emails more easily

### Other Changes
- Added quickmail alias support (commit 6c08c39)
- Version bump to 0.2.0
- Updated commit date to 2025-11-04 07:25:57

---

## Version 0.1.3 (2025-10-30)

**Commit:** 10b22fb

### Features Added
- Added `--settings` / `-s` flag to display current saved settings
- Added `--version` / `-v` flag to show version and commit date/time
- Configuration preview shown before save prompt
- Improved user feedback when saving settings

### Bug Fixes
- Fixed `-s` shorthand flag for --settings (commit 46dcc7d)

### Other Changes
- Added qm.ps1 PowerShell wrapper script (commit e7e3683)

---

## Version 0.1.2 (2025-10-30)

**Commit:** 204f78e

### Changes
- Added settings feedback message when configuration is saved
- Improved user experience with better confirmation messages

---

## Version 0.1.0 (2025-10-29)

**Commit:** c335be7

### Features Added
- Added version tracking with `__version__` and `__date__` variables
- Added `--help` / `-h` flag with comprehensive help information
- Version timestamp tracking in code

### Other Changes
- Changed prompts to default to "Yes" on Enter key (commit 27e6f6f)

---

## Pre-1.0 Development

### Commit: abacbd7
- Renamed `email_sender.py` to `quickmail.py`

### Commit: 051109f
- Added configuration file support (`~/.gmail_sender_config.json`)
- Implemented save/load for default sender, recipient, and App Password
- Password stored with base64 encoding for basic obfuscation

### Commit: b0e7a53
- Implemented cross-platform asterisk masking for password input
- Support for both Windows (msvcrt) and Unix/Linux (termios)
- Secure password entry with visual feedback

### Commit: 6229245
- Initial commit
- Basic email sending functionality via Gmail SMTP
- Interactive CLI prompts for email composition

---

## Summary of Key Features by Version

### v0.2.0
- Text editor support (`--edit`)
- Alias support

### v0.1.3
- Settings display (`--settings`)
- Version display (`--version`)
- Text editor support (`--edit`)
- Alias support
- PowerShell wrapper

### v0.1.2
- Enhanced user feedback

### v0.1.0
- Help system (`--help`)
- Version tracking

### Pre-1.0
- Core email sending
- Configuration persistence
- Secure password input
- Cross-platform support

---

## Upgrade Notes

### From 0.1.x to 0.2.0
- No breaking changes
- Existing configuration files remain compatible

### From 0.0.x to 0.1.0
- Configuration file format unchanged
- All features backward compatible

---

*Last Updated: 2025-11-04*
