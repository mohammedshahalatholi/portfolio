# Troubleshooting Guide

## Issue: "Loading..." Message Stuck on Frontend

### Symptoms
- Frontend shows "Loading..." or "Profile Loading..."
- No content appears on the portfolio page

### Solutions

#### 1. Check Backend Server is Running
```bash
# Make sure backend is running
cd backend
python manage.py runserver
```
Backend should be accessible at: http://127.0.0.1:8000

#### 2. Check Browser Console for Errors
1. Open browser Developer Tools (F12)
2. Go to "Console" tab
3. Look for errors like:
   - `Failed to fetch`
   - `CORS error`
   - `Network error`

#### 3. Verify API Endpoints are Working
Open these URLs in your browser:
- http://127.0.0.1:8000/api/about/ - Should return JSON (may be empty array `[]`)
- http://127.0.0.1:8000/api/projects/ - Should return JSON
- http://127.0.0.1:8000/api/skills/ - Should return JSON

#### 4. Check CORS Settings
Make sure in `backend/portfolio/settings.py`:
```python
CORS_ALLOW_ALL_ORIGINS = True  # For development
```

#### 5. Add Content via Admin Panel
The "Loading..." message appears because there's no content in the database yet.

1. Go to: http://127.0.0.1:8000/admin
2. Create a superuser if you haven't:
   ```bash
   cd backend
   python manage.py createsuperuser
   ```
3. Login to admin panel
4. Add content:
   - **About**: Add your name, bio, and profile image
   - **Projects**: Add projects
   - **Skills**: Add skills
   - etc.
5. **Important**: Check the "Enabled" checkbox for all items you want to display
6. Refresh the frontend page

#### 6. Verify API Base URL
Check `frontend/js/app.js`:
```javascript
const API_BASE_URL = 'http://127.0.0.1:8000/api';
```
Make sure this matches your backend URL.

## Issue: CORS Errors

### Symptoms
- Browser console shows CORS errors
- API calls fail

### Solutions

1. **Check CORS is enabled:**
   - Verify `CORS_ALLOW_ALL_ORIGINS = True` in `backend/portfolio/settings.py`

2. **Check middleware order:**
   - `corsheaders.middleware.CorsMiddleware` should be before `CommonMiddleware`

3. **Restart Django server:**
   - Changes to settings.py require server restart

## Issue: API Returns Empty Arrays

### Symptoms
- API endpoints return `[]` (empty arrays)
- Frontend shows no content

### Solutions

1. **Add content via admin panel:**
   - Go to http://127.0.0.1:8000/admin
   - Add content to each section
   - Make sure "Enabled" checkbox is checked

2. **Check if items are enabled:**
   - Only enabled items are returned by the API
   - Check the "Enabled" checkbox in admin panel

## Issue: Images Not Loading

### Symptoms
- Profile images or project images don't display

### Solutions

1. **Check media files configuration:**
   - Verify `MEDIA_URL` and `MEDIA_ROOT` in `backend/portfolio/settings.py`
   - Make sure `backend/media/` directory exists

2. **Check URL configuration:**
   - Verify media files are served in development (should be in `urls.py`)

3. **Upload images through admin:**
   - Use the admin panel to upload images
   - Images should be saved to `backend/media/` directory

## Issue: Frontend Not Updating

### Symptoms
- Changes in admin panel don't appear on frontend

### Solutions

1. **Refresh the page:**
   - Hard refresh: Ctrl+F5 (Windows) or Cmd+Shift+R (Mac)

2. **Check if items are enabled:**
   - Make sure "Enabled" checkbox is checked in admin

3. **Check browser cache:**
   - Clear browser cache or use incognito mode

4. **Check API is returning data:**
   - Visit API endpoints directly in browser
   - Verify data is there and enabled

## Common Commands

### Start Backend Server
```bash
cd backend
python manage.py runserver
```

### Start Frontend Server
```bash
cd frontend
python -m http.server 3001
```

### Create Admin User
```bash
cd backend
python manage.py createsuperuser
```

### Check Django Setup
```bash
cd backend
python manage.py check
```

### View Database
```bash
cd backend
python manage.py shell
# Then in Python shell:
from api.models import About, Project, Skill
About.objects.all()
Project.objects.all()
Skill.objects.all()
```

## Quick Checklist

- [ ] Backend server is running on http://127.0.0.1:8000
- [ ] Frontend server is running on http://localhost:3001
- [ ] Admin user is created
- [ ] Content is added via admin panel
- [ ] Items are enabled in admin panel
- [ ] Browser console shows no errors
- [ ] API endpoints return data (check in browser)
- [ ] CORS is enabled in settings.py

## Still Having Issues?

1. Check browser console (F12) for detailed error messages
2. Check Django server logs for backend errors
3. Verify both servers are running
4. Test API endpoints directly in browser
5. Make sure all dependencies are installed: `pip install -r requirements.txt`

