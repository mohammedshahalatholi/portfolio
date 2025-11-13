@echo off
echo ========================================
echo Django Backend Server
echo ========================================
echo.
cd backend

echo [1/4] Installing dependencies...
pip install -r requirements.txt
echo.

echo [2/4] Creating migrations...
python manage.py makemigrations
echo.

echo [3/4] Applying migrations...
python manage.py migrate
echo.

echo [4/4] Starting server...
echo.
echo ========================================
echo Server running on: http://127.0.0.1:8000
echo Admin panel: http://127.0.0.1:8000/admin
echo API: http://127.0.0.1:8000/api/
echo ========================================
echo.
echo NOTE: If this is your first time, you may need to create a superuser.
echo Run this in another terminal: python manage.py createsuperuser
echo.
python manage.py runserver
pause

