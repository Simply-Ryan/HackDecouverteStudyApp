#!/usr/bin/env python3
"""
Migration script to add flashcard tables to the database.
Implements SM-2 spaced repetition algorithm for optimal learning.
"""

import sqlite3
from datetime import datetime

def migrate():
    conn = sqlite3.connect('sessions.db')
    cursor = conn.cursor()
    
    print("🎴 Starting flashcard migration...")
    
    # Create flashcard_decks table
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS flashcard_decks (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        title TEXT NOT NULL,
        description TEXT,
        session_id INTEGER,
        user_id INTEGER NOT NULL,
        is_public INTEGER DEFAULT 0,
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
        updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
        FOREIGN KEY (session_id) REFERENCES sessions(id) ON DELETE SET NULL,
        FOREIGN KEY (user_id) REFERENCES users(id) ON DELETE CASCADE
    )
    ''')
    print("✓ Created flashcard_decks table")
    
    # Create flashcards table
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS flashcards (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        deck_id INTEGER NOT NULL,
        question TEXT NOT NULL,
        answer TEXT NOT NULL,
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
        FOREIGN KEY (deck_id) REFERENCES flashcard_decks(id) ON DELETE CASCADE
    )
    ''')
    print("✓ Created flashcards table")
    
    # Create flashcard_progress table for SM-2 algorithm
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS flashcard_progress (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        flashcard_id INTEGER NOT NULL,
        user_id INTEGER NOT NULL,
        easiness_factor REAL DEFAULT 2.5,
        interval INTEGER DEFAULT 0,
        repetitions INTEGER DEFAULT 0,
        next_review_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
        last_reviewed TIMESTAMP,
        FOREIGN KEY (flashcard_id) REFERENCES flashcards(id) ON DELETE CASCADE,
        FOREIGN KEY (user_id) REFERENCES users(id) ON DELETE CASCADE,
        UNIQUE(flashcard_id, user_id)
    )
    ''')
    print("✓ Created flashcard_progress table (SM-2 algorithm)")
    
    # Create index for faster queries
    cursor.execute('''
    CREATE INDEX IF NOT EXISTS idx_flashcard_progress_next_review 
    ON flashcard_progress(user_id, next_review_date)
    ''')
    print("✓ Created index for review dates")
    
    conn.commit()
    conn.close()
    
    print("\n✅ Flashcard migration completed successfully!")
    print("   - flashcard_decks: Store deck metadata")
    print("   - flashcards: Store individual cards (question/answer)")
    print("   - flashcard_progress: Track SM-2 spaced repetition for each user")

if __name__ == '__main__':
    migrate()
