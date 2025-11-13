@echo off
REM Setup script for local development

echo Setting up local development environment...

REM Create .env file if it doesn't exist
if not exist .env (
    echo Creating .env file...
    (
        echo # Django Settings for Local Development
        echo SECRET_KEY=django-insecure-change-this-in-production
        echo DEBUG=True
        echo ALLOWED_HOSTS=localhost,127.0.0.1,*
        echo.
        echo # CORS Settings for Local Development
        echo CORS_ALLOWED_ORIGINS=http://localhost:3000,http://localhost:3001,http://127.0.0.1:3000,http://127.0.0.1:3001
        echo CORS_ALLOW_ALL_ORIGINS=True
        echo.
        echo # Security Settings (not needed for local development)
        echo SECURE_SSL_REDIRECT=False
    ) > .env
    echo .env file created!
) else (
    echo .env file already exists.
)

REM Install dependencies
echo.
echo Installing dependencies...
pip install -r requirements.txt

REM Run migrations
echo.
echo Running migrations...
python manage.py migrate

echo.
echo Setup complete!
echo.
echo To start the server, run:
echo   python manage.py runserver
echo.
pause

