import sqlite3

conn = sqlite3.connect('sessions.db')

try:
    conn.execute('ALTER TABLE user_settings ADD COLUMN reminder_timing INTEGER DEFAULT 1')
    print('Added reminder_timing column')
except Exception as e:
    print(f'reminder_timing column may already exist: {e}')

try:
    conn.execute('ALTER TABLE user_settings ADD COLUMN notification_sound TEXT DEFAULT "default"')
    print('Added notification_sound column')
except Exception as e:
    print(f'notification_sound column may already exist: {e}')

conn.commit()
conn.close()
print('Done!')
