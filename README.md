# Quick Gmail Sender

A simple Python CLI tool for sending emails via Gmail without opening your full Gmail account.

## Features

- 🚀 Quick email sending from command line
- 🔒 Secure password input (hidden)
- ✅ Confirmation before sending
- 📧 Plain text email support
- 🎯 Simple and lightweight

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
python email_sender.py
```

Follow the prompts:
1. Enter your Gmail address
2. Enter your Gmail App Password (will be hidden)
3. Enter recipient email
4. Enter subject
5. Enter body (press Ctrl+Z then Enter when done on Windows)
6. Confirm and send

### Example Session

```
=== Quick Gmail Sender ===

Your Gmail address: your.email@gmail.com
Your Gmail App Password (hidden): 
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
```

## Future Enhancements

Potential features for future versions:
- Command-line arguments for quick sends
- HTML email support
- File attachments
- Multiple recipients (CC, BCC)
- Email templates
- Configuration file for sender credentials
- GUI interface

## Troubleshooting

**Authentication Error**: Make sure you're using an App Password, not your regular Gmail password.

**Connection Error**: Check your internet connection and ensure Gmail SMTP (smtp.gmail.com:587) is not blocked by your firewall.

**2FA Not Enabled**: You must enable 2-Step Verification on your Google account before creating an App Password.

## Security Notes

- Never share your App Password
- The script does not store your credentials
- Password input is hidden for security
- Consider using environment variables for automation (future feature)
