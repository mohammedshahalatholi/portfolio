@echo off
REM Deployment script for portfolio backend (Windows)

echo Starting deployment...

REM Activate virtual environment if it exists
if exist venv\Scripts\activate.bat (
    call venv\Scripts\activate.bat
)

REM Install/update dependencies
echo Installing dependencies...
pip install -r requirements.txt

REM Run migrations
echo Running migrations...
python manage.py migrate

REM Collect static files
echo Collecting static files...
python manage.py collectstatic --noinput

REM Create superuser if needed (uncomment if needed)
REM echo Creating superuser...
REM python manage.py createsuperuser

echo Deployment complete!
echo To start the server:
echo   Development: python manage.py runserver
echo   Production: gunicorn portfolio.wsgi

pause

