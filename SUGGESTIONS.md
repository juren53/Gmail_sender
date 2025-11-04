# Gmail Sender - Future Improvements

*Generated: 2025-11-03*

This document outlines potential improvements and enhancements for the Quick Gmail Sender project.

---

## Security & Best Practices

### 1. Add requirements.txt
Even though using stdlib, document Python version requirement for better dependency management and reproducibility.

**Benefits:**
- Clear Python version requirements
- Easier setup for new users
- Better CI/CD integration

### 2. Implement keyring support
Use system keychains (Windows Credential Manager, macOS Keychain, Linux Secret Service) instead of base64 encoding.

**Benefits:**
- Much more secure password storage
- OS-native credential management
- No passwords in plain config files

**Implementation:**
```python
import keyring
keyring.set_password("quickmail", username, password)
password = keyring.get_password("quickmail", username)
```

### 3. Add .gitignore patterns
Ensure config files and credentials never get committed.

**Patterns to add:**
```
.gmail_sender_config.json
*.log
__pycache__/
*.pyc
```

---

## Features from "Future Enhancements"

### 4. Command-line arguments
Add flags like `--to`, `--subject`, `--body` for scripting and automation.

**Example usage:**
```bash
python quickmail.py --to user@example.com --subject "Update" --body "Quick message"
python quickmail.py --to user@example.com --subject "Report" --attach report.pdf
```

**Benefits:**
- Scriptable email sending
- Integration with other tools
- Faster one-off emails

### 5. Multiple recipients
Support CC and BCC fields.

**Example usage:**
```bash
python quickmail.py --to main@example.com --cc team@example.com --bcc archive@example.com
```

### 6. File attachments
Add `--attach` flag for sending files.

**Example usage:**
```bash
python quickmail.py --to user@example.com --attach document.pdf image.jpg
```

**Implementation notes:**
- Support multiple attachments
- Validate file exists before sending
- Show file size warnings

### 7. HTML email support
Add `--html` flag or auto-detect HTML content.

**Example usage:**
```bash
python quickmail.py --to user@example.com --html --body "<h1>Hello</h1><p>World</p>"
python quickmail.py --to user@example.com --html-file email.html
```

---

## Code Quality

### 8. Add input validation
Validate email addresses and check for empty fields.

**Validations needed:**
- Email format validation (regex or email-validator library)
- Non-empty required fields
- File existence for attachments
- File size limits

### 9. Better error handling
More specific error messages for different failure scenarios.

**Error scenarios to handle:**
- Invalid email format
- Network connectivity issues
- SMTP server errors
- File not found
- Attachment too large
- Rate limiting

### 10. Add tests
Unit tests for core functions.

**Test coverage:**
- Email sending logic
- Configuration save/load
- Password encoding/decoding
- Input validation
- Error handling

**Framework:**
```bash
pytest tests/
```

### 11. Add logging
Optional verbose mode for debugging.

**Implementation:**
```bash
python quickmail.py --verbose
python quickmail.py --log-file quickmail.log
```

---

## Usability

### 12. Email templates
Store reusable templates with placeholders.

**Example template:**
```json
{
  "templates": {
    "meeting": {
      "subject": "Meeting: {topic}",
      "body": "Hi {name},\n\nLet's meet about {topic} on {date}.\n\nBest,\n{sender}"
    }
  }
}
```

**Usage:**
```bash
python quickmail.py --template meeting --var topic="Project X" --var date="Monday"
```

### 13. Alias support
Use quickmail_alias.txt for common recipient shortcuts.

**Alias file format:**
```
boss: manager@company.com
team: member1@company.com,member2@company.com,member3@company.com
support: support@company.com
```

**Usage:**
```bash
python quickmail.py --to @boss --subject "Update"
python quickmail.py --to @team --subject "Team announcement"
```

### 14. Batch sending
Send to multiple recipients from a file.

**Recipients file (recipients.txt):**
```
user1@example.com
user2@example.com
user3@example.com
```

**Usage:**
```bash
python quickmail.py --recipients recipients.txt --subject "Newsletter"
```

### 15. Draft mode
Save drafts without sending.

**Usage:**
```bash
python quickmail.py --draft --save-as my-draft.json
python quickmail.py --send-draft my-draft.json
```

---

## Documentation

### 16. Add installation section
How to add to PATH for global use.

**Windows:**
```powershell
# Add to PowerShell profile
$profile | Set-Alias qm "C:\path\to\qm.ps1"
```

**Unix/Linux/macOS:**
```bash
# Add to ~/.bashrc or ~/.zshrc
alias qm='python3 /path/to/quickmail.py'
# Or create symlink
ln -s /path/to/quickmail.py /usr/local/bin/qm
```

### 17. Add examples
More real-world usage examples in README.

**Examples to add:**
- Sending daily reports
- Integration with cron/Task Scheduler
- Using with other scripts
- Template usage scenarios
- Alias management

---

## Priority Recommendations

### High Priority
1. ✅ Keyring support (security)
2. ✅ Command-line arguments (usability)
3. ✅ Input validation (reliability)
4. ✅ Alias support (already has quickmail_alias.txt file)

### Medium Priority
5. File attachments
6. Multiple recipients (CC/BCC)
7. Better error handling
8. Email templates

### Low Priority
9. HTML email support
10. Tests
11. Batch sending
12. Draft mode

---

## Notes

- The project already includes `quickmail_alias.txt` - this feature may be partially implemented or planned
- Version in code: 0.2.0 (2025-11-04 07:25:57)
- Focus on maintaining simplicity and CLI-first design
- Consider creating a separate GUI version as a different project
