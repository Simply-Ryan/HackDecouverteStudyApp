import sqlite3

conn = sqlite3.connect('sessions.db')

try:
    # Create call_sessions table
    conn.execute('''
        CREATE TABLE IF NOT EXISTS call_sessions (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            session_id INTEGER NOT NULL,
            call_type TEXT NOT NULL,
            started_by INTEGER NOT NULL,
            started_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            ended_at TIMESTAMP,
            duration INTEGER,
            participant_count INTEGER DEFAULT 1,
            quality_rating INTEGER,
            notes TEXT,
            FOREIGN KEY (session_id) REFERENCES sessions(id) ON DELETE CASCADE,
            FOREIGN KEY (started_by) REFERENCES users(id)
        )
    ''')
    print('Created call_sessions table')
    
    # Create call_participants table
    conn.execute('''
        CREATE TABLE IF NOT EXISTS call_participants (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            call_session_id INTEGER NOT NULL,
            user_id INTEGER NOT NULL,
            joined_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            left_at TIMESTAMP,
            duration INTEGER,
            FOREIGN KEY (call_session_id) REFERENCES call_sessions(id) ON DELETE CASCADE,
            FOREIGN KEY (user_id) REFERENCES users(id)
        )
    ''')
    print('Created call_participants table')
    
    conn.commit()
    print('Done!')
except Exception as e:
    print(f'Error: {e}')
finally:
    conn.close()
