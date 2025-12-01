# Message Reactions and Threading

## Overview
The message reactions and threading feature allows users to interact with chat messages in more meaningful ways by adding emoji reactions and creating threaded conversations by replying to specific messages.

## Features

### 1. Message Reactions
Users can react to any message with emoji reactions, similar to Slack or Discord:
- **Supported Emojis**: 👍 ❤️ 😂 🎉 😕 🔥 👏 ✅
- **Toggle Reactions**: Click an emoji to add/remove your reaction
- **Reaction Counts**: See how many users reacted with each emoji
- **Visual Feedback**: User's own reactions are highlighted in purple gradient

### 2. Message Threading
Users can reply to specific messages to create contextual conversations:
- **Reply Button**: Click the reply icon on any message
- **Reply Context**: Shows a preview of the message being replied to
- **Thread Indicator**: Visual indication that a message is a reply
- **Cancel Reply**: Option to cancel reply and send a regular message

## Database Schema

### Messages Table (Updated)
```sql
CREATE TABLE messages (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    session_id INTEGER NOT NULL,
    user_id INTEGER NOT NULL,
    message_text TEXT NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    parent_message_id INTEGER,  -- New column for threading
    FOREIGN KEY (session_id) REFERENCES sessions(id),
    FOREIGN KEY (user_id) REFERENCES users(id),
    FOREIGN KEY (parent_message_id) REFERENCES messages(id)
);
```

### Message Reactions Table (New)
```sql
CREATE TABLE message_reactions (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    message_id INTEGER NOT NULL,
    user_id INTEGER NOT NULL,
    emoji TEXT NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (message_id) REFERENCES messages(id) ON DELETE CASCADE,
    FOREIGN KEY (user_id) REFERENCES users(id) ON DELETE CASCADE,
    UNIQUE(message_id, user_id, emoji)  -- Prevent duplicate reactions
);
```

## API Endpoints

### Add/Remove Reaction
**POST** `/message/<message_id>/react`

**Request Body:**
```json
{
    "emoji": "👍",
    "action": "toggle"  // or "add" or "remove"
}
```

**Response:**
```json
{
    "success": true,
    "data": {
        "message_id": 123,
        "reactions": [
            {
                "emoji": "👍",
                "count": 3,
                "user_ids": [1, 2, 5]
            }
        ]
    }
}
```

### Post Message with Reply
**POST** `/session/<session_id>/message`

**Form Data:**
- `message_text`: The message content
- `parent_message_id`: (Optional) ID of the message being replied to

## WebSocket Events

### Reaction Updated
**Event:** `reaction_updated`

**Payload:**
```javascript
{
    message_id: 123,
    reactions: [
        {
            emoji: "👍",
            count: 3,
            user_ids: [1, 2, 5]
        }
    ]
}
```

### New Message (Enhanced)
**Event:** `new_message`

**Payload (with reply):**
```javascript
{
    id: 456,
    full_name: "John Doe",
    username: "johndoe",
    message_text: "I agree with that!",
    created_at: "2025-11-30 20:45:00",
    user_id: 5,
    parent_message_id: 123,
    parent_info: {
        id: 123,
        text: "This is a great study session",
        author: "Jane Smith"
    },
    reactions: []
}
```

## Frontend Components

### Reaction Picker
When a user clicks the smile icon (😊) on a message, a popup appears with common emoji options:

```html
<div class="reaction-picker">
    <span class="emoji-option">👍</span>
    <span class="emoji-option">❤️</span>
    <span class="emoji-option">😂</span>
    <!-- ... more emojis -->
</div>
```

### Reply Indicator
When replying to a message, a context box appears above the message input:

```html
<div class="reply-indicator">
    <div class="reply-context">
        <i class="fas fa-reply"></i>
        <span>Replying to Jane: "This is a great study session"</span>
        <button class="cancel-reply-btn">×</button>
    </div>
</div>
```

### Message Display
Messages now include reactions, reply context, and action buttons:

```html
<div class="message-item">
    <div class="message-header">...</div>
    
    <!-- Reply reference (if this is a reply) -->
    <div class="reply-reference">
        <i class="fas fa-reply"></i>
        <span>Replying to Jane: "This is a great study session"</span>
    </div>
    
    <!-- Message text -->
    <div class="message-text">I agree with that!</div>
    
    <!-- Reactions -->
    <div class="message-reactions">
        <span class="reaction-badge user-reacted">👍 3</span>
        <span class="reaction-badge">❤️ 1</span>
    </div>
    
    <!-- Action buttons (shown on hover) -->
    <div class="message-actions-btns">
        <button class="msg-action-btn" onclick="showReplyForm(...)">
            <i class="fas fa-reply"></i>
        </button>
        <button class="msg-action-btn" onclick="showReactionPicker(...)">
            <i class="fas fa-smile"></i>
        </button>
    </div>
</div>
```

## JavaScript Functions

### Toggle Reaction
```javascript
function toggleReaction(messageId, emoji) {
    fetch(`/message/${messageId}/react`, {
        method: 'POST',
        headers: {'Content-Type': 'application/json'},
        body: JSON.stringify({ emoji: emoji, action: 'toggle' })
    })
    .then(response => response.json())
    .then(data => {
        // Update handled by WebSocket
    });
}
```

### Show Reply Form
```javascript
function showReplyForm(messageId, authorName, messageText) {
    // Display reply context above message input
    // Set parent_message_id in hidden form field
    replyToMessageId = messageId;
}
```

### Cancel Reply
```javascript
function cancelReply() {
    // Remove reply indicator
    // Clear parent_message_id
    replyToMessageId = null;
}
```

## CSS Styling

### Reaction Badges
```css
.reaction-badge {
    padding: 0.3rem 0.6rem;
    background: rgba(102, 126, 234, 0.1);
    border: 2px solid rgba(102, 126, 234, 0.2);
    border-radius: 20px;
    cursor: pointer;
    transition: all 0.2s ease;
}

.reaction-badge.user-reacted {
    background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
    color: white;
    border-color: #667eea;
}
```

### Reply Reference
```css
.reply-reference {
    padding: 0.5rem 0.8rem;
    background: rgba(102, 126, 234, 0.08);
    border-left: 3px solid #667eea;
    border-radius: 6px;
    color: #667eea;
}
```

### Message Action Buttons
```css
.message-actions-btns {
    opacity: 0;
    transition: opacity 0.2s ease;
}

.message-item:hover .message-actions-btns {
    opacity: 1;  /* Show on hover */
}
```

## Migration

To add reactions and threading to an existing database:

```bash
python migrate_reactions.py
```

This script:
1. Adds `parent_message_id` column to `messages` table
2. Creates `message_reactions` table
3. Handles errors gracefully if columns/tables already exist

## Usage Examples

### Adding a Reaction
1. Hover over any message
2. Click the smile icon (😊)
3. Select an emoji from the picker
4. The reaction appears instantly on the message
5. Other users see the update in real-time via WebSocket

### Replying to a Message
1. Hover over any message
2. Click the reply icon (↩️)
3. A reply context appears above the message input
4. Type your reply
5. Send the message
6. Your reply shows with a reference to the original message

### Removing a Reaction
1. Click on a reaction badge you've already added
2. The reaction is removed instantly
3. If no reactions remain, the reactions section disappears

## Real-Time Updates

All reaction and message actions are broadcast in real-time using WebSocket:
- When a user adds/removes a reaction, all participants see the update instantly
- New replies show the parent message context immediately
- No page refresh required

## Performance Considerations

- **Efficient Queries**: Reactions are grouped by emoji with single SQL query
- **WebSocket Broadcasting**: Only updates affected message, not entire chat
- **Lazy Loading**: Reaction picker created on-demand, not pre-loaded
- **CSS Animations**: Smooth transitions for better UX without performance impact

## Browser Compatibility

- **Emoji Support**: All modern browsers (Chrome, Firefox, Safari, Edge)
- **WebSocket**: Requires Socket.IO library (included via CDN)
- **CSS Features**: Uses modern CSS (flexbox, gradients, transitions)

## Future Enhancements

Potential improvements for this feature:
- Custom emoji support (upload custom reactions)
- Reaction notifications (notify when someone reacts to your message)
- Thread view (collapse/expand full conversation threads)
- Reaction analytics (most popular reactions, emoji usage stats)
- @mentions in replies (notify specific users)
- Pinned messages (highlight important messages)

## Troubleshooting

### Reactions not appearing
- Check browser console for JavaScript errors
- Verify WebSocket connection is established
- Check that migration script ran successfully

### Duplicate reactions
- Verify UNIQUE constraint exists on `message_reactions` table
- Check frontend logic prevents double-clicking

### Reply context not showing
- Ensure `parent_message_id` column exists in `messages` table
- Check that parent message is fetched in backend query
- Verify JavaScript `showReplyForm()` function is defined

## Security Considerations

- **Input Validation**: Emoji field validated on backend
- **Authorization**: Users can only react if logged in and RSVP'd
- **SQL Injection**: Parameterized queries prevent injection attacks
- **XSS Prevention**: Message text escaped in frontend display
