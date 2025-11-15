# Backend Files and Folders - Deployment Checklist

## 📦 Essential Backend Files (MUST DEPLOY)

### Core Application Files
```
app.py                          # Main Flask application entry point
config.py                       # Configuration settings
requirements.txt                # Python dependencies
.env                           # Environment variables (create new for production)
```

### App Directory (Complete Folder)
```
app/
├── __init__.py                # Package initialization
├── auth_middleware.py         # JWT authentication middleware
├── database.py                # Supabase database connection
└── routes/                    # API endpoints
    ├── auth.py               # Authentication routes (/api/auth/*)
    ├── complaints.py         # Complaint routes (/api/complaints/*)
    ├── admin.py              # Admin routes (/api/admin/*)
    └── worker.py             # Worker routes (/api/worker/*)
```

---

## 📋 Complete Backend Structure

### ✅ Required for Deployment

#### 1. **Main Application**
- `app.py` - Flask app entry point
- `config.py` - App configuration
- `requirements.txt` - Python packages

#### 2. **App Package** (entire folder)
```
app/
├── __init__.py
├── auth_middleware.py
├── database.py
└── routes/
    ├── auth.py
    ├── complaints.py
    ├── admin.py
    └── worker.py
```

#### 3. **Environment Configuration**
- `.env` - Environment variables (recreate for production with your values)

#### 4. **Optional but Recommended**
- `Procfile` - For Render/Heroku deployment
- `.gitignore` - To exclude sensitive files
- `README.md` - Documentation

---

## ❌ NOT Needed for Deployment

### Test Files (Don't Deploy)
```
test_*.py                      # All test files
check_*.py                     # Database check scripts
debug_*.py                     # Debug scripts
verify_*.py                    # Verification scripts
view_database.py               # Database viewer
create_test_users.py           # Test data creation
setup_admins.py                # Admin setup script
fix_roles.py                   # Database fix script
quick_test.py                  # Quick test script
run_worker_migration.py        # Migration script
```

### Documentation Files (Don't Deploy)
```
*.md files                     # All markdown documentation
*.txt files (except requirements.txt)
```

### SQL Files (Don't Deploy - Already in Supabase)
```
database_*.sql                 # Database schemas and migrations
*.sql                         # All SQL files
```

### Development Folders (Don't Deploy)
```
venv/                         # Virtual environment
.vscode/                      # VS Code settings
.kiro/                        # Kiro IDE settings
__pycache__/                  # Python cache
*.pyc                         # Compiled Python files
.DS_Store                     # Mac system files
```

### Frontend (Separate Deployment)
```
frontend/                     # Deploy separately to Vercel/Netlify
```

---

## 📦 Minimal Backend Deployment Package

Here's exactly what you need to deploy:

```
your-backend/
├── app/
│   ├── __init__.py
│   ├── auth_middleware.py
│   ├── database.py
│   └── routes/
│       ├── auth.py
│       ├── complaints.py
│       ├── admin.py
│       └── worker.py
├── app.py
├── config.py
├── requirements.txt
├── .env (create new with production values)
├── Procfile (for Render/Heroku)
└── .gitignore
```

**Total Size**: ~50 KB (without dependencies)

---

## 🔧 Creating Deployment Package

### Option 1: Using Git (Recommended)

```bash
# Create .gitignore if not exists
cat > .gitignore << EOF
venv/
__pycache__/
*.pyc
.env
.DS_Store
*.md
test_*.py
check_*.py
debug_*.py
*.sql
frontend/
.vscode/
.kiro/
EOF

# Commit only backend files
git add app/ app.py config.py requirements.txt Procfile
git commit -m "Backend deployment files"
git push origin main
```

### Option 2: Manual ZIP Package

```bash
# Create deployment folder
mkdir backend-deploy
cd backend-deploy

# Copy essential files
cp -r ../app .
cp ../app.py .
cp ../config.py .
cp ../requirements.txt .

# Create new .env (don't copy the old one)
cat > .env << EOF
SUPABASE_URL=your_production_url
SUPABASE_KEY=your_production_key
JWT_SECRET=your_production_secret
PORT=5002
EOF

# Create Procfile
echo "web: gunicorn app:app" > Procfile

# Zip it
cd ..
zip -r backend-deploy.zip backend-deploy/
```

---

## 📝 Environment Variables (.env)

Create a new `.env` file for production:

```env
# Supabase Configuration
SUPABASE_URL=https://your-project.supabase.co
SUPABASE_KEY=your-anon-key

# JWT Configuration
JWT_SECRET=your-super-secret-key-change-this

# Server Configuration
PORT=5002
FLASK_ENV=production
```

**⚠️ IMPORTANT**: Never commit `.env` to Git!

---

## 🚀 Deployment Commands

### For Render.com
```bash
# Build Command
pip install -r requirements.txt

# Start Command
gunicorn app:app
```

### For Railway.app
```bash
# Build Command
pip install -r requirements.txt

# Start Command
gunicorn app:app --bind 0.0.0.0:$PORT
```

### For VPS (Manual)
```bash
# Install dependencies
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
pip install gunicorn

# Run with gunicorn
gunicorn --workers 3 --bind 0.0.0.0:5002 app:app
```

---

## 📊 File Size Reference

| Component | Size |
|-----------|------|
| app/ folder | ~30 KB |
| app.py | ~2 KB |
| config.py | ~1 KB |
| requirements.txt | ~1 KB |
| .env | <1 KB |
| **Total** | **~35 KB** |

Dependencies (installed on server): ~50 MB

---

## ✅ Pre-Deployment Checklist

- [ ] `app/` folder with all route files
- [ ] `app.py` main file
- [ ] `config.py` configuration
- [ ] `requirements.txt` with all dependencies
- [ ] `.env` with production values
- [ ] `Procfile` for platform deployment
- [ ] `.gitignore` to exclude sensitive files
- [ ] Test locally: `python app.py`
- [ ] Verify all routes work
- [ ] Update CORS settings in `app.py`

---

## 🔍 Verify Your Backend Package

Run this command to see what will be deployed:

```bash
# List only backend files
ls -lh app.py config.py requirements.txt
ls -lh app/
ls -lh app/routes/
```

Expected output:
```
app.py
config.py
requirements.txt
app/__init__.py
app/auth_middleware.py
app/database.py
app/routes/auth.py
app/routes/complaints.py
app/routes/admin.py
app/routes/worker.py
```

---

## 🎯 Quick Deploy Script

Save this as `prepare_backend.sh`:

```bash
#!/bin/bash
echo "Preparing backend for deployment..."

# Create deployment directory
mkdir -p backend-deploy
cd backend-deploy

# Copy essential files
cp -r ../app .
cp ../app.py .
cp ../config.py .
cp ../requirements.txt .

# Create Procfile
echo "web: gunicorn app:app" > Procfile

# Create .gitignore
cat > .gitignore << EOF
venv/
__pycache__/
*.pyc
.env
.DS_Store
EOF

echo "✅ Backend deployment package ready in backend-deploy/"
echo "⚠️  Don't forget to create .env file with production values!"
```

Run it:
```bash
chmod +x prepare_backend.sh
./prepare_backend.sh
```

---

## 📞 Need Help?

If you're unsure about any file:
1. Check if it's in the "Essential" list above
2. If it starts with `test_`, `check_`, `debug_` - don't deploy it
3. If it ends with `.md` or `.sql` - don't deploy it
4. When in doubt, only deploy the files listed in "Minimal Backend Deployment Package"
