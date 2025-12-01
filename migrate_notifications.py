import sqlite3
import os

print("Starting migration for notifications system...")

# connect to database
db_path = 'sessions.db'
if not os.path.exists(db_path):
    print(f"Error: Database '{db_path}' not found!")
    exit(1)

conn = sqlite3.connect(db_path)
cursor = conn.cursor()

try:
    # Create notifications table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS notifications (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id INTEGER NOT NULL,
            type TEXT NOT NULL,
            title TEXT NOT NULL,
            message TEXT NOT NULL,
            link TEXT,
            is_read INTEGER DEFAULT 0,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            FOREIGN KEY (user_id) REFERENCES users(id)
        )
    ''')
    conn.commit()
    print("✓ Created notifications table")
    
    print("\nMigration completed successfully!")
    print("Your database is now ready for the notification system.")
    
except sqlite3.OperationalError as e:
    if "already exists" in str(e):
        print(f"⚠ Table already exists: {e}")
    else:
        print(f"✗ Error during migration: {e}")
        raise
except Exception as e:
    print(f"✗ Unexpected error: {e}")
    raise
finally:
    conn.close()
