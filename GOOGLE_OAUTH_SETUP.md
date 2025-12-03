# Google OAuth Setup Guide

This guide will help you set up Google OAuth authentication for StudyFlow.

## Prerequisites
- A Google account
- Access to Google Cloud Console

## Step-by-Step Instructions

### 1. Create a Google Cloud Project

1. Go to [Google Cloud Console](https://console.cloud.google.com/)
2. Click "Select a Project" at the top
3. Click "New Project"
4. Enter project name: "StudyFlow" (or any name you prefer)
5. Click "Create"

### 2. Enable Google+ API

1. In the left sidebar, go to "APIs & Services" → "Library"
2. Search for "Google+ API"
3. Click on it and press "Enable"

### 3. Configure OAuth Consent Screen

1. Go to "APIs & Services" → "OAuth consent screen"
2. Select "External" user type (unless you have a Google Workspace)
3. Click "Create"
4. Fill in the required fields:
   - **App name**: StudyFlow
   - **User support email**: Your email
   - **Developer contact email**: Your email
5. Click "Save and Continue"
6. Skip the "Scopes" section (click "Save and Continue")
7. Add test users if needed (your email address)
8. Click "Save and Continue"

### 4. Create OAuth Credentials

1. Go to "APIs & Services" → "Credentials"
2. Click "Create Credentials" → "OAuth client ID"
3. Select "Web application"
4. Fill in the details:
   - **Name**: StudyFlow Web Client
   - **Authorized JavaScript origins**:
     - `http://localhost:5000`
     - `http://127.0.0.1:5000`
   - **Authorized redirect URIs**:
     - `http://localhost:5000/login/google/callback`
     - `http://127.0.0.1:5000/login/google/callback`
5. Click "Create"
6. **IMPORTANT**: Copy your Client ID and Client Secret

### 5. Configure Environment Variables

1. Open your `.env` file in the StudyFlow project root
2. Add the following lines with your credentials:

```bash
GOOGLE_CLIENT_ID=your-client-id-here.apps.googleusercontent.com
GOOGLE_CLIENT_SECRET=your-client-secret-here
```

3. Save the file

### 6. Test the Integration

1. Start your Flask application:
   ```bash
   python app.py
   ```

2. Navigate to `http://localhost:5000/login`
3. Click "Continue with Google"
4. You should be redirected to Google's login page
5. After logging in, you'll be redirected back to StudyFlow

## Production Deployment

When deploying to production:

1. Add your production domain to:
   - Authorized JavaScript origins: `https://yourdomain.com`
   - Authorized redirect URIs: `https://yourdomain.com/login/google/callback`

2. Update OAuth consent screen to "Published" status (requires verification for large user bases)

3. Update environment variables on your production server

## Troubleshooting

### Error: "redirect_uri_mismatch"
- Make sure your redirect URI in Google Console exactly matches the one used in the application
- Check for trailing slashes and http vs https

### Error: "Access blocked: This app's request is invalid"
- Ensure OAuth consent screen is properly configured
- Add your email as a test user

### Error: "Invalid client"
- Double-check your Client ID and Client Secret in `.env`
- Make sure there are no extra spaces or quotes

## Security Notes

- Never commit your `.env` file to Git
- Keep your Client Secret confidential
- Regularly rotate your credentials
- Use HTTPS in production

## Additional Resources

- [Google OAuth 2.0 Documentation](https://developers.google.com/identity/protocols/oauth2)
- [Authlib Flask Documentation](https://docs.authlib.org/en/latest/client/flask.html)
