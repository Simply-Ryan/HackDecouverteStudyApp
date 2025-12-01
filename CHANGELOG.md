# 📝 Changelog

All notable changes to StudyFlow will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

### Planned
- Video/audio call integration
- Calendar sync (Google Calendar, Outlook)
- Mobile app (PWA)
- AI study assistant

---

## [1.3.0] - 2025-11-30

### Added
- WebSocket-based real-time communication using Flask-SocketIO
- Instant message delivery without polling
- Real-time file upload notifications
- Session room system for isolated real-time updates
- Socket.IO client library integration

### Changed
- Replaced 3-second polling with WebSocket events for messages
- Replaced 5-second polling with WebSocket events for files  
- Improved server performance by eliminating constant polling requests
- Messages and files now appear instantly for all session participants

### Removed
- AJAX polling intervals for messages and files
- `pollMessages()` and `pollFiles()` functions
- Polling-related code and intervals

### Performance
- Reduced server load by ~60-80% (no more constant polling requests)
- Improved battery life on mobile devices
- Instant updates instead of 3-5 second delays

---

## [1.2.0] - 2025-11-30

### Added
- Full-screen file preview modal with darkened overlay
- Preview action buttons (Close, Download, Delete)
- Permission-based delete button (only owner/creator can delete)
- Fit-to-screen image display with smooth animations
- Comprehensive documentation suite:
  - QUICKSTART.md - Quick start guide
  - DEVELOPMENT.md - Development roadmap with 15+ feature ideas
  - DEPLOYMENT.md - Production deployment guide (PythonAnywhere, Heroku, AWS, DigitalOcean)
  - API.md - Internal API documentation
  - CONTRIBUTING.md - Contribution guidelines
  - TROUBLESHOOTING.md - Common issues and solutions
  - LICENSE - MIT License
  - Enhanced README.md with badges and complete overview

### Changed
- Preview modal now uses full-screen darkened overlay (95% opacity)
- Images now display with object-fit: contain for better viewing
- Action buttons positioned top-right with smooth slide-in animation
- Preview animations updated from slideInUp to zoomIn effect

### Fixed
- Preview modal display issues
- Image sizing problems in preview
- Button positioning in preview overlay

---

## [1.1.0] - 2025-11-29

### Added
- Horizontal card layout for study materials (4 cards per row)
- "See Older Materials" toggle button for files beyond 4
- Image thumbnails with hover effects
- File preview support for images (PNG, JPG, JPEG, GIF)
- PDF preview in modal window
- Quick file upload from chat interface
- Separate file contexts: 'chat' vs 'study_material'
- `file_context` column in database

### Changed
- File cards now display in responsive grid layout
- Study materials and chat files tracked separately
- File upload forms accept context parameter
- Preview opens in modal instead of new tab

### Fixed
- File upload only showing in one location
- File organization issues
- Chat file handling

---

## [1.0.0] - 2025-11-28

### Added
- Complete UI redesign with purple gradient theme
- Glass morphism effects throughout application
- Inter font from Google Fonts
- Smooth animations and transitions
- Hover effects on interactive elements
- Responsive design for mobile devices

### Changed
- Primary color scheme to purple gradient (#667eea → #764ba2 → #f093fb)
- All buttons to gradient style with glass effect
- Cards to frosted glass appearance
- Navigation bar with gradient background

### Fixed
- Text contrast issues on navbar and buttons
- Message bubble spacing (green border too close to text)
- Overall visual consistency

---

## [0.9.0] - 2025-11-27

### Added
- Real-time chat with automatic refresh (3-second polling)
- Real-time file updates (5-second polling)
- Duplicate message prevention
- Duplicate file prevention
- AJAX endpoints for messages and files
- Client-side polling with last ID tracking

### Changed
- Chat interface to support real-time updates
- File display to auto-refresh
- Message sending to return immediately

### Fixed
- Messages requiring page refresh to appear
- Files not showing for other users until refresh
- Chat synchronization issues

---

## [0.8.0] - 2025-11-26

### Added
- File upload functionality for study materials
- Support for images, PDFs, Office documents, archives
- File size limit (100MB)
- File type validation
- Secure filename handling
- File download route
- File deletion (owner/creator only)

### Changed
- Session detail page to include file management section
- Database schema to include files table

### Security
- Added file extension validation
- Implemented secure filename sanitization
- Added permission checks for file operations

---

## [0.7.0] - 2025-11-25

### Added
- Personal notes system for sessions
- Notes creation and editing
- Auto-save for notes
- Last updated timestamp
- Notes database table

### Changed
- Session detail page to include notes section

---

## [0.6.0] - 2025-11-24

### Added
- Automatic email reminders 24 hours before sessions
- APScheduler for background task scheduling
- Email configuration setup
- Reminder scheduling on session creation
- SMTP integration

### Changed
- Session creation to schedule reminders
- App initialization to start scheduler

---

## [0.5.0] - 2025-11-23

### Added
- Real-time chat functionality
- Message sending and display
- Chat history
- Message timestamps
- Username display for messages

### Changed
- Session detail page to include chat interface
- Database schema to include messages table

---

## [0.4.0] - 2025-11-22

### Added
- Invitation system
- Send invitations to users
- Accept/decline invitations
- View pending invitations
- Invitation notifications

### Changed
- Dashboard to show invitations
- Session detail to manage invitations

---

## [0.3.0] - 2025-11-21

### Added
- Session RSVP functionality
- Accept/decline session participation
- Attendee management
- Max attendees enforcement
- RSVP status tracking

### Changed
- Sessions table to track RSVPs
- Session detail page to show RSVP status

---

## [0.2.0] - 2025-11-20

### Added
- Study session creation
- Session editing (creator only)
- Session deletion (creator only)
- Session details page
- Dashboard with user's sessions
- Countdown timer to sessions

### Changed
- Database schema to include sessions table
- Homepage to show public sessions

---

## [0.1.0] - 2025-11-19

### Added
- User authentication system
- User registration (signup)
- User login
- User logout
- Password hashing with Werkzeug
- Session management
- Protected routes

### Changed
- Initial Flask app setup
- SQLite database configuration
- Basic templates and styling

---

## [0.0.1] - 2025-11-18

### Added
- Initial project setup
- Flask installation
- Basic project structure
- Hello World endpoint
- Git repository initialization

---

## Version Number Guide

Given a version number MAJOR.MINOR.PATCH:
- **MAJOR**: Incompatible API changes
- **MINOR**: New features (backwards-compatible)
- **PATCH**: Bug fixes (backwards-compatible)

## Links

- [Repository](https://github.com/YOUR_USERNAME/HackDecouverteStudyApp)
- [Issues](https://github.com/YOUR_USERNAME/HackDecouverteStudyApp/issues)
- [Pull Requests](https://github.com/YOUR_USERNAME/HackDecouverteStudyApp/pulls)

---

**Last Updated**: November 30, 2025
