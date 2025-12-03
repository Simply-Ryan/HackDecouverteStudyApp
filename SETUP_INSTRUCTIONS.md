# 🚀 StudyFlow Setup Instructions

Welcome to StudyFlow! This guide will help you set up the application after downloading it from GitHub.

## 📋 Prerequisites

Before running the setup scripts, make sure you have:

- **Python 3.8 or higher** installed ([Download here](https://www.python.org/downloads/))
  - ⚠️ **IMPORTANT**: During installation, check **"Add Python to PATH"**
- **Internet connection** for downloading dependencies
- **Git** (if cloning from GitHub)

---

## 🪟 Windows Setup

### Method 1: Using PowerShell (Recommended)

1. **Download/Clone StudyFlow**
   ```powershell
   git clone https://github.com/your-username/StudyFlow.git
   cd StudyFlow
   ```

2. **Run the Setup Script**
   ```powershell
   PowerShell -ExecutionPolicy Bypass -File .\setup.ps1
   ```

3. **Wait for completion** (takes 2-5 minutes)

4. **Start the application**
   ```powershell
   .\venv\Scripts\Activate.ps1
   python app.py
   ```
   
   If activation fails due to execution policy:
   ```powershell
   PowerShell -ExecutionPolicy Bypass -File .\venv\Scripts\Activate.ps1
   python app.py
   ```

5. **Open your browser** to `http://localhost:5000`

### Method 2: Right-Click Run (May require permissions)

1. Right-click `setup.ps1`
2. Select **"Run with PowerShell"**
3. If you see a security warning, select **"Open"** or **"Run anyway"**
4. Follow on-screen instructions

### ⚠️ Common Windows Issues

**"Cannot be loaded because running scripts is disabled"**
- Solution: Use Method 1 with `-ExecutionPolicy Bypass`
- Or run: `Set-ExecutionPolicy -Scope CurrentUser -ExecutionPolicy RemoteSigned`

**"python is not recognized"**
- Solution: Python not in PATH. Reinstall Python and check "Add to PATH"
- Or find Python path and use full path: `C:\Users\YourName\AppData\Local\Programs\Python\Python312\python.exe`

---

## 🐧 Linux / 🍎 macOS Setup

### Using Terminal (Required)

1. **Download/Clone StudyFlow**
   ```bash
   git clone https://github.com/your-username/StudyFlow.git
   cd StudyFlow
   ```

2. **Make setup script executable**
   ```bash
   chmod +x setup.sh
   ```

3. **Run the setup script**
   ```bash
   ./setup.sh
   ```

4. **Wait for completion** (takes 2-5 minutes)

5. **Start the application**
   ```bash
   source venv/bin/activate
   python app.py
   ```

6. **Open your browser** to `http://localhost:5000`

### ⚠️ Common Linux/macOS Issues

**"python3: command not found"**
- Install Python 3: 
  - Ubuntu/Debian: `sudo apt install python3 python3-pip python3-venv`
  - macOS: `brew install python3` (requires Homebrew)

**"Permission denied" when running ./setup.sh**
- Solution: Make sure you ran `chmod +x setup.sh`

---

## 📝 What the Setup Script Does

The automated setup script performs these steps:

1. ✅ **Checks Python installation** (version 3.8+)
2. ✅ **Creates virtual environment** (`venv/` folder)
3. ✅ **Installs all dependencies** from `requirements.txt`
4. ✅ **Generates secure .env file** with random secret key
5. ✅ **Initializes database** from `schema.sql`
6. ✅ **Creates required folders** (`uploads/`, `flask_session/`, etc.)

---

## 🎯 After Setup

### Configure Optional Features (Optional)

Edit the `.env` file to enable:

**AI Assistant** (ChatGPT integration):
```env
AI_ENABLED=true
OPENAI_API_KEY=your-api-key-here
```

**Email Notifications**:
```env
MAIL_USERNAME=your-email@gmail.com
MAIL_PASSWORD=your-app-password
```

### Start Development

```bash
# Activate virtual environment
# Windows:
.\venv\Scripts\Activate.ps1

# Linux/macOS:
source venv/bin/activate

# Run the application
python app.py

# Open browser to http://localhost:5000
```

### Create Your First Account

1. Go to `http://localhost:5000`
2. Click **"Register"**
3. Fill in your details
4. Start creating study sessions!

---

## 🔧 Manual Setup (If scripts fail)

If the automated scripts don't work, follow these manual steps:

### Windows (PowerShell)
```powershell
# 1. Create virtual environment
python -m venv venv

# 2. Activate it
.\venv\Scripts\Activate.ps1

# 3. Install dependencies
pip install -r requirements.txt

# 4. Initialize database
python init_db.py

# 5. Create .env file manually (copy from .env.example if exists)
# Add: SECRET_KEY=your-random-secret-key-here

# 6. Run application
python app.py
```

### Linux/macOS (Terminal)
```bash
# 1. Create virtual environment
python3 -m venv venv

# 2. Activate it
source venv/bin/activate

# 3. Install dependencies
pip install -r requirements.txt

# 4. Initialize database
python init_db.py

# 5. Create .env file manually
# Add: SECRET_KEY=your-random-secret-key-here

# 6. Run application
python app.py
```

---

## 📚 Additional Resources

- **README.md** - Full application documentation
- **TROUBLESHOOTING.md** - Common issues and solutions
- **QUICKSTART.md** - Quick reference guide
- **API.md** - API documentation

---

## 💬 Getting Help

If you encounter issues:

1. Check **TROUBLESHOOTING.md** for common solutions
2. Verify Python version: `python --version` (should be 3.8+)
3. Check all files are present: `requirements.txt`, `schema.sql`, `app.py`
4. Try manual setup steps above
5. Open an issue on GitHub with:
   - Operating system and version
   - Python version
   - Error message (full text)
   - Steps you tried

---

## ✅ Success Checklist

After running setup, you should have:

- [ ] `venv/` folder created
- [ ] `.env` file with SECRET_KEY
- [ ] `sessions.db` database file
- [ ] All packages installed (check with `pip list`)
- [ ] Application runs without errors
- [ ] Can access `http://localhost:5000` in browser

---

**Happy studying with StudyFlow! 🎓📚**
