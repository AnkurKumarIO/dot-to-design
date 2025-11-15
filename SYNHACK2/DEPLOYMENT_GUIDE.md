# VNIT Hostel Grievance Management System - Deployment Guide

## Overview
This guide covers deploying your full-stack application with:
- **Frontend**: React.js (Port 3000)
- **Backend**: Flask/Python (Port 5002)
- **Database**: Supabase (PostgreSQL)

## Deployment Options

### Option 1: Free Hosting (Recommended for Testing)
- **Frontend**: Vercel or Netlify
- **Backend**: Render or Railway
- **Database**: Supabase (already cloud-hosted)

### Option 2: VPS Hosting (Recommended for Production)
- **Platform**: DigitalOcean, AWS EC2, or Linode
- **Cost**: ~$5-10/month
- **Full control over server**

---

## Option 1: Free Hosting Deployment

### Step 1: Prepare Your Code

#### A. Update Frontend API URL
```bash
# Edit frontend/src/api.js
# Change from:
const API_URL = 'http://localhost:5002/api';

# To (will be updated after backend deployment):
const API_URL = 'https://your-backend-url.onrender.com/api';
```

#### B. Create Production Requirements
```bash
# Create requirements.txt in root directory
pip freeze > requirements.txt
```

#### C. Add Procfile for Backend (Render/Railway)
Create `Procfile` in root:
```
web: gunicorn app:app
```

Install gunicorn:
```bash
pip install gunicorn
pip freeze > requirements.txt
```

### Step 2: Deploy Backend to Render

1. **Sign up at [Render.com](https://render.com)**

2. **Create New Web Service**
   - Click "New +" → "Web Service"
   - Connect your GitHub repository
   - Configure:
     - **Name**: vnit-grievance-backend
     - **Environment**: Python 3
     - **Build Command**: `pip install -r requirements.txt`
     - **Start Command**: `gunicorn app:app`
     - **Plan**: Free

3. **Add Environment Variables**
   Go to Environment tab and add:
   ```
   SUPABASE_URL=your_supabase_url
   SUPABASE_KEY=your_supabase_key
   JWT_SECRET=your_jwt_secret
   PORT=5002
   ```

4. **Deploy**
   - Click "Create Web Service"
   - Wait for deployment (5-10 minutes)
   - Note your backend URL: `https://vnit-grievance-backend.onrender.com`

### Step 3: Deploy Frontend to Vercel

1. **Sign up at [Vercel.com](https://vercel.com)**

2. **Update API URL**
   ```bash
   # Edit frontend/src/api.js
   const API_URL = 'https://vnit-grievance-backend.onrender.com/api';
   ```

3. **Build Frontend Locally (Test)**
   ```bash
   cd frontend
   npm run build
   ```

4. **Deploy to Vercel**
   - Install Vercel CLI:
     ```bash
     npm install -g vercel
     ```
   
   - Deploy:
     ```bash
     cd frontend
     vercel
     ```
   
   - Follow prompts:
     - Project name: vnit-grievance-system
     - Framework: Create React App
     - Build command: `npm run build`
     - Output directory: `build`

5. **Your app will be live at**: `https://vnit-grievance-system.vercel.app`

---

## Option 2: VPS Deployment (Production)

### Step 1: Get a VPS

**Recommended Providers:**
- **DigitalOcean**: $6/month droplet
- **Linode**: $5/month
- **AWS EC2**: Free tier (1 year)

**Specs Needed:**
- 1 GB RAM minimum
- 25 GB SSD
- Ubuntu 22.04 LTS

### Step 2: Initial Server Setup

```bash
# SSH into your server
ssh root@your_server_ip

# Update system
apt update && apt upgrade -y

# Install required software
apt install -y python3 python3-pip python3-venv nginx nodejs npm git

# Install Node.js 18 (LTS)
curl -fsSL https://deb.nodesource.com/setup_18.x | bash -
apt install -y nodejs

# Create application user
adduser vnit
usermod -aG sudo vnit
su - vnit
```

### Step 3: Clone and Setup Application

```bash
# Clone your repository
git clone https://github.com/yourusername/vnit-grievance-system.git
cd vnit-grievance-system

# Setup Backend
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
pip install gunicorn

# Create .env file
nano .env
# Add your environment variables:
# SUPABASE_URL=your_url
# SUPABASE_KEY=your_key
# JWT_SECRET=your_secret
# PORT=5002

# Setup Frontend
cd frontend
npm install
npm run build
cd ..
```

### Step 4: Setup Systemd Service for Backend

```bash
# Create service file
sudo nano /etc/systemd/system/vnit-backend.service
```

Add this content:
```ini
[Unit]
Description=VNIT Grievance Backend
After=network.target

[Service]
User=vnit
WorkingDirectory=/home/vnit/vnit-grievance-system
Environment="PATH=/home/vnit/vnit-grievance-system/venv/bin"
ExecStart=/home/vnit/vnit-grievance-system/venv/bin/gunicorn --workers 3 --bind 0.0.0.0:5002 app:app

[Install]
WantedBy=multi-user.target
```

```bash
# Enable and start service
sudo systemctl daemon-reload
sudo systemctl enable vnit-backend
sudo systemctl start vnit-backend
sudo systemctl status vnit-backend
```

### Step 5: Setup Nginx

```bash
# Create Nginx configuration
sudo nano /etc/nginx/sites-available/vnit-grievance
```

Add this content:
```nginx
server {
    listen 80;
    server_name your_domain.com;  # or your_server_ip

    # Frontend
    location / {
        root /home/vnit/vnit-grievance-system/frontend/build;
        try_files $uri $uri/ /index.html;
    }

    # Backend API
    location /api {
        proxy_pass http://localhost:5002;
        proxy_http_version 1.1;
        proxy_set_header Upgrade $http_upgrade;
        proxy_set_header Connection 'upgrade';
        proxy_set_header Host $host;
        proxy_cache_bypass $http_upgrade;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
    }
}
```

```bash
# Enable site
sudo ln -s /etc/nginx/sites-available/vnit-grievance /etc/nginx/sites-enabled/
sudo nginx -t
sudo systemctl restart nginx
```

### Step 6: Setup SSL (HTTPS) with Let's Encrypt

```bash
# Install Certbot
sudo apt install -y certbot python3-certbot-nginx

# Get SSL certificate
sudo certbot --nginx -d your_domain.com

# Auto-renewal is set up automatically
```

### Step 7: Setup Firewall

```bash
# Configure UFW
sudo ufw allow OpenSSH
sudo ufw allow 'Nginx Full'
sudo ufw enable
```

---

## Post-Deployment Steps

### 1. Update Frontend API URL

If using same domain for frontend and backend:
```javascript
// frontend/src/api.js
const API_URL = '/api';  // Relative URL
```

If using different domains:
```javascript
const API_URL = 'https://api.yourdomain.com/api';
```

### 2. Test the Application

```bash
# Test backend
curl https://your_domain.com/api/

# Test frontend
# Open browser: https://your_domain.com
```

### 3. Create Initial Admin Users

```bash
# SSH into server
ssh vnit@your_server_ip

# Activate venv
cd vnit-grievance-system
source venv/bin/activate

# Run Python script to create users
python3 create_admin_users.py
```

### 4. Setup Database Backups

```bash
# Create backup script
nano ~/backup_db.sh
```

Add:
```bash
#!/bin/bash
# Supabase handles backups automatically
# But you can export data periodically
DATE=$(date +%Y%m%d_%H%M%S)
curl "YOUR_SUPABASE_URL/rest/v1/complaints?select=*" \
  -H "apikey: YOUR_KEY" > ~/backups/complaints_$DATE.json
```

```bash
chmod +x ~/backup_db.sh

# Add to crontab (daily at 2 AM)
crontab -e
# Add: 0 2 * * * /home/vnit/backup_db.sh
```

---

## Monitoring and Maintenance

### Check Backend Logs
```bash
sudo journalctl -u vnit-backend -f
```

### Check Nginx Logs
```bash
sudo tail -f /var/log/nginx/access.log
sudo tail -f /var/log/nginx/error.log
```

### Restart Services
```bash
# Restart backend
sudo systemctl restart vnit-backend

# Restart Nginx
sudo systemctl restart nginx
```

### Update Application
```bash
cd ~/vnit-grievance-system
git pull origin main

# Update backend
source venv/bin/activate
pip install -r requirements.txt
sudo systemctl restart vnit-backend

# Update frontend
cd frontend
npm install
npm run build
cd ..

# Restart Nginx
sudo systemctl restart nginx
```

---

## Troubleshooting

### Backend Not Starting
```bash
# Check logs
sudo journalctl -u vnit-backend -n 50

# Check if port is in use
sudo lsof -i :5002

# Test manually
cd ~/vnit-grievance-system
source venv/bin/activate
python app.py
```

### Frontend Not Loading
```bash
# Check Nginx config
sudo nginx -t

# Check if build exists
ls -la ~/vnit-grievance-system/frontend/build

# Rebuild frontend
cd ~/vnit-grievance-system/frontend
npm run build
```

### Database Connection Issues
```bash
# Test Supabase connection
cd ~/vnit-grievance-system
source venv/bin/activate
python -c "from app.database import get_supabase_client; print(get_supabase_client())"
```

### CORS Issues
```bash
# Check app.py CORS configuration
# Ensure your domain is in the allowed origins
```

---

## Performance Optimization

### 1. Enable Gzip Compression
Add to Nginx config:
```nginx
gzip on;
gzip_types text/plain text/css application/json application/javascript;
```

### 2. Add Caching Headers
```nginx
location /static {
    expires 1y;
    add_header Cache-Control "public, immutable";
}
```

### 3. Increase Gunicorn Workers
```bash
# Edit service file
sudo nano /etc/systemd/system/vnit-backend.service

# Change workers based on CPU cores: (2 x cores) + 1
ExecStart=... --workers 5 ...
```

---

## Security Checklist

- [ ] Change default JWT_SECRET
- [ ] Enable HTTPS (SSL certificate)
- [ ] Setup firewall (UFW)
- [ ] Disable root SSH login
- [ ] Use strong passwords
- [ ] Keep system updated
- [ ] Setup fail2ban for SSH protection
- [ ] Regular database backups
- [ ] Monitor logs regularly
- [ ] Use environment variables for secrets

---

## Cost Estimate

### Free Tier (Testing)
- Frontend (Vercel): Free
- Backend (Render): Free (sleeps after 15 min inactivity)
- Database (Supabase): Free (500 MB, 2 GB bandwidth)
- **Total**: $0/month

### Production (VPS)
- VPS (DigitalOcean): $6/month
- Domain name: $10-15/year
- Supabase Pro (optional): $25/month
- **Total**: ~$6-31/month

---

## Quick Start Commands

### Deploy to Render + Vercel (Fastest)
```bash
# 1. Push code to GitHub
git add .
git commit -m "Ready for deployment"
git push origin main

# 2. Deploy backend on Render.com (via web interface)
# 3. Update frontend API URL
# 4. Deploy frontend on Vercel
cd frontend
vercel --prod
```

### Deploy to VPS (Full Control)
```bash
# Run this script on your VPS
curl -O https://raw.githubusercontent.com/yourusername/vnit-grievance-system/main/deploy.sh
chmod +x deploy.sh
./deploy.sh
```

---

## Support

For deployment issues:
1. Check logs first
2. Review this guide
3. Check Supabase dashboard for database issues
4. Test locally to isolate the problem

Good luck with your deployment! 🚀
