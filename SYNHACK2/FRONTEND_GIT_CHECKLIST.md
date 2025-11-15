# Frontend Git Repository Checklist

## ✅ **Files to ADD to Git**

### **Source Code (Required)**
```
frontend/
├── src/                          # All React source code
│   ├── pages/                    # All page components
│   │   ├── AdminDashboard.js
│   │   ├── Home.js
│   │   ├── Home.css
│   │   ├── Login.js
│   │   ├── Profile.js
│   │   ├── Register.js
│   │   ├── StudentDashboard.js
│   │   ├── WorkerDashboard.js
│   │   └── WorkerDashboard.css
│   ├── api.js                    # API client
│   ├── App.js                    # Main app component
│   ├── App.css                   # Global styles
│   ├── index.js                  # Entry point
│   └── index.css                 # Base styles
├── public/
│   ├── index.html                # HTML template
│   ├── vnit-logo.png             # Logo image
│   └── *.jpg                     # Hostel images (if needed)
├── package.json                  # Dependencies
├── package-lock.json             # Lock file
└── README.md                     # Documentation (optional)
```

### **Configuration Files (Required)**
```
frontend/
├── package.json                  # ✅ MUST include
├── package-lock.json             # ✅ MUST include
└── .gitignore                    # ✅ MUST create (see below)
```

---

## ❌ **Files to EXCLUDE from Git**

### **Create `.gitignore` file:**
```gitignore
# Dependencies
node_modules/

# Production build
build/
dist/

# Environment variables
.env
.env.local
.env.development.local
.env.test.local
.env.production.local

# IDE
.vscode/
.idea/
*.swp
*.swo
*~

# OS
.DS_Store
Thumbs.db
Desktop.ini

# Logs
npm-debug.log*
yarn-debug.log*
yarn-error.log*
lerna-debug.log*

# Testing
coverage/
.nyc_output/

# Misc
.eslintcache
.cache/
```

---

## 📋 **Git Commands to Add Frontend**

### **1. Create .gitignore (if not exists)**
```bash
cd frontend
cat > .gitignore << 'EOF'
node_modules/
build/
.env
.env.local
.DS_Store
npm-debug.log*
EOF
```

### **2. Add Source Files**
```bash
# From project root
git add frontend/src/
git add frontend/public/index.html
git add frontend/public/vnit-logo.png
git add frontend/public/*.jpg
git add frontend/package.json
git add frontend/package-lock.json
git add frontend/.gitignore
```

### **3. Commit**
```bash
git commit -m "Add frontend source code"
```

---

## 📊 **Size Comparison**

| What | Size | Add to Git? |
|------|------|-------------|
| **Source code** | ~500 KB | ✅ Yes |
| **node_modules** | ~200 MB | ❌ No |
| **build/** | ~2-5 MB | ❌ No (auto-generated) |
| **Images** | ~2-5 MB | ✅ Yes (if needed) |

---

## 🔍 **Verify Before Committing**

### **Check what will be committed:**
```bash
cd frontend
git status
```

### **Should see:**
```
✅ src/
✅ public/index.html
✅ public/*.png, *.jpg
✅ package.json
✅ package-lock.json
✅ .gitignore
```

### **Should NOT see:**
```
❌ node_modules/
❌ build/
❌ .env files
```

---

## 🚀 **Deployment Flow**

### **What You Commit:**
```
Source code (~500 KB)
├── src/
├── public/
├── package.json
└── package-lock.json
```

### **What Platform Does:**
```
1. Reads package.json
2. Runs: npm install (creates node_modules)
3. Runs: npm run build (creates build/)
4. Serves: build/ to users
```

---

## ⚠️ **Important Notes**

1. **Never commit `node_modules/`** - It's huge (~200 MB) and auto-generated
2. **Never commit `build/`** - It's auto-generated during deployment
3. **Never commit `.env` files** - They contain secrets
4. **Always commit `package-lock.json`** - Ensures consistent dependencies
5. **Update API URL before deploying** - Change from localhost to production

---

## 🎯 **Quick Checklist**

- [ ] Created `.gitignore` file
- [ ] Added all `src/` files
- [ ] Added `public/index.html`
- [ ] Added `package.json` and `package-lock.json`
- [ ] Verified `node_modules/` is NOT staged
- [ ] Verified `build/` is NOT staged
- [ ] Updated API URL in `src/api.js` (for production)
- [ ] Committed changes

---

## 📝 **Example Git Workflow**

```bash
# 1. Navigate to project root
cd /path/to/your/project

# 2. Create .gitignore if needed
cat > frontend/.gitignore << 'EOF'
node_modules/
build/
.env
.DS_Store
EOF

# 3. Add frontend files
git add frontend/src/
git add frontend/public/index.html
git add frontend/public/*.png
git add frontend/public/*.jpg
git add frontend/package.json
git add frontend/package-lock.json
git add frontend/.gitignore

# 4. Check what's staged
git status

# 5. Commit
git commit -m "Add frontend application"

# 6. Push to remote
git push origin main
```

---

## 🔧 **Before Deployment**

### **Update API URL:**
```javascript
// frontend/src/api.js
// Change from:
const API_URL = 'http://localhost:5002/api';

// To production:
const API_URL = 'https://your-backend.onrender.com/api';
// OR relative:
const API_URL = '/api';
```

---

## ✨ **Summary**

**Add to Git:**
- ✅ All files in `src/`
- ✅ `public/index.html` and images
- ✅ `package.json` and `package-lock.json`
- ✅ `.gitignore`

**Exclude from Git:**
- ❌ `node_modules/` (200+ MB)
- ❌ `build/` (auto-generated)
- ❌ `.env` files (secrets)
- ❌ IDE/OS files

**Total to commit: ~500 KB of source code** 🎉
