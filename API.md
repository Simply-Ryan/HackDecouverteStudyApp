# 📡 API Documentation

Internal API endpoints for StudyFlow web application.

## Overview

StudyFlow uses a combination of traditional Flask routes (server-side rendering) and AJAX endpoints for real-time features. This document covers the JSON/AJAX endpoints.

## Base URL

```
http://127.0.0.1:5000  (Development)
https://your-domain.com  (Production)
```

## Authentication

All authenticated endpoints require an active session cookie. Users must be logged in via the web interface.

### Session Cookie
- **Name**: `session`
- **Type**: Secure, HttpOnly cookie
- **Expiration**: Browser session

---

## 📨 Chat Endpoints

### Get New Messages

Retrieves messages posted after a specific message ID.

**Endpoint**: `/session/<int:session_id>/messages`

**Method**: `GET`

**Authentication**: Required (must be RSVP'd to session)

**Query Parameters**:
- `after_id` (integer, optional): Return messages with ID greater than this

**Response**:
```json
{
  "messages": [
    {
      "id": 123,
      "username": "john_doe",
      "content": "Hello everyone!",
      "timestamp": "2025-11-30 14:23:45"
    },
    {
      "id": 124,
      "username": "jane_smith", 
      "content": "Hi John!",
      "timestamp": "2025-11-30 14:24:10"
    }
  ]
}
```

**Status Codes**:
- `200 OK`: Success
- `403 Forbidden`: User not RSVP'd to session
- `404 Not Found`: Session doesn't exist

**Example**:
```javascript
fetch('/session/5/messages?after_id=120')
  .then(res => res.json())
  .then(data => {
    data.messages.forEach(msg => {
      console.log(`${msg.username}: ${msg.content}`);
    });
  });
```

---

### Get New Files

Retrieves files uploaded after a specific file ID.

**Endpoint**: `/session/<int:session_id>/files`

**Method**: `GET`

**Authentication**: Required (must be RSVP'd to session)

**Query Parameters**:
- `after_id` (integer, optional): Return files with ID greater than this

**Response**:
```json
{
  "files": [
    {
      "id": 45,
      "filename": "lecture_notes.pdf",
      "upload_date": "2025-11-30 14:30:00",
      "username": "professor_smith",
      "user_id": 7,
      "file_context": "study_material"
    },
    {
      "id": 46,
      "filename": "diagram.png",
      "upload_date": "2025-11-30 14:35:22",
      "username": "student_bob",
      "user_id": 12,
      "file_context": "chat"
    }
  ]
}
```

**File Context Values**:
- `study_material`: File uploaded to study materials section
- `chat`: File shared in chat conversation

**Status Codes**:
- `200 OK`: Success
- `403 Forbidden`: User not RSVP'd to session
- `404 Not Found`: Session doesn't exist

**Example**:
```javascript
fetch('/session/5/files?after_id=40')
  .then(res => res.json())
  .then(data => {
    data.files.forEach(file => {
      console.log(`New file: ${file.filename} by ${file.username}`);
    });
  });
```

---

## 📂 File Endpoints

### Preview File

Serves a file for inline preview (images, PDFs) in the browser.

**Endpoint**: `/file/<int:file_id>/preview`

**Method**: `GET`

**Authentication**: Required (must be RSVP'd to session that owns the file)

**Response**: Binary file data with `Content-Disposition: inline`

**Status Codes**:
- `200 OK`: Success, returns file
- `403 Forbidden`: User not authorized to view file
- `404 Not Found`: File doesn't exist

**Supported Preview Types**:
- Images: PNG, JPG, JPEG, GIF
- Documents: PDF

**Example**:
```html
<!-- Image preview -->
<img src="/file/45/preview" alt="Preview">

<!-- PDF preview -->
<iframe src="/file/45/preview" width="800" height="600"></iframe>
```

---

### Download File

Downloads a file as an attachment.

**Endpoint**: `/file/<int:file_id>/download`

**Method**: `GET`

**Authentication**: Required (must be RSVP'd to session that owns the file)

**Response**: Binary file data with `Content-Disposition: attachment`

**Status Codes**:
- `200 OK`: Success, downloads file
- `403 Forbidden`: User not authorized to download file
- `404 Not Found`: File doesn't exist

**Example**:
```html
<a href="/file/45/download" download>Download File</a>
```

---

## 🔍 Data Models

### Message Object

```typescript
{
  id: number;           // Unique message ID
  username: string;     // Username of sender
  content: string;      // Message text content
  timestamp: string;    // ISO format datetime "YYYY-MM-DD HH:MM:SS"
}
```

### File Object

```typescript
{
  id: number;           // Unique file ID
  filename: string;     // Original filename
  upload_date: string;  // ISO format datetime "YYYY-MM-DD HH:MM:SS"
  username: string;     // Username of uploader
  user_id: number;      // User ID of uploader
  file_context: string; // "study_material" or "chat"
}
```

### Session Object (Partial)

```typescript
{
  id: number;
  title: string;
  description: string;
  date: string;         // "YYYY-MM-DD"
  time: string;         // "HH:MM"
  duration: number;     // Hours
  location: string;
  max_attendees: number;
  creator_id: number;
  creator_username: string;
}
```

---

## 🚀 Real-Time Polling

The frontend uses JavaScript polling to simulate real-time updates:

### Message Polling
- **Interval**: 3 seconds
- **Endpoint**: `/session/<id>/messages?after_id=<last_id>`
- **Triggers**: New message appears in chat

### File Polling
- **Interval**: 5 seconds
- **Endpoint**: `/session/<id>/files?after_id=<last_id>`
- **Triggers**: New file card appears in materials/chat

### Implementation Example

```javascript
let lastMessageId = 0;
let lastFileId = 0;

// Poll for new messages every 3 seconds
setInterval(async () => {
  const response = await fetch(`/session/${sessionId}/messages?after_id=${lastMessageId}`);
  const data = await response.json();
  
  if (data.messages.length > 0) {
    data.messages.forEach(msg => {
      appendMessage(msg);
      lastMessageId = Math.max(lastMessageId, msg.id);
    });
  }
}, 3000);

// Poll for new files every 5 seconds
setInterval(async () => {
  const response = await fetch(`/session/${sessionId}/files?after_id=${lastFileId}`);
  const data = await response.json();
  
  if (data.files.length > 0) {
    data.files.forEach(file => {
      addFileCard(file);
      lastFileId = Math.max(lastFileId, file.id);
    });
  }
}, 5000);
```

---

## 🔒 Security Considerations

### Authorization Checks

All file and message endpoints verify:
1. User is authenticated (has valid session)
2. User has RSVP'd to the session (is a participant)
3. Session exists in database

### Rate Limiting

**Not currently implemented** - Consider adding:
- Max 60 requests per minute per user
- Max 10 file uploads per hour
- Max 100 messages per hour

### File Validation

Uploads are validated for:
- **Max size**: 100MB
- **Allowed extensions**: png, jpg, jpeg, gif, pdf, doc, docx, xls, xlsx, ppt, pptx, txt, zip, rar
- **Filename sanitization**: Uses `werkzeug.utils.secure_filename()`

---

## 🛠️ Error Handling

### Standard Error Response

```json
{
  "error": "Error message here",
  "code": "ERROR_CODE"
}
```

### Common Error Codes

| Code | Status | Description |
|------|--------|-------------|
| `NOT_AUTHENTICATED` | 401 | User not logged in |
| `NOT_AUTHORIZED` | 403 | User lacks permission |
| `NOT_FOUND` | 404 | Resource doesn't exist |
| `VALIDATION_ERROR` | 400 | Invalid input data |
| `FILE_TOO_LARGE` | 413 | File exceeds 100MB |
| `INVALID_FILE_TYPE` | 400 | File extension not allowed |
| `SERVER_ERROR` | 500 | Internal server error |

---

## 📚 Future API Enhancements

Planned additions:

1. **WebSocket Support**
   - Replace polling with real-time WebSocket connections
   - Bidirectional communication for chat

2. **RESTful API**
   - Full REST API for mobile apps
   - JWT authentication
   - Pagination for lists
   - Filtering and sorting

3. **Rate Limiting**
   - Implement Flask-Limiter
   - Per-user and per-IP limits

4. **API Versioning**
   - `/api/v1/` prefix
   - Version headers

5. **Webhooks**
   - Notify external services of events
   - Session reminders, new messages, etc.

---

## 🧪 Testing

### Manual Testing with cURL

**Get Messages**:
```bash
curl -X GET \
  -H "Cookie: session=your-session-cookie" \
  http://127.0.0.1:5000/session/5/messages?after_id=0
```

**Preview File**:
```bash
curl -X GET \
  -H "Cookie: session=your-session-cookie" \
  http://127.0.0.1:5000/file/45/preview \
  --output preview.pdf
```

### JavaScript Fetch Example

```javascript
// Get new messages
async function getNewMessages(sessionId, afterId) {
  try {
    const response = await fetch(
      `/session/${sessionId}/messages?after_id=${afterId}`,
      {
        method: 'GET',
        credentials: 'same-origin'  // Include session cookie
      }
    );
    
    if (!response.ok) {
      throw new Error(`HTTP error! status: ${response.status}`);
    }
    
    const data = await response.json();
    return data.messages;
  } catch (error) {
    console.error('Failed to fetch messages:', error);
    return [];
  }
}
```

---

## 📞 Support

For API questions:
- Review this documentation
- Check browser console for errors
- Inspect network requests in DevTools
- Verify authentication/authorization

---

**Last Updated**: November 30, 2025
