# Fix Backend Connection Issue

## Current Status
✅ Backend is running on port 8000
❌ Frontend cannot connect to backend

## Quick Fixes to Try

### Fix 1: Restart Django Server with Explicit Host
Stop the current Django server and restart it with:
```bash
cd backend
python manage.py runserver 0.0.0.0:8000
```
Or:
```bash
python manage.py runserver localhost:8000
```

### Fix 2: Test API Directly
Open these URLs in your browser to test:
- http://127.0.0.1:8000/api/about/
- http://localhost:8000/api/about/

Both should return JSON (may be empty array `[]`)

### Fix 3: Check Browser Console
1. Open http://localhost:3001
2. Press F12 (Developer Tools)
3. Go to Console tab
4. Look for error messages
5. Go to Network tab
6. Refresh page
7. Look for failed requests to `/api/`

### Fix 4: Use Test Page
1. Open `test_api.html` in your browser
2. It will test all API endpoints
3. Check which ones work/fail

### Fix 5: Change API URL
I've already changed the API URL to use `localhost` instead of `127.0.0.1`. Try refreshing the page.

If that doesn't work, change it back in `frontend/js/app.js`:
```javascript
const API_BASE_URL = 'http://127.0.0.1:8000/api';
```

### Fix 6: Check CORS in Browser
1. Open browser console (F12)
2. Go to Network tab
3. Try to load the page
4. Look for CORS errors in console
5. Check if requests are being blocked

### Fix 7: Verify Django Settings
Make sure in `backend/portfolio/settings.py`:
```python
CORS_ALLOW_ALL_ORIGINS = True
CORS_ALLOWED_ORIGINS = [
    "http://localhost:3001",
    "http://127.0.0.1:3001",
]
```

### Fix 8: Try Different Browser
Sometimes browser extensions or settings can block requests. Try:
- Incognito/Private mode
- Different browser
- Disable browser extensions

## Step-by-Step Diagnosis

### Step 1: Verify Backend is Running
```bash
# Check if port 8000 is listening
netstat -ano | findstr ":8000"
```
Should show LISTENING on 127.0.0.1:8000

### Step 2: Test API in Browser
Open: http://127.0.0.1:8000/api/about/
Should show JSON response

### Step 3: Test API with curl
```bash
curl http://127.0.0.1:8000/api/about/
```
Should return JSON

### Step 4: Check Browser Console
1. Open http://localhost:3001
2. F12 → Console tab
3. Look for error messages
4. Note the exact error message

### Step 5: Check Network Requests
1. F12 → Network tab
2. Refresh page
3. Look for requests to `/api/`
4. Check status codes
5. Check response

## Common Error Messages and Solutions

### "Failed to fetch"
- Backend might not be running
- Port might be wrong
- Firewall might be blocking

### "CORS policy" error
- CORS not enabled in Django
- Wrong CORS settings
- Restart Django server

### "Connection refused"
- Backend not running
- Wrong port
- Firewall blocking

### "Network error"
- Backend not accessible
- Check firewall
- Check if backend is running

## Next Steps
1. Try Fix 1 first (restart Django server)
2. Test API in browser (Fix 2)
3. Check browser console (Fix 3)
4. Use test page (Fix 4)
5. Report back with specific error messages

