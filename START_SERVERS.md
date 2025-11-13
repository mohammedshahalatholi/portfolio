# 🚀 Start Servers - Step by Step

## Current Status

✅ **Dependencies Installed**
✅ **Database Migrations Applied**
✅ **Frontend Server**: Running on port 3001
⚠️ **Backend Server**: Needs to be started manually

## How to Start Servers

### Option 1: Using Batch Files (Recommended)

**Terminal 1 - Backend:**
1. Double-click `start_backend.bat`
   OR
2. Open terminal and run:
   ```bash
   cd backend
   python manage.py runserver
   ```

**Terminal 2 - Frontend:**
1. Double-click `start_frontend.bat`
   OR
2. Open a NEW terminal and run:
   ```bash
   cd frontend
   python -m http.server 3001
   ```

### Option 2: Manual Commands

**Open TWO separate terminal windows:**

**Terminal 1 (Backend):**
```bash
cd backend
python manage.py runserver
```
You should see: "Starting development server at http://127.0.0.1:8000/"

**Terminal 2 (Frontend):**
```bash
cd frontend
python -m http.server 3001
```
You should see: "Serving HTTP on 0.0.0.0 port 3001"

## Verify Servers Are Running

### Check Backend:
- Open browser: http://127.0.0.1:8000
- Should see Django welcome page or API root

### Check Frontend:
- Open browser: http://localhost:3001
- Should see your portfolio website (may be empty until you add content)

### Check API:
- Open browser: http://127.0.0.1:8000/api/
- Should see API root with available endpoints

## First Time Setup

### Create Admin User:

1. Open a NEW terminal (while servers are running)
2. Run:
   ```bash
   cd backend
   python manage.py createsuperuser
   ```
3. Enter:
   - Username: (your choice)
   - Email: (your email)
   - Password: (your password)

### Add Content:

1. Go to: http://127.0.0.1:8000/admin
2. Login with your superuser credentials
3. Add your portfolio content:
   - **About**: Click "About" → "Add About"
     - Enter your name and bio
     - Upload profile image (optional)
     - Check "Enabled" checkbox
     - Click "Save"
   
   - **Projects**: Click "Projects" → "Add Project"
     - Enter title, description
     - Add technologies (comma-separated)
     - Add project link and image (optional)
     - Check "Enabled" checkbox
     - Click "Save"
   
   - **Skills**: Click "Skills" → "Add Skill"
     - Enter skill name
     - Add category (optional)
     - Set proficiency level (0-100)
     - Check "Enabled" checkbox
     - Click "Save"
   
   - Repeat for: Experiences, Education, Contact Info, Social Links, Awards, Hobbies

4. **Important**: Always check "Enabled" checkbox for items you want to display!

5. View your portfolio at: http://localhost:3000

## Troubleshooting

### Backend Not Starting:
- Check if port 8000 is already in use
- Try: `python manage.py runserver 8001`
- Update `API_BASE_URL` in `frontend/js/app.js` if port changed

### Frontend Not Starting:
- Check if port 3001 is already in use
- Try: `python -m http.server 3002`
- Access at: http://localhost:3002

### CORS Errors:
- Make sure backend is running
- Check `backend/portfolio/settings.py` has `CORS_ALLOW_ALL_ORIGINS = True`

### No Content Showing:
- Make sure items are "enabled" in admin panel
- Check browser console for errors (F12)
- Verify backend is running and accessible

## URLs Reference

- **Backend**: http://127.0.0.1:8000
- **Admin Panel**: http://127.0.0.1:8000/admin
- **API Root**: http://127.0.0.1:8000/api/
- **Frontend**: http://localhost:3001

## Next Steps

1. ✅ Start both servers
2. ✅ Create admin user
3. ✅ Add your content via admin panel
4. ✅ Enable items you want to display
5. ✅ View your portfolio at http://localhost:3001
6. ✅ Customize design in `frontend/css/style.css`

Enjoy your portfolio website! 🎉

