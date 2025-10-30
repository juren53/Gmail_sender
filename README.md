# Quick Gmail Sender

A simple Python CLI tool for sending emails via Gmail without opening your full Gmail account.

## Features

- 🚀 Quick email sending from command line
- 🔒 Secure password input with asterisk masking
- 💾 Save default settings (sender, recipient, password)
- ✅ Confirmation before sending
- 📧 Plain text email support
- 🎯 Simple and lightweight
- 🖥️ Cross-platform (Windows, Linux, macOS)

## Requirements

- Python 3.6+
- Gmail account with App Password enabled

## Setup

### 1. Enable Gmail App Password

Since Gmail requires 2FA for SMTP access, you need to create an App Password:

1. Go to your Google Account: https://myaccount.google.com/
2. Navigate to Security → 2-Step Verification (enable it if not already)
3. Go to Security → App passwords: https://myaccount.google.com/apppasswords
4. Generate a new app password for "Mail" on "Windows Computer"
5. Save this 16-character password (you'll need it when running the script)

### 2. Install Python

Make sure Python 3 is installed on your system. No additional packages required - uses only standard library.

## Usage

### Basic Usage

Run the script:

```bash
python quickmail.py
```

Follow the prompts:
1. Enter your Gmail address (or press Enter to use saved default)
2. Choose to use saved App Password or enter a new one (shown as asterisks)
3. Enter recipient email (or press Enter to use saved default)
4. Enter subject
5. Enter body (press Ctrl+Z then Enter on Windows, or Ctrl+D on Unix)
6. Confirm and send
7. Optionally save settings for future use

### Example Session

```
=== Quick Gmail Sender ===

Your Gmail address: your.email@gmail.com
Your Gmail App Password: ****************
Recipient email: friend@example.com
Subject: Quick update

Email body (press Ctrl+Z then Enter on Windows, or Ctrl+D on Unix when done):
Hey! Just wanted to send a quick update about the project.
^Z

==================================================
From: your.email@gmail.com
To: friend@example.com
Subject: Quick update
Body: Hey! Just wanted to send a quick update...
==================================================

Send this email? (y/n): y
Connecting to Gmail SMTP server...
Logging in...
Sending email...
✓ Email sent successfully to friend@example.com

Save these settings as defaults? (y/n): y
✓ Configuration saved to /home/user/.gmail_sender_config.json
```

## Configuration File

The script can save your default settings to `~/.gmail_sender_config.json`. This file stores:
- Default sender email
- Default recipient email  
- App Password (base64 encoded for basic obfuscation)

**Note**: The password encoding is NOT cryptographically secure - it's just basic obfuscation. Keep the config file permissions restricted (automatic on Unix-like systems).

### Manual Configuration

You can manually create or edit `~/.gmail_sender_config.json`:

```json
{
  "sender_email": "your-email@gmail.com",
  "recipient_email": "recipient@example.com",
  "sender_password": "base64_encoded_app_password"
}
```

## Future Enhancements

Potential features for future versions:
- Command-line arguments for quick sends
- HTML email support
- File attachments
- Multiple recipients (CC, BCC)
- Email templates
- More secure password encryption
- GUI interface

## Troubleshooting

**Authentication Error**: Make sure you're using an App Password, not your regular Gmail password.

**Connection Error**: Check your internet connection and ensure Gmail SMTP (smtp.gmail.com:587) is not blocked by your firewall.

**2FA Not Enabled**: You must enable 2-Step Verification on your Google account before creating an App Password.

## Security Notes

- Never share your App Password
- Config file uses basic obfuscation (not encryption) for the password
- On Unix-like systems, config file permissions are automatically set to user-only (600)
- Password input is masked with asterisks for security
- Store the config file in a secure location
- Consider using system keychains for more secure storage (future feature)
