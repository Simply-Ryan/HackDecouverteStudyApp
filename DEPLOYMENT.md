# 🚀 Deployment Guide

Complete guide for deploying StudyFlow to production.

## 📋 Pre-Deployment Checklist

- [ ] All tests passing
- [ ] Environment variables configured
- [ ] Secret key changed from default
- [ ] Debug mode disabled (`debug=False`)
- [ ] Database migrations applied
- [ ] Static files collected/optimized
- [ ] HTTPS/SSL certificate configured
- [ ] Email service configured (SMTP)
- [ ] File upload limits appropriate
- [ ] Security headers configured
- [ ] Backup strategy in place

## 🌐 Deployment Options

### Option 1: PythonAnywhere (Easiest - Free Tier Available)

**Perfect for**: Beginners, small-scale deployments, testing

#### Steps:

1. **Create Account**
   - Sign up at [pythonanywhere.com](https://www.pythonanywhere.com/)
   - Free tier supports 1 web app

2. **Upload Code**
   ```bash
   # On PythonAnywhere bash console
   git clone <your-repo-url>
   cd HackDecouverteStudyApp
   ```

3. **Set Up Virtual Environment**
   ```bash
   mkvirtualenv --python=/usr/bin/python3.10 studyflow-env
   pip install -r requirements.txt
   ```

4. **Configure Web App**
   - Go to Web tab → Add a new web app
   - Choose Manual Configuration → Python 3.10
   - Set source code directory: `/home/yourusername/HackDecouverteStudyApp`
   - Set working directory: `/home/yourusername/HackDecouverteStudyApp`
   - Edit WSGI file:
   ```python
   import sys
   path = '/home/yourusername/HackDecouverteStudyApp'
   if path not in sys.path:
       sys.path.append(path)
   
   from app import app as application
   ```

5. **Configure Static Files**
   - URL: `/static/`
   - Directory: `/home/yourusername/HackDecouverteStudyApp/static`

6. **Initialize Database**
   ```bash
   cd /home/yourusername/HackDecouverteStudyApp
   python init_db.py
   ```

7. **Reload Web App**
   - Click green "Reload" button on Web tab

**Limitations**: 
- Daily CPU quota on free tier
- No custom domain on free tier
- Limited storage (512MB)

---

### Option 2: Heroku (Moderate - Free Tier Discontinued)

**Perfect for**: Medium-scale apps, quick deployment with Git

#### Steps:

1. **Install Heroku CLI**
   ```bash
   # Download from heroku.com/cli
   ```

2. **Create Heroku App**
   ```bash
   heroku login
   heroku create studyflow-app
   ```

3. **Add Procfile**
   ```bash
   # In project root, create Procfile:
   web: gunicorn app:app
   ```

4. **Add gunicorn to requirements.txt**
   ```bash
   echo "gunicorn==21.2.0" >> requirements.txt
   ```

5. **Set Environment Variables**
   ```bash
   heroku config:set SECRET_KEY='your-production-secret-key'
   heroku config:set FLASK_ENV=production
   ```

6. **Deploy**
   ```bash
   git add .
   git commit -m "Prepare for Heroku deployment"
   git push heroku main
   ```

7. **Initialize Database**
   ```bash
   heroku run python init_db.py
   ```

8. **Open App**
   ```bash
   heroku open
   ```

**Note**: Heroku uses ephemeral filesystem - uploaded files are lost on restart. Use AWS S3 or similar for file storage.

---

### Option 3: AWS EC2 (Advanced - Full Control)

**Perfect for**: Large-scale production apps, custom requirements

#### Steps:

1. **Launch EC2 Instance**
   - Choose Ubuntu Server 22.04 LTS
   - Instance type: t2.micro (free tier) or t2.small
   - Configure security group: Allow HTTP (80), HTTPS (443), SSH (22)

2. **Connect via SSH**
   ```bash
   ssh -i your-key.pem ubuntu@your-ec2-ip
   ```

3. **Install Dependencies**
   ```bash
   sudo apt update
   sudo apt install python3-pip python3-venv nginx supervisor -y
   ```

4. **Clone Repository**
   ```bash
   cd /var/www
   sudo git clone <your-repo-url>
   sudo chown -R ubuntu:ubuntu HackDecouverteStudyApp
   cd HackDecouverteStudyApp
   ```

5. **Set Up Virtual Environment**
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   pip install -r requirements.txt
   pip install gunicorn
   ```

6. **Configure Environment Variables**
   ```bash
   sudo nano /var/www/HackDecouverteStudyApp/.env
   ```
   Add:
   ```
   SECRET_KEY=your-production-secret-key
   FLASK_ENV=production
   DATABASE_URL=sqlite:///sessions.db
   ```

7. **Configure Gunicorn**
   ```bash
   sudo nano /etc/supervisor/conf.d/studyflow.conf
   ```
   Add:
   ```ini
   [program:studyflow]
   directory=/var/www/HackDecouverteStudyApp
   command=/var/www/HackDecouverteStudyApp/venv/bin/gunicorn -w 4 -b 127.0.0.1:8000 app:app
   user=ubuntu
   autostart=true
   autorestart=true
   stopasgroup=true
   killasgroup=true
   stderr_logfile=/var/log/studyflow/error.log
   stdout_logfile=/var/log/studyflow/access.log
   ```

8. **Configure Nginx**
   ```bash
   sudo nano /etc/nginx/sites-available/studyflow
   ```
   Add:
   ```nginx
   server {
       listen 80;
       server_name your-domain.com;
   
       location / {
           proxy_pass http://127.0.0.1:8000;
           proxy_set_header Host $host;
           proxy_set_header X-Real-IP $remote_addr;
           proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
       }
   
       location /static {
           alias /var/www/HackDecouverteStudyApp/static;
       }
   
       location /uploads {
           alias /var/www/HackDecouverteStudyApp/uploads;
       }
   }
   ```

9. **Enable Site**
   ```bash
   sudo ln -s /etc/nginx/sites-available/studyflow /etc/nginx/sites-enabled/
   sudo nginx -t
   sudo systemctl restart nginx
   ```

10. **Start Application**
    ```bash
    sudo mkdir -p /var/log/studyflow
    sudo supervisorctl reread
    sudo supervisorctl update
    sudo supervisorctl start studyflow
    ```

11. **Initialize Database**
    ```bash
    cd /var/www/HackDecouverteStudyApp
    source venv/bin/activate
    python init_db.py
    ```

12. **Configure SSL (Optional but Recommended)**
    ```bash
    sudo apt install certbot python3-certbot-nginx
    sudo certbot --nginx -d your-domain.com
    ```

---

### Option 4: DigitalOcean App Platform (Easy - Paid)

**Perfect for**: Quick deployment with managed infrastructure

#### Steps:

1. **Create Account** at [digitalocean.com](https://www.digitalocean.com/)

2. **Create New App**
   - Connect GitHub repository
   - Detect Python app automatically

3. **Configure Build Command**
   ```bash
   pip install -r requirements.txt
   ```

4. **Configure Run Command**
   ```bash
   gunicorn --worker-tmp-dir /dev/shm --workers=2 app:app
   ```

5. **Add Environment Variables**
   - `SECRET_KEY`: Your production secret key
   - `FLASK_ENV`: production

6. **Deploy**
   - Click "Deploy" button
   - App builds and deploys automatically

**Cost**: Starts at $5/month for Basic plan

---

## 🔐 Security Best Practices

### 1. Change Secret Key
```python
# In app.py, use environment variable:
import os
app.secret_key = os.environ.get('SECRET_KEY', 'fallback-dev-key')
```

Generate secure key:
```python
import secrets
print(secrets.token_hex(32))
```

### 2. Disable Debug Mode
```python
if __name__ == '__main__':
    app.run(debug=False)
```

### 3. Use Environment Variables
Create `.env` file (add to `.gitignore`):
```env
SECRET_KEY=your-secret-key-here
DATABASE_URL=sqlite:///sessions.db
MAIL_SERVER=smtp.gmail.com
MAIL_PORT=587
MAIL_USERNAME=your-email@gmail.com
MAIL_PASSWORD=your-app-password
```

Load in `app.py`:
```python
from dotenv import load_dotenv
load_dotenv()
```

### 4. Use HTTPS
- Free SSL: Let's Encrypt (Certbot)
- Managed SSL: Cloudflare, AWS Certificate Manager
- Force HTTPS:
```python
from flask_talisman import Talisman
Talisman(app, force_https=True)
```

### 5. Set Security Headers
```python
@app.after_request
def set_security_headers(response):
    response.headers['X-Content-Type-Options'] = 'nosniff'
    response.headers['X-Frame-Options'] = 'DENY'
    response.headers['X-XSS-Protection'] = '1; mode=block'
    response.headers['Strict-Transport-Security'] = 'max-age=31536000; includeSubDomains'
    return response
```

### 6. Database Backups
```bash
# Automated backup script
#!/bin/bash
BACKUP_DIR="/var/backups/studyflow"
DATE=$(date +%Y%m%d_%H%M%S)
cp /var/www/HackDecouverteStudyApp/sessions.db $BACKUP_DIR/sessions_$DATE.db
# Keep only last 30 days
find $BACKUP_DIR -name "sessions_*.db" -mtime +30 -delete
```

Add to crontab:
```bash
0 3 * * * /path/to/backup-script.sh
```

---

## 📧 Email Configuration

### Gmail Setup
1. Enable 2-Factor Authentication
2. Generate App Password: [myaccount.google.com/apppasswords](https://myaccount.google.com/apppasswords)
3. Add to environment variables:
```env
MAIL_SERVER=smtp.gmail.com
MAIL_PORT=587
MAIL_USE_TLS=True
MAIL_USERNAME=your-email@gmail.com
MAIL_PASSWORD=your-app-password
```

### SendGrid Setup (Recommended for Production)
1. Sign up at [sendgrid.com](https://sendgrid.com/)
2. Create API Key
3. Configure:
```python
app.config['MAIL_SERVER'] = 'smtp.sendgrid.net'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USERNAME'] = 'apikey'
app.config['MAIL_PASSWORD'] = 'your-sendgrid-api-key'
```

---

## 🗄️ Database Migration (SQLite → PostgreSQL)

For production with multiple workers, use PostgreSQL:

### 1. Install PostgreSQL
```bash
sudo apt install postgresql postgresql-contrib
pip install psycopg2-binary
```

### 2. Create Database
```bash
sudo -u postgres psql
CREATE DATABASE studyflow;
CREATE USER studyflow_user WITH PASSWORD 'secure-password';
GRANT ALL PRIVILEGES ON DATABASE studyflow TO studyflow_user;
\q
```

### 3. Update app.py
```python
DATABASE = os.environ.get('DATABASE_URL', 'sqlite:///sessions.db')
# Use SQLAlchemy for PostgreSQL support
```

### 4. Migrate Data
```bash
# Export from SQLite
sqlite3 sessions.db .dump > export.sql
# Import to PostgreSQL (requires conversion)
```

---

## 📊 Monitoring & Logging

### Set Up Logging
```python
import logging
from logging.handlers import RotatingFileHandler

if not app.debug:
    handler = RotatingFileHandler('logs/app.log', maxBytes=10000, backupCount=3)
    handler.setLevel(logging.INFO)
    app.logger.addHandler(handler)
```

### Monitor with Sentry
```bash
pip install sentry-sdk[flask]
```

```python
import sentry_sdk
from sentry_sdk.integrations.flask import FlaskIntegration

sentry_sdk.init(
    dsn="your-sentry-dsn",
    integrations=[FlaskIntegration()]
)
```

---

## 🔄 Continuous Deployment

### GitHub Actions Example
Create `.github/workflows/deploy.yml`:
```yaml
name: Deploy to Production

on:
  push:
    branches: [ main ]

jobs:
  deploy:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v2
      
      - name: Deploy to Server
        uses: appleboy/ssh-action@master
        with:
          host: ${{ secrets.SERVER_IP }}
          username: ubuntu
          key: ${{ secrets.SSH_PRIVATE_KEY }}
          script: |
            cd /var/www/HackDecouverteStudyApp
            git pull origin main
            source venv/bin/activate
            pip install -r requirements.txt
            sudo supervisorctl restart studyflow
```

---

## 🆘 Troubleshooting

### App Won't Start
- Check logs: `sudo supervisorctl tail -f studyflow`
- Verify virtual environment activated
- Check file permissions

### Database Locked
- Stop multiple workers accessing SQLite simultaneously
- Migrate to PostgreSQL for production

### Files Not Uploading
- Check disk space: `df -h`
- Verify upload folder permissions: `chmod 755 uploads/`
- Check MAX_FILE_SIZE limit

### Email Not Sending
- Verify SMTP credentials
- Check firewall rules (allow outbound port 587/465)
- Test with Python script

---

## 📞 Support

For deployment issues:
- Check application logs
- Review Nginx/Apache error logs
- Test with minimal configuration first
- Consult platform-specific documentation

---

**Last Updated**: November 30, 2025

Good luck with your deployment! 🚀
