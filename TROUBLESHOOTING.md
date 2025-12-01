# 🔧 Troubleshooting Guide

Common issues and their solutions for StudyFlow.

## 📋 Table of Contents

- [Installation Issues](#installation-issues)
- [Database Problems](#database-problems)
- [Authentication Errors](#authentication-errors)
- [File Upload Issues](#file-upload-issues)
- [Chat Not Working](#chat-not-working)
- [Email/Reminder Problems](#emailreminder-problems)
- [Performance Issues](#performance-issues)
- [Browser Compatibility](#browser-compatibility)

---

## 🛠️ Installation Issues

### "pip: command not found"

**Problem**: pip is not installed or not in PATH

**Solution**:
```bash
# Windows
python -m ensurepip --upgrade

# macOS/Linux
python3 -m ensurepip --upgrade

# Or install pip separately
curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py
python get-pip.py
```

### "No module named 'flask'"

**Problem**: Dependencies not installed

**Solution**:
```bash
# Ensure you're in the project directory
cd HackDecouverteStudyApp

# Install dependencies
pip install -r requirements.txt

# If using virtual environment, activate it first
source venv/bin/activate  # macOS/Linux
venv\Scripts\activate     # Windows
```

### "ModuleNotFoundError: No module named 'werkzeug.security'"

**Problem**: Outdated Flask/Werkzeug version

**Solution**:
```bash
pip install --upgrade Flask Werkzeug
```

---

## 🗄️ Database Problems

### "no such table: users"

**Problem**: Database not initialized

**Solution**:
```bash
python init_db.py
```

If that doesn't work:
```bash
# Delete existing database
rm sessions.db  # macOS/Linux
del sessions.db # Windows

# Recreate
python init_db.py
```

### "database is locked"

**Problem**: SQLite database accessed by multiple processes

**Solutions**:

1. **Close other connections**:
   - Close any open database browsers (DB Browser for SQLite)
   - Stop any running instances of the app
   
2. **Reset database**:
   ```bash
   python reset_db.py
   python init_db.py
   ```

3. **For production**: Migrate to PostgreSQL (see DEPLOYMENT.md)

### "UNIQUE constraint failed: users.username"

**Problem**: Trying to create account with existing username

**Solution**: Choose a different username or log in with existing account

### Database corruption

**Problem**: Database file corrupted

**Solution**:
```bash
# Backup if possible
cp sessions.db sessions.db.backup

# Check integrity
sqlite3 sessions.db "PRAGMA integrity_check;"

# If corrupted, reset
python reset_db.py
python init_db.py
```

---

## 🔐 Authentication Errors

### "Invalid username or password"

**Possible causes**:
1. Incorrect credentials
2. Account doesn't exist
3. Password was changed

**Solutions**:
- Double-check username/password (case-sensitive)
- Try signing up if account doesn't exist
- Reset password (if feature implemented)

### Logged out unexpectedly

**Problem**: Session expired or cleared

**Solutions**:
- Log in again
- Check if cookies are enabled
- Ensure browser isn't in private/incognito mode

### "Please log in to access this page"

**Problem**: Trying to access protected page without authentication

**Solution**: Log in first, then access the page

---

## 📁 File Upload Issues

### "File too large"

**Problem**: File exceeds 100MB limit

**Solution**:
- Compress file (use ZIP for documents)
- Split into smaller files
- Use external file sharing (Google Drive, Dropbox) and share link in chat

### "File type not allowed"

**Problem**: File extension not in allowed list

**Allowed types**: png, jpg, jpeg, gif, pdf, doc, docx, xls, xlsx, ppt, pptx, txt, zip, rar

**Solution**:
- Convert file to allowed format
- ZIP unsupported file types
- Request feature to support additional formats

### Upload appears to hang

**Problem**: Large file taking time, or connection issue

**Solutions**:
- Wait longer (100MB can take several minutes)
- Check internet connection
- Try smaller file first to test
- Check browser console for errors (F12)

### File preview not working

**Problem**: Browser can't display file type

**Solutions**:
- Ensure file is image (PNG/JPG/GIF) or PDF
- Try downloading instead of previewing
- Clear browser cache
- Try different browser

### Uploaded file not appearing

**Problem**: File saved but not displayed, or real-time update not working

**Solutions**:
1. **Refresh page** (F5)
2. **Check file context**: File might be in chat instead of study materials (or vice versa)
3. **Check permissions**: You must be RSVP'd to session
4. **Verify upload succeeded**: Check for error message

---

## 💬 Chat Not Working

### Messages not appearing

**Problem**: Real-time polling not working

**Solutions**:

1. **Refresh page** (F5)
2. **Check browser console** (F12 → Console tab):
   - Look for JavaScript errors
   - Look for failed network requests
3. **Verify you're RSVP'd** to the session
4. **Check if session still exists**

### Message duplication

**Problem**: Messages appearing multiple times

**Solution**: Already fixed in current version. If still occurring:
- Clear browser cache
- Hard refresh (Ctrl+Shift+R or Cmd+Shift+R)
- Check for multiple tabs open with same session

### Can't send messages

**Problem**: Send button not working

**Checks**:
- Are you logged in?
- Are you RSVP'd to the session?
- Is the message box empty? (can't send blank messages)
- Check browser console for errors

### Real-time updates stopped

**Problem**: New messages not appearing automatically

**Solutions**:
- Check internet connection
- Look for JavaScript errors in console
- Refresh page to restart polling
- Close and reopen the session

---

## 📧 Email/Reminder Problems

### Not receiving reminder emails

**Possible causes**:
1. Email not configured in app
2. SMTP credentials incorrect
3. Email in spam folder
4. Email service blocking automated emails

**Solutions**:

1. **Check spam/junk folder**

2. **Verify email configuration** in `app.py`:
   ```python
   app.config['MAIL_SERVER'] = 'smtp.gmail.com'
   app.config['MAIL_PORT'] = 587
   app.config['MAIL_USERNAME'] = 'your-email@gmail.com'
   app.config['MAIL_PASSWORD'] = 'your-app-password'
   ```

3. **For Gmail**:
   - Enable 2-Factor Authentication
   - Generate App Password: [myaccount.google.com/apppasswords](https://myaccount.google.com/apppasswords)
   - Use app password instead of regular password

4. **Test email manually**:
   ```python
   # In Python console
   from app import app, send_reminder
   with app.app_context():
       # Check if reminders are scheduled
       # Look for error messages
   ```

5. **Check scheduler is running**:
   - Scheduler runs in background
   - Reminders sent 24 hours before session
   - Check terminal/logs for errors

### Email sent but not received

**Problem**: SMTP working but email not arriving

**Solutions**:
- Whitelist sender email
- Check email provider's spam settings
- Try different email address
- Verify email address is correct in user account

---

## ⚡ Performance Issues

### App is slow

**Possible causes**:
1. Large database
2. Many uploaded files
3. Too many simultaneous users
4. Inefficient queries

**Solutions**:

1. **Clear old sessions**:
   ```sql
   -- In sqlite3 sessions.db
   DELETE FROM sessions WHERE date < date('now', '-30 days');
   ```

2. **Clean up old files**:
   ```bash
   # Check uploads folder size
   du -sh uploads/  # macOS/Linux
   
   # Manually remove old files if needed
   ```

3. **Optimize database**:
   ```sql
   VACUUM;
   ```

4. **Add indexes** (for production):
   ```sql
   CREATE INDEX idx_sessions_date ON sessions(date);
   CREATE INDEX idx_messages_session ON messages(session_id);
   CREATE INDEX idx_files_session ON files(session_id);
   ```

5. **Upgrade hardware** or move to better hosting

### Chat updates are delayed

**Problem**: 3-second polling interval may seem slow

**Solutions**:
- Reduce polling interval in `detail.html`:
  ```javascript
  setInterval(checkForNewMessages, 2000); // 2 seconds instead of 3
  ```
- Implement WebSockets for instant updates (future enhancement)

### Page load is slow

**Problem**: Too much data loading at once

**Solutions**:
- Implement pagination for messages
- Lazy load files (load thumbnails first)
- Use CDN for Font Awesome and Google Fonts
- Minify CSS/JavaScript

---

## 🌐 Browser Compatibility

### Styles not appearing correctly

**Problem**: CSS not loading or browser doesn't support features

**Solutions**:
- Hard refresh (Ctrl+Shift+R or Cmd+Shift+R)
- Clear browser cache
- Update browser to latest version
- Try different browser (Chrome/Edge recommended)

### JavaScript features not working

**Problem**: Browser doesn't support ES6+

**Solution**: Update browser or use polyfills

### Glass morphism effects not showing

**Problem**: Browser doesn't support `backdrop-filter`

**Affected browsers**: 
- Safari < 14
- Firefox < 103 (without flag)

**Solution**: 
- Update browser
- Fallback styles automatically applied (solid background instead of blur)

### Mobile layout broken

**Problem**: Responsive design not working

**Solutions**:
- Check viewport meta tag in HTML
- Test in Chrome DevTools responsive mode
- Report specific device/browser in issue tracker

---

## 🔍 Debugging Tips

### Enable Debug Mode

**For development only** (never in production):

```python
# In app.py
if __name__ == '__main__':
    app.run(debug=True)
```

This provides:
- Detailed error pages
- Auto-reload on code changes
- Interactive debugger

### Check Browser Console

Press F12 and go to Console tab to see:
- JavaScript errors
- Network requests
- Console.log output

### Check Network Requests

In DevTools Network tab:
- See all AJAX requests
- Check response status codes
- View request/response data

### Check Flask Logs

Terminal shows:
- HTTP requests
- Status codes
- Error messages

### SQLite Database Browser

Use [DB Browser for SQLite](https://sqlitebrowser.org/) to:
- View database contents
- Run manual queries
- Check data integrity

---

## 🆘 Still Having Issues?

1. **Search existing issues** on GitHub
2. **Create new issue** with:
   - Detailed description
   - Steps to reproduce
   - Error messages
   - Screenshots
   - Environment details (OS, browser, Python version)
3. **Ask in community chat** (if available)
4. **Check documentation**: README.md, QUICKSTART.md, etc.

---

## 📝 Reporting Bugs

When reporting issues, include:

```markdown
**Describe the bug**
Clear description of what's wrong

**To Reproduce**
1. Go to '...'
2. Click on '...'
3. See error

**Expected behavior**
What should happen

**Screenshots**
If applicable

**Environment**
- OS: [e.g., Windows 11]
- Browser: [e.g., Chrome 120]
- Python version: [e.g., 3.10.5]
- Flask version: [run `pip show flask`]

**Error messages**
```
Paste any error messages here
```

**Additional context**
Any other relevant information
```

---

**Last Updated**: November 30, 2025

If you encounter issues not covered here, please open an issue on GitHub!
