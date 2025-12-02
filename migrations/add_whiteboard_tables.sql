-- Migration: Add Whiteboard Tables
-- Date: 2025-12-02
-- Description: Creates tables for collaborative whiteboard/canvas feature

-- Main whiteboards table
CREATE TABLE IF NOT EXISTS whiteboards (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    session_id INTEGER NOT NULL,
    title TEXT DEFAULT 'Untitled Whiteboard',
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    created_by INTEGER NOT NULL,
    FOREIGN KEY (session_id) REFERENCES study_sessions(id) ON DELETE CASCADE,
    FOREIGN KEY (created_by) REFERENCES users(id) ON DELETE CASCADE
);

-- Whiteboard canvas data (stores the actual drawing data)
CREATE TABLE IF NOT EXISTS whiteboard_data (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    whiteboard_id INTEGER NOT NULL,
    data_json TEXT NOT NULL, -- JSON string of canvas elements
    version INTEGER DEFAULT 1,
    saved_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    saved_by INTEGER NOT NULL,
    FOREIGN KEY (whiteboard_id) REFERENCES whiteboards(id) ON DELETE CASCADE,
    FOREIGN KEY (saved_by) REFERENCES users(id) ON DELETE CASCADE
);

-- Create indexes for better performance
CREATE INDEX IF NOT EXISTS idx_whiteboards_session ON whiteboards(session_id);
CREATE INDEX IF NOT EXISTS idx_whiteboard_data_whiteboard ON whiteboard_data(whiteboard_id);
CREATE INDEX IF NOT EXISTS idx_whiteboard_data_version ON whiteboard_data(whiteboard_id, version DESC);
