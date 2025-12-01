# 🚀 Quick Start Guide

Get StudyFlow up and running in 5 minutes!

## Prerequisites

- Python 3.8 or higher
- pip (Python package manager)
- Git (optional, for cloning)

## Installation Steps

### 1. Clone or Download the Project

```bash
git clone <your-repo-url>
cd HackDecouverteStudyApp
```

Or download and extract the ZIP file.

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

### 3. Initialize the Database

```bash
python init_db.py
```

This creates the SQLite database with all necessary tables.

### 4. Run the Application

```bash
python app.py
```

The app will start on `http://127.0.0.1:5000/`

### 5. Create Your First Account

1. Open your browser and navigate to `http://127.0.0.1:5000/`
2. Click "Sign Up" in the navigation bar
3. Fill in your details:
   - Username (unique)
   - Email
   - Password
4. Click "Sign Up"

### 6. Create a Study Session

1. After logging in, click "Create Session"
2. Fill in the session details:
   - **Title**: Name your study session
   - **Description**: What you'll be studying
   - **Date**: When the session will happen
   - **Time**: Start time
   - **Duration**: How long (in hours)
   - **Location**: Where to meet (or "Online")
   - **Max Attendees**: Participant limit
3. Click "Create Session"

### 7. Start Collaborating!

- **Invite Friends**: Share the session link or send invitations
- **Chat**: Use the real-time chat to discuss topics
- **Upload Files**: Share study materials and notes
- **Take Notes**: Keep personal notes for each session
- **Set Reminders**: Get automatic email reminders before sessions

## 🎯 Quick Tips

### For Session Creators:
- You can edit/delete sessions you created
- Manage participants (accept invitations)
- Upload study materials visible to all participants
- Files uploaded to chat are separate from study materials

### For Participants:
- RSVP to sessions you're invited to
- View all your upcoming sessions on the dashboard
- Download shared materials
- Contribute to the chat and upload files
- Preview images and PDFs directly in the browser

### File Uploads:
- **Study Materials**: Organized in a card layout, visible to all
- **Chat Files**: Shared directly in the conversation
- **Supported formats**: Images (PNG, JPG, GIF), PDFs, Office docs, archives
- **Max size**: 100MB per file

## 🔧 Troubleshooting

### Database Issues
If you encounter database errors:
```bash
python reset_db.py  # WARNING: This deletes all data!
python init_db.py
```

### Port Already in Use
If port 5000 is busy:
```python
# In app.py, change the last line to:
app.run(debug=True, port=5001)
```

### Missing Dependencies
If you get import errors:
```bash
pip install --upgrade -r requirements.txt
```

## 🎨 Features at a Glance

| Feature | Description |
|---------|-------------|
| **Authentication** | Secure login/signup with password hashing |
| **Study Sessions** | Create, edit, and manage study sessions |
| **Invitations** | Invite users or request to join sessions |
| **Real-time Chat** | Live messaging with auto-refresh (3s interval) |
| **File Sharing** | Upload images, PDFs, documents (100MB limit) |
| **File Preview** | Full-screen preview for images and PDFs |
| **Notes System** | Personal notes for each session |
| **Email Reminders** | Automatic reminders 24h before sessions |
| **Responsive Design** | Beautiful purple gradient theme with glass morphism |

## 📱 Browser Compatibility

- ✅ Chrome/Edge (Recommended)
- ✅ Firefox
- ✅ Safari
- ✅ Opera

## 🆘 Need Help?

- Check `README.md` for detailed credits and information
- Review `DEVELOPMENT.md` for future features and expansion ideas
- See `DEPLOYMENT.md` for production deployment guide

## 🎉 You're Ready!

Start creating study sessions and collaborating with your friends. Happy studying! 📚✨
