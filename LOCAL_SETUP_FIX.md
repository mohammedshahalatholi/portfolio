# Local Setup Fix

If you're getting errors when trying to run locally, follow these steps:

## Issue: ModuleNotFoundError: No module named 'decouple'

This happens because the new deployment dependencies need to be installed.

### Quick Fix (Windows):

1. **Open terminal in `backend` directory**
2. **Run setup script:**
   ```bash
   setup_local.bat
   ```
   This will:
   - Install all dependencies
   - Create `.env` file for local development
   - Run migrations

3. **Start the server:**
   ```bash
   python manage.py runserver
   ```

### Quick Fix (Linux/Mac):

1. **Open terminal in `backend` directory**
2. **Run setup script:**
   ```bash
   chmod +x setup_local.sh
   ./setup_local.sh
   ```
   This will:
   - Install all dependencies
   - Create `.env` file for local development
   - Run migrations

3. **Start the server:**
   ```bash
   python manage.py runserver
   ```

### Manual Fix:

1. **Install dependencies:**
   ```bash
   cd backend
   pip install -r requirements.txt
   ```

2. **Create `.env` file in `backend` directory:**
   ```env
   SECRET_KEY=django-insecure-change-this-in-production
   DEBUG=True
   ALLOWED_HOSTS=localhost,127.0.0.1,*
   CORS_ALLOWED_ORIGINS=http://localhost:3000,http://localhost:3001,http://127.0.0.1:3000,http://127.0.0.1:3001
   CORS_ALLOW_ALL_ORIGINS=True
   SECURE_SSL_REDIRECT=False
   ```

3. **Run migrations:**
   ```bash
   python manage.py migrate
   ```

4. **Start the server:**
   ```bash
   python manage.py runserver
   ```

## What Changed?

The project was updated for deployment readiness, which added:
- `python-decouple` for environment variables
- `whitenoise` for static file serving
- `gunicorn` for production server

These are now required dependencies, so they need to be installed.

## After Setup

Once setup is complete, everything should work as before:
- Backend: `http://127.0.0.1:8000`
- Admin: `http://127.0.0.1:8000/admin`
- Frontend: `http://localhost:3001`

The `.env` file is automatically ignored by git (it's in `.gitignore`), so your local settings won't be committed.

