# 🚀 Quick Start Guide - Run on Localhost

## Method 1: Using Batch Files (Windows - Easiest)

### Step 1: Start Backend
1. Double-click `start_backend.bat`
2. Wait for dependencies to install and migrations to run
3. Backend will start on **http://127.0.0.1:8000**

**First time only:** Create an admin user:
- Open a new terminal
- Run: `cd backend` then `python manage.py createsuperuser`
- Follow prompts to create username, email, and password

### Step 2: Start Frontend
1. Open a **NEW terminal window** (keep backend running!)
2. Double-click `start_frontend.bat`
3. Frontend will start on **http://localhost:3001**

### Step 3: Add Content
1. Go to **http://127.0.0.1:8000/admin**
2. Login with your superuser credentials
3. Add your portfolio content (About, Projects, Skills, etc.)
4. **Important:** Check the "enabled" checkbox for items you want to display
5. Go to **http://localhost:3001** to see your portfolio!

---

## Method 2: Manual Setup (All Platforms)

### Backend Setup

```bash
# 1. Navigate to backend
cd backend

# 2. Install dependencies
pip install -r requirements.txt

# 3. Create and apply migrations
python manage.py makemigrations
python manage.py migrate

# 4. Create admin user (first time only)
python manage.py createsuperuser

# 5. Start server
python manage.py runserver
```

Backend runs on: **http://127.0.0.1:8000**

### Frontend Setup

Open a **NEW terminal** (keep backend running):

```bash
# 1. Navigate to frontend
cd frontend

# 2. Start HTTP server
python -m http.server 3001
```

Frontend runs on: **http://localhost:3001**

---

## What You'll See

### Backend URLs:
- **Admin Panel**: http://127.0.0.1:8000/admin
- **API Root**: http://127.0.0.1:8000/api/
- **About API**: http://127.0.0.1:8000/api/about/
- **Projects API**: http://127.0.0.1:8000/api/projects/
- (and more...)

### Frontend:
- **Portfolio Website**: http://localhost:3001

---

## Adding Your First Content

1. **Login to Admin**: http://127.0.0.1:8000/admin
2. **Add About Section**:
   - Click "About" → "Add About"
   - Enter your name and bio
   - Upload a profile image (optional)
   - Check "Enabled" checkbox
   - Click "Save"

3. **Add a Project**:
   - Click "Projects" → "Add Project"
   - Enter title, description, technologies
   - Add project link and image (optional)
   - Check "Enabled" checkbox
   - Click "Save"

4. **Add Skills, Experience, etc.**:
   - Follow the same process for other sections
   - Remember to enable items you want to display

5. **View Your Portfolio**:
   - Go to http://localhost:3001
   - Refresh the page to see your content!

---

## Troubleshooting

### "Module not found" errors
```bash
pip install -r requirements.txt
```

### "Port already in use"
- Backend: Change port with `python manage.py runserver 8001`
- Frontend: Change port with `python -m http.server 3002`
- Update `API_BASE_URL` in `frontend/js/app.js` if backend port changed

### CORS errors
- Make sure backend is running
- Check that `CORS_ALLOW_ALL_ORIGINS = True` in `backend/portfolio/settings.py`

### No content showing
- Make sure items are "enabled" in admin panel
- Check browser console for errors
- Verify backend is running and accessible

### Images not loading
- Upload images through admin panel
- Check that media folder exists: `backend/media/`
- Make sure Django is serving media files in development

---

## Next Steps

1. ✅ Customize colors and styles in `frontend/css/style.css`
2. ✅ Add more sections if needed
3. ✅ Configure for production deployment
4. ✅ Set up proper media file serving
5. ✅ Add authentication for admin panel

---

## Need Help?

- Check `SETUP.md` for detailed setup instructions
- Check `README.md` for full documentation
- Check browser console for errors
- Check Django server logs for backend errors

