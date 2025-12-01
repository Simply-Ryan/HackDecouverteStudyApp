# 📚 StudyFlow

A collaborative study session management web application built for **HackDécouverte** (HackConcordia). Create study sessions, invite friends, share materials, chat in real-time, and stay organized with automatic reminders!

![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)
![Flask](https://img.shields.io/badge/Flask-3.0-green.svg)
![License](https://img.shields.io/badge/License-MIT-yellow.svg)

## ✨ Features

### 🎯 Core Functionality
- **User Authentication**: Secure signup/login with password hashing
- **Study Sessions**: Create, edit, and manage study sessions with date/time/location
- **Invitations System**: Invite users or request to join sessions
- **RSVP Management**: Accept/decline invitations and manage attendees
- **Access Control**: Only participants can view session details

### 💬 Collaboration Tools
- **Real-time Chat**: Live messaging with 3-second auto-refresh
- **File Sharing**: Upload and share study materials (images, PDFs, documents)
- **File Preview**: Full-screen preview for images and PDFs with action buttons
- **Quick Upload**: Upload files directly from chat
- **Notes System**: Personal notes for each session

### 🔔 Productivity Features
- **Automatic Reminders**: Email notifications 24 hours before sessions
- **Countdown Timer**: See how much time until your session
- **Dashboard**: View all your upcoming sessions at a glance
- **Search & Filter**: Find sessions easily (coming soon)

### 🎨 Modern Design
- **Purple Gradient Theme**: Beautiful color scheme throughout
- **Glass Morphism**: Frosted glass effects with backdrop blur
- **Responsive Layout**: Works perfectly on mobile, tablet, and desktop
- **Horizontal Cards**: Clean 4-per-row layout for study materials
- **Smooth Animations**: Polished transitions and hover effects

## 🚀 Quick Start

Get up and running in 5 minutes! See **[QUICKSTART.md](QUICKSTART.md)** for detailed instructions.

```bash
# Clone repository
git clone <your-repo-url>
cd HackDecouverteStudyApp

# Install dependencies
pip install -r requirements.txt

# Initialize database
python init_db.py

# Run application
python app.py
```

Visit `http://127.0.0.1:5000` and create your account!

## 📖 Documentation

- **[Quick Start Guide](QUICKSTART.md)** - Get started in minutes
- **[Development Roadmap](DEVELOPMENT.md)** - Future features and expansion ideas
- **[Deployment Guide](DEPLOYMENT.md)** - Deploy to production (PythonAnywhere, Heroku, AWS)
- **[API Documentation](API.md)** - Internal API endpoints reference
- **[Contributing Guide](CONTRIBUTING.md)** - How to contribute to the project

## 🛠️ Tech Stack

### Backend
- **[Flask 3.0](https://flask.palletsprojects.com/)** - Web framework
- **[SQLite3](https://www.sqlite.org/)** - Database
- **[Werkzeug](https://werkzeug.palletsprojects.com/)** - Security (password hashing)
- **[APScheduler](https://apscheduler.readthedocs.io/)** - Automated reminders

### Frontend
- **HTML5** - Semantic markup
- **CSS3** - Modern styling with gradients and animations
- **JavaScript (ES6+)** - Real-time updates and interactivity
- **[Font Awesome 6.5](https://fontawesome.com/)** - Icon library
- **[Google Fonts (Inter)](https://fonts.google.com/)** - Typography

### Development Tools
- **Git & GitHub** - Version control
- **Visual Studio Code** - Code editor
- **Python 3.8+** - Programming language

## 📂 Project Structure

```
HackDecouverteStudyApp/
├── app.py                 # Main Flask application
├── init_db.py            # Database initialization
├── reset_db.py           # Database reset utility
├── schema.sql            # Database schema
├── requirements.txt      # Python dependencies
├── sessions.db           # SQLite database (generated)
├── static/
│   ├── css/
│   │   └── style.css    # Main stylesheet
│   └── js/
│       └── main.js      # Frontend JavaScript
├── templates/           # Jinja2 HTML templates
│   ├── base.html       # Base template
│   ├── index.html      # Homepage
│   ├── dashboard.html  # User dashboard
│   ├── detail.html     # Session detail page
│   └── ...
├── uploads/            # User-uploaded files
├── flask_session/      # Session storage
└── docs/              # Documentation
    ├── QUICKSTART.md
    ├── DEVELOPMENT.md
    ├── DEPLOYMENT.md
    ├── API.md
    └── CONTRIBUTING.md
```

## 🎯 Use Cases

### For Students
- Organize group study sessions for exams
- Share lecture notes and study materials
- Collaborate on assignments
- Stay accountable with scheduled sessions

### For Study Groups
- Plan recurring weekly study sessions
- Build a library of shared resources
- Track attendance and participation
- Communicate in real-time

### For Tutors
- Schedule tutoring sessions
- Share teaching materials
- Manage multiple student groups
- Send automatic session reminders

## 🔐 Security Features

- **Password Hashing**: Werkzeug secure password hashing (SHA-256)
- **Session Management**: Secure Flask sessions with secret key
- **File Validation**: Restricted file types and size limits (100MB)
- **Filename Sanitization**: Prevents directory traversal attacks
- **Access Control**: Permission checks on all sensitive routes
- **SQL Injection Protection**: Parameterized queries throughout

## 🌐 Browser Support

- ✅ Chrome/Edge (Recommended)
- ✅ Firefox
- ✅ Safari
- ✅ Opera

## 📊 Database Schema

**Users Table**:
- id, username (unique), email, password_hash

**Sessions Table**:
- id, title, description, date, time, duration, location, max_attendees, creator_id

**Invitations Table**:
- id, session_id, user_id, status (pending/accepted/declined)

**Messages Table**:
- id, session_id, user_id, content, timestamp

**Files Table**:
- id, session_id, filename, filepath, upload_date, user_id, file_context

**Notes Table**:
- id, user_id, session_id, content, last_updated

## 🤝 Contributing

We welcome contributions! Please see **[CONTRIBUTING.md](CONTRIBUTING.md)** for:
- Code of conduct
- Development workflow
- Coding standards
- Pull request process
- Bug reporting guidelines

## 🐛 Known Issues

- Chat uses polling (3s) instead of WebSockets (planned upgrade)
- File storage is local (consider cloud storage for production)
- No mobile app (PWA coming soon)

## 🔮 Future Features

See **[DEVELOPMENT.md](DEVELOPMENT.md)** for the complete roadmap, including:
- Video/audio call integration
- Calendar sync (Google Calendar, Outlook)
- Advanced file management with search
- Progress tracking and analytics
- Study groups/communities
- AI study assistant
- Mobile app (PWA)
- And much more!

## 📜 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Credits

### Team Name: The Goon Squad

### Front-end
Félix Hardy, Stryker Pinchin

### Back-end
Ryan El Fani, Rafael Ethan Olliver

### Stress Test
Stryker Pinchin, Rafael Ethan Olliver

## Third-Party Libraries & Frameworks

#### Backend
- **[Flask](https://flask.palletsprojects.com/)** Simple Web Framework
  
- **[Werkzeug](https://werkzeug.palletsprojects.com/)** Security functions & some more minor things

- **[Jinja2](https://jinja.palletsprojects.com/)** Templates (included with Flask)

#### Frontend
- **[Font Awesome](https://fontawesome.com/)** Online Icon Database

#### Database
- **SQLite3** - Embedded database (included with Python)

### Development Tools
- **Python** - Programming language
- **Git & GitHub** - Version control (used it for unnecessary things!)
- **Visual Studio Code** - Code editor
- **Stack Overflow, PythonAnywhere, W3Schools** - General Forums Scavenging and assistance
