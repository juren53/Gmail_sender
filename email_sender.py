#!/usr/bin/env python3
"""
Simple CLI Email Sender for Gmail
Quickly send emails without opening the full Gmail interface.
"""

import smtplib
import sys
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from getpass import getpass

try:
    import msvcrt
    WINDOWS = True
except ImportError:
    import tty
    import termios
    WINDOWS = False


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


def main():
    """Main CLI interface for sending emails."""
    print("=== Quick Gmail Sender ===\n")
    
    # Get email details from user
    sender_email = input("Your Gmail address: ").strip()
    sender_password = getpass_with_asterisks("Your Gmail App Password: ")
    
    print()
    recipient_email = input("Recipient email: ").strip()
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
    
    confirm = input("\nSend this email? (y/n): ").strip().lower()
    if confirm != 'y':
        print("Cancelled.")
        return
    
    # Send the email
    send_email(sender_email, sender_password, recipient_email, subject, body)


if __name__ == "__main__":
    main()
