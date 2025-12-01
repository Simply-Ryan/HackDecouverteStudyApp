"""
Migration script to add message reactions and threading support
Run this to upgrade existing databases to v1.4.0
"""

import sqlite3

DATABASE = 'sessions.db'

def migrate():
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()
    
    print("Starting migration for message reactions and threading...")
    
    # Add parent_message_id column to messages table
    try:
        cursor.execute("ALTER TABLE messages ADD COLUMN parent_message_id INTEGER REFERENCES messages(id)")
        print("✓ Added parent_message_id column to messages table")
    except sqlite3.OperationalError as e:
        if "duplicate column" in str(e).lower():
            print("⚠ parent_message_id column already exists")
        else:
            print(f"✗ Error adding parent_message_id: {e}")
    
    # Create message_reactions table
    try:
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS message_reactions (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                message_id INTEGER NOT NULL,
                user_id INTEGER NOT NULL,
                emoji TEXT NOT NULL,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                FOREIGN KEY (message_id) REFERENCES messages(id),
                FOREIGN KEY (user_id) REFERENCES users(id),
                UNIQUE(message_id, user_id, emoji)
            )
        ''')
        print("✓ Created message_reactions table")
    except sqlite3.OperationalError as e:
        print(f"⚠ message_reactions table might already exist: {e}")
    
    conn.commit()
    conn.close()
    
    print("\nMigration completed successfully!")
    print("Your database is now ready for message reactions and threading.")

if __name__ == '__main__':
    migrate()
