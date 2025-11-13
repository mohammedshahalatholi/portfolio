# Portfolio Deployment Guide

This guide will help you deploy the portfolio website to various hosting platforms.

## Table of Contents
- [Prerequisites](#prerequisites)
- [General Deployment Steps](#general-deployment-steps)
- [Platform-Specific Guides](#platform-specific-guides)
  - [PythonAnywhere](#pythonanywhere)
  - [Heroku](#heroku)
  - [AWS (EC2/Elastic Beanstalk)](#aws)
  - [DigitalOcean](#digitalocean)
  - [Railway](#railway)
  - [Render](#render)
- [Frontend Deployment](#frontend-deployment)
- [Environment Variables](#environment-variables)
- [Troubleshooting](#troubleshooting)

## Prerequisites

1. **Python 3.8+** installed
2. **Git** installed
3. **Domain name** (optional but recommended)
4. **SSL Certificate** (for HTTPS - most platforms provide this)

## General Deployment Steps

### 1. Prepare Your Code

```bash
# Clone or upload your project
cd portfolio_v1

# Create virtual environment
cd backend
python -m venv venv

# Activate virtual environment
# On Windows:
venv\Scripts\activate
# On Linux/Mac:
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt
```

### 2. Configure Environment Variables

Create a `.env` file in the `backend` directory:

```bash
cd backend
cp env.example .env
```

Edit `.env` with your production settings:

```env
SECRET_KEY=your-very-secret-key-here-generate-with-django-admin
DEBUG=False
ALLOWED_HOSTS=yourdomain.com,www.yourdomain.com
CORS_ALLOWED_ORIGINS=https://yourdomain.com
CORS_ALLOW_ALL_ORIGINS=False
SECURE_SSL_REDIRECT=True
```

**Generate a secret key:**
```python
python -c "from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())"
```

### 3. Run Migrations

```bash
python manage.py migrate
python manage.py createsuperuser
```

### 4. Collect Static Files

```bash
python manage.py collectstatic --noinput
```

### 5. Test Locally

```bash
python manage.py runserver
```

## Platform-Specific Guides

### PythonAnywhere

1. **Create Account**: Sign up at [pythonanywhere.com](https://www.pythonanywhere.com)

2. **Upload Files**:
   - Use the Files tab to upload your project
   - Or use Git: `git clone https://github.com/yourusername/portfolio.git`

3. **Create Web App**:
   - Go to Web tab
   - Click "Add a new web app"
   - Choose "Manual configuration"
   - Select Python 3.8 or higher

4. **Configure WSGI**:
   - Edit the WSGI configuration file
   - Point to your project:
   ```python
   import os
   import sys
   
   path = '/home/yourusername/portfolio_v1/backend'
   if path not in sys.path:
       sys.path.append(path)
   
   os.environ['DJANGO_SETTINGS_MODULE'] = 'portfolio.settings'
   
   from django.core.wsgi import get_wsgi_application
   application = get_wsgi_application()
   ```

5. **Set Environment Variables**:
   - In Web tab, add environment variables:
   ```
   SECRET_KEY=your-secret-key
   DEBUG=False
   ALLOWED_HOSTS=yourusername.pythonanywhere.com
   ```

6. **Static Files**:
   - In Web tab, add static files mapping:
   - URL: `/static/`
   - Directory: `/home/yourusername/portfolio_v1/backend/staticfiles`

7. **Media Files**:
   - URL: `/media/`
   - Directory: `/home/yourusername/portfolio_v1/backend/media`

8. **Reload Web App**

### Heroku

1. **Install Heroku CLI**: [heroku.com/cli](https://devcenter.heroku.com/articles/heroku-cli)

2. **Create Procfile** (in `backend` directory):
   ```
   web: gunicorn portfolio.wsgi --log-file -
   ```

3. **Create runtime.txt** (in `backend` directory):
   ```
   python-3.11.0
   ```

4. **Login and Create App**:
   ```bash
   heroku login
   heroku create your-portfolio-app
   ```

5. **Set Environment Variables**:
   ```bash
   heroku config:set SECRET_KEY=your-secret-key
   heroku config:set DEBUG=False
   heroku config:set ALLOWED_HOSTS=your-portfolio-app.herokuapp.com
   heroku config:set CORS_ALLOWED_ORIGINS=https://your-portfolio-app.herokuapp.com
   ```

6. **Deploy**:
   ```bash
   git init
   git add .
   git commit -m "Initial commit"
   heroku git:remote -a your-portfolio-app
   git push heroku main
   ```

7. **Run Migrations**:
   ```bash
   heroku run python manage.py migrate
   heroku run python manage.py createsuperuser
   ```

### AWS (EC2)

1. **Launch EC2 Instance**:
   - Choose Ubuntu Server
   - Configure security group (open ports 22, 80, 443, 8000)

2. **Connect via SSH**:
   ```bash
   ssh -i your-key.pem ubuntu@your-ec2-ip
   ```

3. **Install Dependencies**:
   ```bash
   sudo apt update
   sudo apt install python3-pip python3-venv nginx git
   ```

4. **Clone and Setup**:
   ```bash
   git clone https://github.com/yourusername/portfolio.git
   cd portfolio/backend
   python3 -m venv venv
   source venv/bin/activate
   pip install -r requirements.txt
   ```

5. **Configure Gunicorn**:
   Create `/etc/systemd/system/portfolio.service`:
   ```ini
   [Unit]
   Description=Portfolio Gunicorn daemon
   After=network.target

   [Service]
   User=ubuntu
   Group=www-data
   WorkingDirectory=/home/ubuntu/portfolio/backend
   ExecStart=/home/ubuntu/portfolio/backend/venv/bin/gunicorn --workers 3 --bind unix:/home/ubuntu/portfolio/backend/portfolio.sock portfolio.wsgi

   [Install]
   WantedBy=multi-user.target
   ```

6. **Configure Nginx**:
   Create `/etc/nginx/sites-available/portfolio`:
   ```nginx
   server {
       listen 80;
       server_name yourdomain.com;

       location /static/ {
           alias /home/ubuntu/portfolio/backend/staticfiles/;
       }

       location /media/ {
           alias /home/ubuntu/portfolio/backend/media/;
       }

       location / {
           include proxy_params;
           proxy_pass http://unix:/home/ubuntu/portfolio/backend/portfolio.sock;
       }
   }
   ```

7. **Enable and Start**:
   ```bash
   sudo ln -s /etc/nginx/sites-available/portfolio /etc/nginx/sites-enabled/
   sudo systemctl start portfolio
   sudo systemctl enable portfolio
   sudo systemctl restart nginx
   ```

8. **Setup SSL with Let's Encrypt**:
   ```bash
   sudo apt install certbot python3-certbot-nginx
   sudo certbot --nginx -d yourdomain.com
   ```

### DigitalOcean

1. **Create Droplet**: Choose Ubuntu, basic plan

2. **Follow AWS EC2 steps** (similar setup)

3. **Or use App Platform**:
   - Connect your GitHub repository
   - Auto-detect Django
   - Set environment variables
   - Deploy automatically

### Railway

1. **Sign up**: [railway.app](https://railway.app)

2. **New Project**: Connect GitHub repository

3. **Add Service**: Choose Django

4. **Set Environment Variables**:
   - SECRET_KEY
   - DEBUG=False
   - ALLOWED_HOSTS=your-app.railway.app

5. **Deploy**: Automatic deployment on push

### Render

1. **Sign up**: [render.com](https://render.com)

2. **New Web Service**: Connect GitHub repository

3. **Configure**:
   - Build Command: `cd backend && pip install -r requirements.txt && python manage.py collectstatic --noinput`
   - Start Command: `cd backend && gunicorn portfolio.wsgi`

4. **Set Environment Variables**

5. **Deploy**

## Frontend Deployment

### Option 1: Serve with Django (Recommended)

1. **Copy frontend files to Django static**:
   ```bash
   # In backend directory
   mkdir -p static
   cp -r ../frontend/* static/
   ```

2. **Update Django URLs** to serve frontend:
   ```python
   # In portfolio/urls.py
   from django.views.generic import TemplateView
   
   urlpatterns = [
       # ... existing patterns
       path('', TemplateView.as_view(template_name='index.html')),
   ]
   ```

### Option 2: Deploy Separately (Netlify, Vercel, etc.)

1. **Update API URL** in `frontend/js/app.js`:
   ```javascript
   const API_BASE_URL = 'https://your-backend-domain.com/api';
   ```

2. **Deploy to Netlify/Vercel**:
   - Connect GitHub repository
   - Build command: (none needed for static files)
   - Publish directory: `frontend`

3. **Update CORS** in backend:
   ```env
   CORS_ALLOWED_ORIGINS=https://your-frontend-domain.com
   ```

## Environment Variables

### Required Variables

- `SECRET_KEY`: Django secret key (generate with Django)
- `DEBUG`: Set to `False` in production
- `ALLOWED_HOSTS`: Your domain(s), comma-separated
- `CORS_ALLOWED_ORIGINS`: Frontend URL(s), comma-separated

### Optional Variables

- `DATABASE_URL`: For PostgreSQL/MySQL (if not using SQLite)
- `EMAIL_*`: For email functionality

## Troubleshooting

### Static Files Not Loading

1. Run `python manage.py collectstatic`
2. Check `STATIC_ROOT` in settings.py
3. Verify static files mapping in web server config

### Media Files Not Loading

1. Check `MEDIA_ROOT` and `MEDIA_URL` in settings.py
2. Verify media files mapping in web server config
3. Ensure proper file permissions

### CORS Errors

1. Update `CORS_ALLOWED_ORIGINS` with your frontend URL
2. Set `CORS_ALLOW_ALL_ORIGINS=False` in production
3. Check browser console for specific CORS errors

### Database Issues

1. Run migrations: `python manage.py migrate`
2. Check database connection settings
3. Verify database user permissions

### 500 Internal Server Error

1. Check server logs
2. Verify `DEBUG=False` and check error pages
3. Verify all environment variables are set
4. Check file permissions

## Security Checklist

- [ ] `DEBUG=False` in production
- [ ] Strong `SECRET_KEY` set
- [ ] `ALLOWED_HOSTS` configured
- [ ] HTTPS enabled (SSL certificate)
- [ ] CORS properly configured
- [ ] Database credentials secure
- [ ] Admin panel protected with strong password
- [ ] Static files served correctly
- [ ] Media files access controlled (if needed)

## Support

For issues or questions, check:
- Django Deployment Checklist: https://docs.djangoproject.com/en/4.2/howto/deployment/checklist/
- Platform-specific documentation
- Project README.md

