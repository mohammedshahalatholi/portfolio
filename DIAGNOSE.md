# Diagnose API Connection Issue

## The Problem
Frontend cannot connect to backend API, showing error: "Unable to connect to the backend server"

## Backend Status
✅ Backend is running on port 8000 (verified with netstat)

## Diagnostic Steps

### Step 1: Test API Directly in Browser
1. Open your browser
2. Go to: http://127.0.0.1:8000/api/about/
3. You should see JSON data (may be empty array `[]`)

### Step 2: Use Test Page
1. Open `test_api.html` in your browser
2. It will automatically test all API endpoints
3. Check the results to see which endpoints work

### Step 3: Check Browser Console
1. Open your portfolio page: http://localhost:3001
2. Press F12 to open Developer Tools
3. Go to "Console" tab
4. Look for error messages like:
   - CORS errors
   - Network errors
   - Connection refused
   - Failed to fetch

### Step 4: Check Network Tab
1. In Developer Tools, go to "Network" tab
2. Refresh the page
3. Look for API requests (to `/api/about/`, `/api/projects/`, etc.)
4. Click on each request to see:
   - Request URL
   - Status code
   - Response
   - Error messages

### Step 5: Verify CORS Settings
Check `backend/portfolio/settings.py`:
```python
CORS_ALLOW_ALL_ORIGINS = True  # Should be True
```

### Step 6: Try Different URLs
The frontend uses `http://127.0.0.1:8000/api` but try:
- `http://localhost:8000/api` (instead of 127.0.0.1)
- Some browsers treat localhost and 127.0.0.1 differently

## Common Issues and Solutions

### Issue 1: CORS Error
**Symptoms:** Console shows "CORS policy" error
**Solution:**
1. Make sure `CORS_ALLOW_ALL_ORIGINS = True` in settings.py
2. Restart Django server
3. Check middleware order in settings.py

### Issue 2: Connection Refused
**Symptoms:** "Failed to fetch" or "Connection refused"
**Solution:**
1. Make sure backend server is running
2. Check if port 8000 is accessible
3. Try accessing http://127.0.0.1:8000/ directly in browser

### Issue 3: Mixed Content
**Symptoms:** Errors about HTTP/HTTPS
**Solution:**
- Make sure both frontend and backend use HTTP (not HTTPS)
- Frontend: http://localhost:3001
- Backend: http://127.0.0.1:8000

### Issue 4: Firewall Blocking
**Symptoms:** Connection timeouts
**Solution:**
1. Check Windows Firewall settings
2. Allow Python through firewall
3. Temporarily disable firewall to test

## Quick Fixes to Try

### Fix 1: Change API URL to localhost
Edit `frontend/js/app.js`:
```javascript
const API_BASE_URL = 'http://localhost:8000/api';
```
Instead of:
```javascript
const API_BASE_URL = 'http://127.0.0.1:8000/api';
```

### Fix 2: Restart Both Servers
1. Stop backend server (Ctrl+C)
2. Stop frontend server (Ctrl+C)
3. Start backend: `cd backend && python manage.py runserver`
4. Start frontend: `cd frontend && python -m http.server 3001`

### Fix 3: Check Django Server Logs
Look at the terminal where Django is running for any error messages

### Fix 4: Test with curl
Open terminal and run:
```bash
curl http://127.0.0.1:8000/api/about/
```
Should return JSON data

## Next Steps
1. Run the diagnostic steps above
2. Check browser console for specific error messages
3. Test API endpoints directly in browser
4. Use test_api.html to see which endpoints work
5. Report back with specific error messages you see

