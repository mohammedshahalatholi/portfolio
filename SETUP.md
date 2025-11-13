# Quick Start Guide - Run Portfolio on Localhost

## Step 1: Backend Setup (Django)

### 1.1 Install Dependencies
```bash
cd backend
pip install -r requirements.txt
```

### 1.2 Create Database and Migrations
```bash
python manage.py makemigrations
python manage.py migrate
```

### 1.3 Create Admin User
```bash
python manage.py createsuperuser
```
Follow the prompts to create a username, email, and password.

### 1.4 Run Django Server
```bash
python manage.py runserver
```

The backend will run on: **http://127.0.0.1:8000**

You can access:
- Admin Panel: **http://127.0.0.1:8000/admin**
- API: **http://127.0.0.1:8000/api/**

---

## Step 2: Frontend Setup

### Option A: Using Python HTTP Server (Recommended)

1. Open a **new terminal window** (keep Django server running in the first terminal)
2. Navigate to frontend directory:
```bash
cd frontend
```

3. Start HTTP server:
```bash
# Python 3
python -m http.server 3001

# OR if python doesn't work, try:
python3 -m http.server 3001
```

4. Open your browser and go to: **http://localhost:3001**

### Option B: Using VS Code Live Server

1. Install "Live Server" extension in VS Code
2. Right-click on `frontend/index.html`
3. Select "Open with Live Server"

### Option C: Direct File Open (May have CORS issues)

1. Simply double-click `frontend/index.html` to open in browser
2. Note: This may not work if backend CORS is not configured for file:// protocol

---

## Step 3: Add Content via Admin Panel

1. Go to **http://127.0.0.1:8000/admin**
2. Login with your superuser credentials
3. Add content:
   - **About**: Add your name, bio, and upload a profile image
   - **Experiences**: Add work experiences
   - **Projects**: Add projects with images and links
   - **Skills**: Add skills with categories and proficiency levels
   - **Education**: Add educational background
   - **Contact Info**: Add your email, phone, location
   - **Social Links**: Add social media links (Facebook, LinkedIn, GitHub, etc.)
   - **Awards**: Add awards and achievements
   - **Hobbies**: Add hobbies and interests

4. Make sure to **check the "enabled" checkbox** for items you want to display on the frontend

5. Refresh the frontend page to see your content!

---

## Troubleshooting

### Backend Issues

**Issue: `django-admin: command not found`**
- Solution: Make sure Django is installed: `pip install -r requirements.txt`

**Issue: `No module named 'rest_framework'`**
- Solution: Install dependencies: `pip install -r requirements.txt`

**Issue: Port 8000 already in use**
- Solution: Use a different port: `python manage.py runserver 8001`
- Then update `API_BASE_URL` in `frontend/js/app.js` to match the new port

### Frontend Issues

**Issue: CORS errors in browser console**
- Solution: Make sure CORS is enabled in `backend/portfolio/settings.py` (it should be enabled by default)
- Check that `CORS_ALLOW_ALL_ORIGINS = True` is set in settings.py

**Issue: API calls failing**
- Solution: Check that backend is running on `http://127.0.0.1:8000`
- Check browser console for errors
- Verify `API_BASE_URL` in `frontend/js/app.js` matches your backend URL

**Issue: Images not loading**
- Solution: Make sure media files are configured correctly
- Check that `MEDIA_URL` and `MEDIA_ROOT` are set in settings.py
- Upload images through admin panel

### Port Conflicts

If port 3001 is already in use for frontend:
```bash
python -m http.server 3002
```
Then access at: http://localhost:3002

---

## Complete Setup Checklist

- [ ] Install Python dependencies (`pip install -r requirements.txt`)
- [ ] Run migrations (`python manage.py migrate`)
- [ ] Create superuser (`python manage.py createsuperuser`)
- [ ] Start Django server (`python manage.py runserver`)
- [ ] Start frontend server (`python -m http.server 3001`)
- [ ] Add content via admin panel
- [ ] Enable items you want to display
- [ ] View portfolio at http://localhost:3001

---

## Development Workflow

1. **Backend Development**: 
   - Make changes to models in `backend/api/models.py`
   - Run `python manage.py makemigrations` and `python manage.py migrate`
   - Test API endpoints at http://127.0.0.1:8000/api/

2. **Frontend Development**:
   - Edit HTML in `frontend/index.html`
   - Edit CSS in `frontend/css/style.css` and `frontend/css/responsive.css`
   - Edit JavaScript in `frontend/js/app.js` and `frontend/js/main.js`
   - Refresh browser to see changes

3. **Adding Content**:
   - Use Django admin panel at http://127.0.0.1:8000/admin
   - All changes reflect immediately on frontend after refresh

---

## Next Steps

1. Customize the design in `frontend/css/style.css`
2. Add more sections if needed
3. Deploy to production when ready
4. Configure proper CORS settings for production
5. Set up proper media file serving for production

