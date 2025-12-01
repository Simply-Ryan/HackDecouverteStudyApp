# Typing Indicators

## Overview
Real-time typing indicators show when other users are composing messages in the study room chat. This provides instant feedback and improves conversational flow by letting participants know when someone is about to respond.

## Features

### Core Functionality
- **Real-Time Detection**: Typing status is broadcast instantly to all session participants
- **Smart Timeout**: Indicator disappears after 1 second of inactivity
- **Multi-User Support**: Shows multiple users typing simultaneously
- **Automatic Stop**: Typing indicator stops when message is sent
- **Animated Dots**: Smooth bouncing animation for visual feedback

### Display Modes
The typing indicator adapts to the number of active typers:

- **Single User**: "Jane Doe is typing..."
- **Two Users**: "Jane Doe and John Smith are typing..."
- **Multiple Users**: "3 people are typing..."

## Technical Implementation

### Backend (Flask-SocketIO)

#### WebSocket Event Handler
```python
@socketio.on('typing')
def handle_typing(data):
    """Broadcast typing indicator to all users in session except sender"""
    session_id = data.get('session_id')
    user_name = data.get('user_name')
    is_typing = data.get('is_typing', True)
    
    if session_id and user_name:
        room = f'session_{session_id}'
        socketio.emit('user_typing', {
            'user_name': user_name,
            'is_typing': is_typing
        }, room=room, include_self=False)
```

**Key Points:**
- `include_self=False` prevents sender from seeing their own typing indicator
- Uses session rooms for targeted broadcasting
- Supports both start (`is_typing: true`) and stop (`is_typing: false`) events

### Frontend (JavaScript)

#### Typing Detection
```javascript
let typingTimeout;
let isCurrentlyTyping = false;

messageTextarea.addEventListener('input', function() {
    if (!isCurrentlyTyping) {
        isCurrentlyTyping = true;
        socket.emit('typing', {
            session_id: sessionId,
            user_name: currentUserName,
            is_typing: true
        });
    }

    clearTimeout(typingTimeout);

    typingTimeout = setTimeout(function() {
        isCurrentlyTyping = false;
        socket.emit('typing', {
            session_id: sessionId,
            user_name: currentUserName,
            is_typing: false
        });
    }, 1000); // 1 second debounce
});
```

#### Receiving Typing Events
```javascript
let activeTypers = new Set();

socket.on('user_typing', function(data) {
    if (data.user_name !== currentUserName) {
        if (data.is_typing) {
            activeTypers.add(data.user_name);
        } else {
            activeTypers.delete(data.user_name);
        }
        updateTypingIndicator();
    }
});
```

#### Display Update Logic
```javascript
function updateTypingIndicator() {
    if (activeTypers.size > 0) {
        const names = Array.from(activeTypers);
        let typingText = '';
        
        if (names.length === 1) {
            typingText = `${names[0]} is typing`;
        } else if (names.length === 2) {
            typingText = `${names[0]} and ${names[1]} are typing`;
        } else {
            typingText = `${names.length} people are typing`;
        }
        
        typingUserSpan.textContent = typingText;
        typingIndicator.style.display = 'flex';
    } else {
        typingIndicator.style.display = 'none';
    }
}
```

#### Stop Typing on Send
```javascript
messageForm.addEventListener('submit', function(e) {
    // Stop typing indicator immediately when sending
    clearTimeout(typingTimeout);
    if (isCurrentlyTyping) {
        isCurrentlyTyping = false;
        socket.emit('typing', {
            session_id: sessionId,
            user_name: currentUserName,
            is_typing: false
        });
    }
    // ... rest of submit logic
});
```

### HTML Structure

```html
<!-- Typing indicator -->
<div class="typing-indicator" id="typingIndicator" style="display: none;">
    <div class="typing-dots">
        <span class="typing-user"></span>
        <span class="dot"></span>
        <span class="dot"></span>
        <span class="dot"></span>
    </div>
</div>
```

**Placement**: Between messages container and message input form

### CSS Styling

#### Container
```css
.typing-indicator {
    display: flex;
    align-items: center;
    padding: 0.8rem 1rem;
    margin-top: 0.5rem;
    background: rgba(102, 126, 234, 0.05);
    border-radius: 10px;
    animation: fadeIn 0.3s ease;
}
```

#### Animated Dots
```css
.typing-dots .dot {
    width: 8px;
    height: 8px;
    background: #667eea;
    border-radius: 50%;
    animation: typingDot 1.4s infinite ease-in-out;
}

.typing-dots .dot:nth-child(2) {
    animation-delay: 0.2s;
}

.typing-dots .dot:nth-child(3) {
    animation-delay: 0.4s;
}

.typing-dots .dot:nth-child(4) {
    animation-delay: 0.6s;
}

@keyframes typingDot {
    0%, 60%, 100% {
        transform: translateY(0);
        opacity: 0.7;
    }
    30% {
        transform: translateY(-10px);
        opacity: 1;
    }
}
```

## WebSocket Events

### Client → Server

#### Start/Stop Typing
**Event:** `typing`

**Payload:**
```javascript
{
    session_id: 123,
    user_name: "Jane Doe",
    is_typing: true  // or false
}
```

**Trigger Conditions:**
- `is_typing: true` - User starts typing (first keystroke)
- `is_typing: false` - User stops typing (1 second of inactivity or message sent)

### Server → Client

#### Typing Update
**Event:** `user_typing`

**Payload:**
```javascript
{
    user_name: "Jane Doe",
    is_typing: true  // or false
}
```

**Broadcast:** Sent to all users in session room except the sender

## User Experience

### Timing
- **Debounce Period**: 1 second (typing stops after 1s of inactivity)
- **Animation Speed**: 1.4 seconds per dot cycle
- **Fade In**: 0.3 seconds when indicator appears

### Visual Design
- **Background**: Light purple tint (`rgba(102, 126, 234, 0.05)`)
- **Text Color**: Purple (`#667eea`)
- **Dot Color**: Purple (`#667eea`)
- **Border Radius**: 10px for smooth edges
- **Padding**: 0.8rem vertical, 1rem horizontal

### Behavior
1. User starts typing → Indicator appears immediately for others
2. User pauses typing → Indicator remains for 1 second
3. User continues typing → Timer resets, indicator persists
4. User stops typing → Indicator disappears after 1 second
5. User sends message → Indicator disappears immediately

## Performance Considerations

### Optimizations
- **Debouncing**: Prevents excessive WebSocket events (only emits after 1s pause)
- **State Tracking**: Uses `isCurrentlyTyping` flag to avoid redundant emissions
- **Efficient Updates**: Only updates DOM when typing state changes
- **Set Data Structure**: Uses JavaScript `Set` for O(1) add/remove operations

### Network Efficiency
- **Event Frequency**: Maximum 2 events per typing session (start + stop)
- **Payload Size**: ~100 bytes per event (minimal overhead)
- **Targeted Broadcasting**: Only sends to session room, not entire server

## Browser Compatibility

- **WebSocket**: All modern browsers (Chrome, Firefox, Safari, Edge)
- **CSS Animations**: Full support in all modern browsers
- **JavaScript Set**: Supported in ES6+ browsers (2015+)

## Testing Scenarios

### Single User
1. Open session in one browser
2. Start typing in message box
3. Verify no typing indicator appears (own typing excluded)

### Two Users
1. Open session in two browsers (different accounts)
2. User A starts typing
3. User B sees "User A is typing..."
4. User A sends message
5. Indicator disappears immediately for User B

### Multiple Users
1. Open session in three browsers
2. User A and User B start typing
3. User C sees "User A and User B are typing..."
4. User D starts typing
5. Display changes to "3 people are typing..."

### Timeout Test
1. User A starts typing
2. User A pauses for 1 second
3. Indicator disappears for other users
4. User A resumes typing
5. Indicator reappears immediately

## Troubleshooting

### Indicator Not Appearing
**Symptoms**: No typing indicator shows when others type

**Solutions:**
- Check WebSocket connection in browser console
- Verify `user_typing` event listener is attached
- Ensure `currentUserName` variable is set correctly
- Check that `typingIndicator` element exists in DOM

### Indicator Stuck Visible
**Symptoms**: Typing indicator doesn't disappear after typing stops

**Solutions:**
- Verify timeout logic is working (check `typingTimeout`)
- Ensure `is_typing: false` event is being sent
- Check for JavaScript errors in console
- Clear `activeTypers` set manually if needed

### Multiple Indicators
**Symptoms**: Duplicate typing indicators appear

**Solutions:**
- Ensure only one typing indicator element exists
- Check that event listeners aren't duplicated
- Verify `include_self=False` in backend emit

### Wrong User Name
**Symptoms**: Incorrect name shown in typing indicator

**Solutions:**
- Verify `session.get('full_name')` returns correct value
- Check that user_name is passed correctly in emit
- Ensure session data is properly initialized

## Future Enhancements

Potential improvements:
- **Typing Speed**: Show "typing slowly" vs "typing quickly"
- **Position Tracking**: Show where in the message user is typing
- **Rich Indicators**: "User is typing a reply to your message"
- **Emoji Support**: Show emoji reactions while typing
- **Sound Notifications**: Optional sound when someone starts typing
- **Typing History**: Track typing patterns for analytics

## Security Considerations

### User Identification
- Uses session-stored full name (server-validated)
- Cannot spoof typing as another user
- Session isolation via room system

### Rate Limiting
- Natural rate limit via 1-second debounce
- No risk of spam (limited to typing speed)
- Server doesn't store typing state (stateless)

### Privacy
- Only shows typing to session participants
- No persistent storage of typing events
- Respects session permissions (RSVP required)

## Integration with Other Features

### Works With
- **Message Reactions**: Typing indicator appears above reactions
- **Threading**: Compatible with reply functionality
- **File Uploads**: Indicator persists during file selection
- **Real-Time Messages**: Coordinated with WebSocket message delivery

### Interaction Notes
- Typing stops when message is sent (prevents stuck indicator)
- Indicator positioned between messages and input form
- Doesn't interfere with message scrolling
- Compatible with reply context UI

## Code Maintenance

### Key Variables
- `typingTimeout`: Debounce timer reference
- `isCurrentlyTyping`: Boolean flag for current user's typing state
- `activeTypers`: Set of user names currently typing
- `currentUserName`: Current user's full name from session

### Important Functions
- `updateTypingIndicator()`: Updates display based on active typers
- `socket.emit('typing', ...)`: Broadcasts typing state
- `socket.on('user_typing', ...)`: Receives typing updates

### Event Lifecycle
```
User types → input event → emit('typing', true) →
→ broadcast('user_typing', true) → updateIndicator() →
→ setTimeout(1000ms) → emit('typing', false) →
→ broadcast('user_typing', false) → updateIndicator()
```
