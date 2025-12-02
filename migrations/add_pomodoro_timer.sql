-- Migration: Add Pomodoro Timer Tables
-- Date: 2025-12-02
-- Description: Creates tables for Pomodoro timer and focus statistics

-- Pomodoro sessions table
CREATE TABLE IF NOT EXISTS pomodoro_sessions (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id INTEGER NOT NULL,
    session_id INTEGER, -- NULL if personal timer
    duration_minutes INTEGER NOT NULL, -- 25 for work, 5 for short break, 15 for long break
    type TEXT NOT NULL, -- 'work', 'short_break', 'long_break'
    started_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    completed_at TIMESTAMP,
    is_completed INTEGER DEFAULT 0,
    FOREIGN KEY (user_id) REFERENCES users(id) ON DELETE CASCADE,
    FOREIGN KEY (session_id) REFERENCES sessions(id) ON DELETE CASCADE
);

-- Focus statistics table
CREATE TABLE IF NOT EXISTS focus_statistics (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id INTEGER NOT NULL,
    date DATE NOT NULL,
    total_focus_minutes INTEGER DEFAULT 0,
    pomodoros_completed INTEGER DEFAULT 0,
    total_breaks_minutes INTEGER DEFAULT 0,
    FOREIGN KEY (user_id) REFERENCES users(id) ON DELETE CASCADE,
    UNIQUE(user_id, date)
);

-- User preferences for Pomodoro
CREATE TABLE IF NOT EXISTS pomodoro_preferences (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id INTEGER NOT NULL UNIQUE,
    work_duration INTEGER DEFAULT 25,
    short_break_duration INTEGER DEFAULT 5,
    long_break_duration INTEGER DEFAULT 15,
    auto_start_breaks INTEGER DEFAULT 0,
    auto_start_pomodoros INTEGER DEFAULT 0,
    dnd_mode INTEGER DEFAULT 1, -- Do Not Disturb during focus
    ambient_sound TEXT DEFAULT 'none', -- 'none', 'white_noise', 'rain', 'cafe'
    FOREIGN KEY (user_id) REFERENCES users(id) ON DELETE CASCADE
);

-- Create indexes
CREATE INDEX IF NOT EXISTS idx_pomodoro_sessions_user ON pomodoro_sessions(user_id);
CREATE INDEX IF NOT EXISTS idx_pomodoro_sessions_session ON pomodoro_sessions(session_id);
CREATE INDEX IF NOT EXISTS idx_focus_statistics_user_date ON focus_statistics(user_id, date);
