-- OAuth Social Login Migration
-- Adds support for Google OAuth authentication

-- Add OAuth fields to users table
ALTER TABLE users ADD COLUMN oauth_provider TEXT; -- 'google', 'github', 'discord', etc.
ALTER TABLE users ADD COLUMN oauth_id TEXT; -- Provider-specific user ID
ALTER TABLE users ADD COLUMN profile_picture TEXT; -- URL to profile picture from OAuth provider
ALTER TABLE users ADD COLUMN email_verified INTEGER DEFAULT 0; -- OAuth emails are pre-verified

-- Table to store OAuth tokens for API access (optional, for future features)
CREATE TABLE IF NOT EXISTS oauth_tokens (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id INTEGER NOT NULL,
    provider TEXT NOT NULL, -- 'google', 'github', 'discord'
    access_token TEXT NOT NULL,
    refresh_token TEXT,
    token_type TEXT DEFAULT 'Bearer',
    expires_at TIMESTAMP,
    scope TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (user_id) REFERENCES users(id) ON DELETE CASCADE,
    UNIQUE(user_id, provider)
);

-- Index for OAuth lookups
CREATE INDEX IF NOT EXISTS idx_users_oauth ON users(oauth_provider, oauth_id);
CREATE INDEX IF NOT EXISTS idx_oauth_tokens_user ON oauth_tokens(user_id);
