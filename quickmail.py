#!/usr/bin/env python3
"""
Quickmail - Simple CLI Email Sender for Gmail
Quickly send emails without opening the full Gmail interface.

Version: 0.1.2
Date: 2025-01-30 01:17:00
"""

import smtplib
import sys
import os
import json
import base64
from datetime import datetime
from pathlib import Path
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from getpass import getpass

__version__ = "0.1.2"
__date__ = "2025-01-30 01:17:00"

try:
    import msvcrt
    WINDOWS = True
except ImportError:
    import tty
    import termios
    WINDOWS = False


def get_config_path():
    """Get the path to the configuration file."""
    return Path.home() / '.gmail_sender_config.json'


def encode_password(password):
    """Simple encoding for password (NOT cryptographically secure, just obfuscation)."""
    return base64.b64encode(password.encode()).decode()


def decode_password(encoded):
    """Decode the obfuscated password."""
    return base64.b64decode(encoded.encode()).decode()


def load_config():
    """Load configuration from file."""
    config_path = get_config_path()
    if not config_path.exists():
        return {}
    
    try:
        with open(config_path, 'r') as f:
            config = json.load(f)
            # Decode password if present
            if 'sender_password' in config:
                config['sender_password'] = decode_password(config['sender_password'])
            return config
    except Exception as e:
        print(f"Warning: Could not load config file: {e}")
        return {}


def save_config(sender_email, recipient_email, sender_password):
    """Save configuration to file."""
    config_path = get_config_path()
    config = {
        'sender_email': sender_email,
        'recipient_email': recipient_email,
        'sender_password': encode_password(sender_password)
    }
    
    try:
        with open(config_path, 'w') as f:
            json.dump(config, f, indent=2)
        # Set file permissions to be readable only by owner (Unix-like systems)
        if not WINDOWS:
            os.chmod(config_path, 0o600)
        print(f"✓ Configuration saved to {config_path}")
    except Exception as e:
        print(f"Warning: Could not save config file: {e}")


def getpass_with_asterisks(prompt="Password: "):
    """
    Get password input with asterisk masking (cross-platform).
    Works on both Windows and Unix-like systems.
    """
    print(prompt, end='', flush=True)
    password = ""
    
    if WINDOWS:
        # Windows implementation
        while True:
            ch = msvcrt.getch()
            if ch in (b'\r', b'\n'):  # Enter key
                print()
                break
            elif ch == b'\x08':  # Backspace
                if password:
                    password = password[:-1]
                    print('\b \b', end='', flush=True)
            elif ch == b'\x03':  # Ctrl+C
                print()
                raise KeyboardInterrupt
            else:
                password += ch.decode('utf-8', errors='ignore')
                print('*', end='', flush=True)
    else:
        # Unix/Linux implementation
        fd = sys.stdin.fileno()
        old_settings = termios.tcgetattr(fd)
        try:
            tty.setraw(fd)
            while True:
                ch = sys.stdin.read(1)
                if ch in ('\r', '\n'):  # Enter key
                    print()
                    break
                elif ch == '\x7f':  # Backspace/Delete
                    if password:
                        password = password[:-1]
                        print('\b \b', end='', flush=True)
                elif ch == '\x03':  # Ctrl+C
                    print()
                    raise KeyboardInterrupt
                else:
                    password += ch
                    print('*', end='', flush=True)
        finally:
            termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
    
    return password


def send_email(sender_email, sender_password, recipient_email, subject, body):
    """
    Send an email via Gmail SMTP server.
    
    Args:
        sender_email: Your Gmail address
        sender_password: Your Gmail app password (not regular password)
        recipient_email: Recipient's email address
        subject: Email subject
        body: Email body text
    
    Returns:
        True if successful, False otherwise
    """
    try:
        # Create message
        message = MIMEMultipart()
        message['From'] = sender_email
        message['To'] = recipient_email
        message['Subject'] = subject
        
        # Add body to email
        message.attach(MIMEText(body, 'plain'))
        
        # Connect to Gmail SMTP server
        print("Connecting to Gmail SMTP server...")
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        
        # Login
        print("Logging in...")
        server.login(sender_email, sender_password)
        
        # Send email
        print("Sending email...")
        server.send_message(message)
        server.quit()
        
        print(f"✓ Email sent successfully to {recipient_email}")
        return True
        
    except smtplib.SMTPAuthenticationError:
        print("✗ Authentication failed. Make sure you're using an App Password, not your regular Gmail password.")
        print("  Generate one at: https://myaccount.google.com/apppasswords")
        return False
    except Exception as e:
        print(f"✗ Error sending email: {str(e)}")
        return False


def show_help():
    """Display help information."""
    help_text = f"""
Quickmail v{__version__} - Simple CLI Email Sender for Gmail

USAGE:
  python quickmail.py [--help]

DESCRIPTION:
  Quick command-line tool for sending emails via Gmail without opening
  the full Gmail interface. Supports saving default settings for faster sends.

FEATURES:
  • Cross-platform (Windows, Linux, macOS)
  • Secure password input with asterisk masking
  • Save default sender, recipient, and App Password
  • Configuration stored in ~/.gmail_sender_config.json
  • Plain text email support

REQUIREMENTS:
  • Gmail account with App Password enabled
  • Generate App Password at: https://myaccount.google.com/apppasswords

MORE INFO:
  https://github.com/juren53/Gmail_sender/blob/main/README.md
"""
    print(help_text)


def main():
    """Main CLI interface for sending emails."""
    # Check for help flag
    if '--help' in sys.argv or '-h' in sys.argv:
        show_help()
        sys.exit(0)
    
    print("=== Quick Gmail Sender ===")
    print(f"Version {__version__} ({__date__})")
    
    # Load configuration
    config = load_config()
    
    # Get email details from user (with defaults from config)
    default_sender = config.get('sender_email', '')
    sender_prompt = f"Your Gmail address [{default_sender}]: " if default_sender else "Your Gmail address: "
    sender_email = input(sender_prompt).strip() or default_sender
    
    # Ask for password if not in config or if user wants to update it
    if config.get('sender_password'):
        use_saved = input("Use saved App Password? (Y/n): ").strip().lower()
        if not use_saved or use_saved == 'y':
            sender_password = config['sender_password']
        else:
            sender_password = getpass_with_asterisks("Your Gmail App Password: ")
    else:
        sender_password = getpass_with_asterisks("Your Gmail App Password: ")
    
    print()
    default_recipient = config.get('recipient_email', '')
    recipient_prompt = f"Recipient email [{default_recipient}]: " if default_recipient else "Recipient email: "
    recipient_email = input(recipient_prompt).strip() or default_recipient
    
    subject = input("Subject: ").strip()
    
    print("\nEmail body (press Ctrl+Z then Enter on Windows, or Ctrl+D on Unix when done):")
    try:
        body = sys.stdin.read()
    except KeyboardInterrupt:
        print("\n\nCancelled.")
        return
    
    # Confirm before sending
    print("\n" + "="*50)
    print(f"From: {sender_email}")
    print(f"To: {recipient_email}")
    print(f"Subject: {subject}")
    print(f"Body: {body[:100]}{'...' if len(body) > 100 else ''}")
    print("="*50)
    
    confirm = input("\nSend this email? (Y/n): ").strip().lower()
    if confirm and confirm != 'y':
        print("Cancelled.")
        return
    
    # Send the email
    success = send_email(sender_email, sender_password, recipient_email, subject, body)
    
    # Ask to save configuration
    if success:
        save_conf = input("\nSave these settings as defaults? (y/n): ").strip().lower()
        if save_conf == 'y':
            save_config(sender_email, recipient_email, sender_password)
        else:
            print("Settings unchanged.")


if __name__ == "__main__":
    main()
