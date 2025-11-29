from flask import Flask, render_template, request, redirect, url_for, flash
import sqlite3
from datetime import datetime

app = Flask(__name__)
app.secret_key = 'your_secret_key'

DATABASE = 'sessions.db'

# Helper function to format session dates
def format_time_remaining(session_date_str):
    """Calculate time remaining until session and return formatted string"""
    if not session_date_str:
        return None
    
    try:
        session_date = datetime.fromisoformat(session_date_str.replace('T', ' '))
        now = datetime.now()
        
        if session_date < now:
            return "Session ended"
        
        delta = session_date - now
        
        if delta.days > 0:
            return f"In {delta.days} day{'s' if delta.days > 1 else ''}"
        elif delta.seconds >= 3600:
            hours = delta.seconds // 3600
            return f"In {hours} hour{'s' if hours > 1 else ''}"
        elif delta.seconds >= 60:
            minutes = delta.seconds // 60
            return f"In {minutes} minute{'s' if minutes > 1 else ''}"
        else:
            return "Starting soon!"
    except:
        return None

app.jinja_env.globals.update(format_time_remaining=format_time_remaining)

def get_db():
    conn = sqlite3.connect(DATABASE)
    conn.row_factory = sqlite3.Row
    return conn

@app.route('/')
def index():
    conn = get_db()
    sessions = conn.execute('SELECT * FROM sessions').fetchall()
    conn.close()
    return render_template('index.html', sessions=sessions)

@app.route('/create', methods=['GET', 'POST'])
def create():
    if request.method == 'POST':
        title = request.form['title']
        session_type = request.form['session_type']
        subject = request.form.get('subject', 'General')
        session_date = request.form.get('session_date', '')
        max_participants = request.form.get('max_participants', 10)
        meeting_link = request.form.get('meeting_link', '')
        location = request.form.get('location', '')
        
        conn = get_db()
        conn.execute('INSERT INTO sessions (title, session_type, subject, session_date, max_participants, meeting_link, location) VALUES (?, ?, ?, ?, ?, ?, ?)',
                     (title, session_type, subject, session_date, max_participants, meeting_link, location))
        conn.commit()
        conn.close()
        flash('Study session created successfully!')
        return redirect(url_for('index'))
    
    return render_template('create.html')

@app.route('/session/<int:session_id>', methods=['GET', 'POST'])
def detail(session_id):
    conn = get_db()
    session = conn.execute('SELECT * FROM sessions WHERE id = ?', (session_id,)).fetchone()
    rsvps = conn.execute('SELECT * FROM rsvps WHERE session_id = ?', (session_id,)).fetchall()
    
    if request.method == 'POST':
        if 'participant_name' in request.form:
            # Check if session is full
            current_count = len(rsvps)
            max_participants = session['max_participants'] if session['max_participants'] else 10
            
            if current_count >= max_participants:
                flash('Sorry, this session is full!')
            else:
                participant_name = request.form['participant_name']
                conn.execute('INSERT INTO rsvps (session_id, participant_name) VALUES (?, ?)',
                             (session_id, participant_name))
                conn.commit()
                flash('RSVP submitted successfully!')
        return redirect(url_for('detail', session_id=session_id))
    
    messages = conn.execute('SELECT * FROM messages WHERE session_id = ? ORDER BY created_at ASC', (session_id,)).fetchall()
    conn.close()
    
    # Calculate capacity info
    current_count = len(rsvps)
    max_participants = session['max_participants'] if session['max_participants'] else 10
    is_full = current_count >= max_participants
    spots_left = max_participants - current_count
    
    return render_template('detail.html', session=session, rsvps=rsvps, messages=messages,
                         current_count=current_count, max_participants=max_participants,
                         is_full=is_full, spots_left=spots_left)

@app.route('/session/<int:session_id>/message', methods=['POST'])
def post_message(session_id):
    sender_name = request.form.get('sender_name', 'Anonymous')
    message_text = request.form.get('message_text', '')
    
    if message_text.strip():
        conn = get_db()
        conn.execute('INSERT INTO messages (session_id, sender_name, message_text) VALUES (?, ?, ?)',
                     (session_id, sender_name, message_text))
        conn.commit()
        conn.close()
        flash('Message posted!')
    
    return redirect(url_for('detail', session_id=session_id))

if __name__ == '__main__':
    app.run(debug=True)