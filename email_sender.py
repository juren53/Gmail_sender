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
    sender_password = getpass("Your Gmail App Password (hidden): ")
    
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
