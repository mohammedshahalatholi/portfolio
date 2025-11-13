# Quick Deployment Guide

## For PythonAnywhere (Easiest)

1. Sign up at [pythonanywhere.com](https://www.pythonanywhere.com)
2. Upload your project files
3. In Web tab, create new web app (Manual configuration)
4. Edit WSGI file to point to your project
5. Set environment variables in Web tab
6. Reload web app

## For Heroku

1. Install Heroku CLI
2. Login: `heroku login`
3. Create app: `heroku create your-app-name`
4. Set config vars:
   ```bash
   heroku config:set SECRET_KEY=your-secret-key
   heroku config:set DEBUG=False
   heroku config:set ALLOWED_HOSTS=your-app-name.herokuapp.com
   ```
5. Deploy: `git push heroku main`
6. Run migrations: `heroku run python manage.py migrate`

## For AWS/DigitalOcean

1. Launch server (Ubuntu)
2. SSH into server
3. Install: `sudo apt install python3-pip python3-venv nginx`
4. Clone project
5. Setup virtual environment
6. Install dependencies: `pip install -r requirements.txt`
7. Configure Gunicorn + Nginx
8. Setup SSL with Let's Encrypt

## Environment Variables Needed

Create `.env` file in `backend` directory:

```env
SECRET_KEY=generate-with-django-admin
DEBUG=False
ALLOWED_HOSTS=yourdomain.com
CORS_ALLOWED_ORIGINS=https://yourdomain.com
```

## Generate Secret Key

```python
python -c "from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())"
```

## Before Deploying

1. ✅ Update `.env` file with production values
2. ✅ Run `python manage.py collectstatic`
3. ✅ Run `python manage.py migrate`
4. ✅ Create superuser: `python manage.py createsuperuser`
5. ✅ Test locally with `DEBUG=False`

## Frontend Deployment

### Option 1: Serve with Django
- Copy frontend files to Django static directory
- Django will serve them automatically

### Option 2: Deploy Separately
- Update `API_BASE_URL` in `frontend/js/app.js`
- Deploy to Netlify/Vercel/GitHub Pages
- Update CORS settings in backend

## Common Issues

**Static files not loading?**
- Run: `python manage.py collectstatic`
- Check STATIC_ROOT in settings.py

**CORS errors?**
- Update CORS_ALLOWED_ORIGINS with your frontend URL
- Set CORS_ALLOW_ALL_ORIGINS=False

**500 errors?**
- Check server logs
- Verify all environment variables are set
- Check DEBUG=False

For detailed instructions, see [DEPLOYMENT.md](DEPLOYMENT.md)

