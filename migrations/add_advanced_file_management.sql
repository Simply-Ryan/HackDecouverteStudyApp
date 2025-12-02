-- Migration: Add Advanced File Management
-- Date: 2025-12-02
-- Description: Adds file categories, tags, folders, and version control

-- File categories table
CREATE TABLE IF NOT EXISTS file_categories (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL UNIQUE,
    icon TEXT DEFAULT 'fa-file',
    color TEXT DEFAULT '#667eea',
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Insert default categories
INSERT OR IGNORE INTO file_categories (name, icon, color) VALUES
    ('Notes', 'fa-sticky-note', '#10b981'),
    ('Slides', 'fa-presentation', '#f59e0b'),
    ('Assignments', 'fa-tasks', '#ef4444'),
    ('Resources', 'fa-book', '#667eea'),
    ('Code', 'fa-code', '#8b5cf6'),
    ('Other', 'fa-file', '#6b7280');

-- File tags table
CREATE TABLE IF NOT EXISTS file_tags (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL UNIQUE,
    color TEXT DEFAULT '#667eea',
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- File folders table (for organization)
CREATE TABLE IF NOT EXISTS file_folders (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    session_id INTEGER NOT NULL,
    name TEXT NOT NULL,
    parent_folder_id INTEGER,
    created_by INTEGER NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (session_id) REFERENCES sessions(id) ON DELETE CASCADE,
    FOREIGN KEY (parent_folder_id) REFERENCES file_folders(id) ON DELETE CASCADE,
    FOREIGN KEY (created_by) REFERENCES users(id) ON DELETE CASCADE
);

-- File versions table (for version control)
CREATE TABLE IF NOT EXISTS file_versions (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    file_id INTEGER NOT NULL,
    version_number INTEGER NOT NULL,
    filename TEXT NOT NULL,
    file_size INTEGER NOT NULL,
    uploaded_by INTEGER NOT NULL,
    uploaded_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    change_description TEXT,
    FOREIGN KEY (file_id) REFERENCES files(id) ON DELETE CASCADE,
    FOREIGN KEY (uploaded_by) REFERENCES users(id) ON DELETE CASCADE
);

-- Update files table with new columns
ALTER TABLE files ADD COLUMN category_id INTEGER REFERENCES file_categories(id);
ALTER TABLE files ADD COLUMN folder_id INTEGER REFERENCES file_folders(id);
ALTER TABLE files ADD COLUMN version INTEGER DEFAULT 1;
ALTER TABLE files ADD COLUMN is_archived INTEGER DEFAULT 0;

-- File-Tag relationship (many-to-many)
CREATE TABLE IF NOT EXISTS file_tag_relationships (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    file_id INTEGER NOT NULL,
    tag_id INTEGER NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (file_id) REFERENCES files(id) ON DELETE CASCADE,
    FOREIGN KEY (tag_id) REFERENCES file_tags(id) ON DELETE CASCADE,
    UNIQUE(file_id, tag_id)
);

-- File favorites (for quick access)
CREATE TABLE IF NOT EXISTS file_favorites (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    file_id INTEGER NOT NULL,
    user_id INTEGER NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (file_id) REFERENCES files(id) ON DELETE CASCADE,
    FOREIGN KEY (user_id) REFERENCES users(id) ON DELETE CASCADE,
    UNIQUE(file_id, user_id)
);

-- Create indexes
CREATE INDEX IF NOT EXISTS idx_files_category ON files(category_id);
CREATE INDEX IF NOT EXISTS idx_files_folder ON files(folder_id);
CREATE INDEX IF NOT EXISTS idx_file_folders_session ON file_folders(session_id);
CREATE INDEX IF NOT EXISTS idx_file_folders_parent ON file_folders(parent_folder_id);
CREATE INDEX IF NOT EXISTS idx_file_versions_file ON file_versions(file_id);
CREATE INDEX IF NOT EXISTS idx_file_tag_rel_file ON file_tag_relationships(file_id);
CREATE INDEX IF NOT EXISTS idx_file_tag_rel_tag ON file_tag_relationships(tag_id);
CREATE INDEX IF NOT EXISTS idx_file_favorites_user ON file_favorites(user_id);
