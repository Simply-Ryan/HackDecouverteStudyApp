from flask import Flask, render_template, request, redirect, url_for, flash
import sqlite3

app = Flask(__name__)
app.secret_key = 'your_secret_key'

DATABASE = 'sessions.db'

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
        meeting_link = request.form.get('meeting_link', '')
        location = request.form.get('location', '')
        
        conn = get_db()
        conn.execute('INSERT INTO sessions (title, session_type, subject, meeting_link, location) VALUES (?, ?, ?, ?, ?)',
                     (title, session_type, subject, meeting_link, location))
        conn.commit()
        conn.close()
        flash('Study session created successfully!')
        return redirect(url_for('index'))
    
    return render_template('create.html')

@app.route('/session/<int:session_id>', methods=['GET', 'POST'])
def detail(session_id):
    conn = get_db()
    session = conn.execute('SELECT * FROM sessions WHERE id = ?', (session_id,)).fetchone()
    
    if request.method == 'POST':
        if 'participant_name' in request.form:
            participant_name = request.form['participant_name']
            conn.execute('INSERT INTO rsvps (session_id, participant_name) VALUES (?, ?)',
                         (session_id, participant_name))
            conn.commit()
            flash('RSVP submitted successfully!')
        return redirect(url_for('detail', session_id=session_id))
    
    rsvps = conn.execute('SELECT * FROM rsvps WHERE session_id = ?', (session_id,)).fetchall()
    messages = conn.execute('SELECT * FROM messages WHERE session_id = ? ORDER BY created_at ASC', (session_id,)).fetchall()
    conn.close()
    return render_template('detail.html', session=session, rsvps=rsvps, messages=messages)

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