# Portfolio Website with Django Backend

A modern portfolio website with a Django REST API backend and HTML/CSS/JavaScript frontend. This project allows you to manage your portfolio content through a Django admin panel with CRUD operations for experiences, projects, skills, education, contact info, social links, awards, and hobbies.

## Features

- **Backend**: Django REST Framework API
- **Database**: SQLite
- **Admin Panel**: Django admin for managing all portfolio content
- **Frontend**: Modern, responsive HTML/CSS/JavaScript
- **Enable/Disable**: Toggle visibility of sections and items
- **CRUD Operations**: Create, Read, Update, Delete for all models

## Project Structure

```
portfolio_v1/
├── backend/          # Django backend
│   ├── portfolio/    # Django project settings
│   ├── api/          # API app with models, views, serializers
│   └── manage.py     # Django management script
├── frontend/         # Frontend files
│   ├── index.html    # Main HTML file
│   ├── css/          # Stylesheets
│   └── js/           # JavaScript files
└── README.md
```

## Quick Start (Windows)

### Easy Method (Using Batch Files)

1. **Start Backend:**
   - Double-click `start_backend.bat`
   - First time: It will install dependencies and run migrations
   - Createsuperuser: If prompted, create an admin user with:
     ```bash
     python manage.py createsuperuser
     ```
   - Backend runs at: `http://127.0.0.1:8000`

2. **Start Frontend (in a new terminal):**
   - Double-click `start_frontend.bat`
   - Frontend runs at: `http://localhost:3001`

3. **Add Content:**
   - Go to: `http://127.0.0.1:8000/admin`
   - Login and add your portfolio content
   - Make sure to enable items you want to display

## Setup Instructions

### Backend Setup

1. **Navigate to backend directory:**
   ```bash
   cd backend
   ```

2. **Create a virtual environment (recommended):**
   ```bash
   python -m venv venv
   # On Windows
   venv\Scripts\activate
   # On Linux/Mac
   source venv/bin/activate
   ```

3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Run migrations:**
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

5. **Create a superuser for admin access:**
   ```bash
   python manage.py createsuperuser
   ```
   Follow the prompts to create username, email, and password.

6. **Run the development server:**
   ```bash
   python manage.py runserver
   ```

The backend will be available at `http://127.0.0.1:8000`
- Admin Panel: `http://127.0.0.1:8000/admin`
- API: `http://127.0.0.1:8000/api/`

### Frontend Setup

1. **Open a NEW terminal window** (keep backend running)

2. **Serve the frontend:**
   - Option 1: Use a simple HTTP server (Python):
     ```bash
     cd frontend
     python -m http.server 3001
     ```
   - Option 2: Use Live Server extension in VS Code
   - Option 3: Double-click `start_frontend.bat` (Windows)

3. **Access the frontend:**
   - Open browser: `http://localhost:3001`
   - Make sure the backend is running on `http://127.0.0.1:8000`

### API Configuration

The frontend is configured to connect to `http://127.0.0.1:8000/api`. If you're running the backend on a different URL or port, update the `API_BASE_URL` in `frontend/js/app.js`.

### First Time Setup Checklist

- [ ] Install Python (if not installed)
- [ ] Run `start_backend.bat` or follow backend setup steps
- [ ] Create superuser account
- [ ] Run `start_frontend.bat` or follow frontend setup steps
- [ ] Open `http://localhost:3001` in browser
- [ ] Go to `http://127.0.0.1:8000/admin` and add content
- [ ] Enable items you want to display
- [ ] Refresh frontend to see your content

## Usage

### Admin Panel

1. Access the admin panel at `http://127.0.0.1:8000/admin`
2. Log in with your superuser credentials
3. Manage your portfolio content:
   - **About**: Add your name, bio, and profile image
   - **Experiences**: Add work experiences
   - **Projects**: Add projects with images and links
   - **Skills**: Add skills with categories and proficiency levels
   - **Education**: Add educational background
   - **Contact Info**: Add contact information
   - **Social Links**: Add social media links
   - **Awards**: Add awards and achievements
   - **Hobbies**: Add hobbies and interests

### Enable/Disable Items

Each model has an `enabled` field that you can toggle in the admin panel. Only enabled items will be displayed on the frontend.

### API Endpoints

- `GET /api/about/` - Get about information
- `GET /api/experiences/` - Get all experiences
- `GET /api/projects/` - Get all projects
- `GET /api/skills/` - Get all skills
- `GET /api/education/` - Get all education
- `GET /api/contact/` - Get contact information
- `GET /api/social-links/` - Get all social links
- `GET /api/awards/` - Get all awards
- `GET /api/hobbies/` - Get all hobbies

All endpoints return only enabled items by default for public access.

## Models

### About
- name (CharField)
- bio (TextField)
- profile_image (ImageField)
- enabled (BooleanField)

### Experience
- title (CharField)
- company (CharField)
- description (TextField)
- start_date (DateField)
- end_date (DateField, optional)
- enabled (BooleanField)

### Project
- title (CharField)
- description (TextField)
- image (ImageField, optional)
- link (URLField, optional)
- technologies (CharField)
- enabled (BooleanField)

### Skill
- name (CharField)
- category (CharField, optional)
- proficiency_level (IntegerField, 0-100)
- enabled (BooleanField)

### Education
- degree (CharField)
- institution (CharField)
- description (TextField, optional)
- start_date (DateField)
- end_date (DateField, optional)
- enabled (BooleanField)

### ContactInfo
- email (EmailField)
- phone (CharField, optional)
- location (CharField, optional)
- enabled (BooleanField)

### SocialLink
- platform (CharField)
- url (URLField)
- icon (CharField, optional)
- enabled (BooleanField)

### Award
- title (CharField)
- description (TextField, optional)
- date (DateField)
- issuer (CharField, optional)
- enabled (BooleanField)

### Hobby
- name (CharField)
- description (TextField, optional)
- icon (CharField, optional)
- enabled (BooleanField)

## Development

### Adding New Fields

1. Update the model in `backend/api/models.py`
2. Create a migration: `python manage.py makemigrations`
3. Apply the migration: `python manage.py migrate`
4. Update the serializer in `backend/api/serializers.py`
5. Update the frontend rendering in `frontend/js/app.js`

### Customizing Styles

Edit `frontend/css/style.css` for main styles and `frontend/css/responsive.css` for responsive design.

## Deployment

The portfolio is ready for deployment to various hosting platforms. See the deployment guides for detailed instructions:

- **[DEPLOYMENT.md](DEPLOYMENT.md)** - Comprehensive deployment guide for all platforms
- **[DEPLOYMENT_QUICK_START.md](DEPLOYMENT_QUICK_START.md)** - Quick reference for common platforms

### Quick Deployment Steps

1. **Configure Environment Variables**:
   - Copy `backend/env.example` to `backend/.env`
   - Update with your production values:
     ```env
     SECRET_KEY=your-secret-key-here
     DEBUG=False
     ALLOWED_HOSTS=yourdomain.com,www.yourdomain.com
     CORS_ALLOWED_ORIGINS=https://yourdomain.com
     ```

2. **Generate Secret Key**:
   ```python
   python -c "from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())"
   ```

3. **Run Deployment Script**:
   - Windows: `backend\deploy.bat`
   - Linux/Mac: `bash backend/deploy.sh`

4. **Deploy to Your Platform**:
   - **PythonAnywhere**: See [DEPLOYMENT.md](DEPLOYMENT.md#pythonanywhere)
   - **Heroku**: See [DEPLOYMENT.md](DEPLOYMENT.md#heroku)
   - **AWS/DigitalOcean**: See [DEPLOYMENT.md](DEPLOYMENT.md#aws)
   - **Railway/Render**: See [DEPLOYMENT.md](DEPLOYMENT.md#railway)

### Production Checklist

- [ ] Set `DEBUG=False` in `.env`
- [ ] Generate and set strong `SECRET_KEY`
- [ ] Configure `ALLOWED_HOSTS` with your domain
- [ ] Set `CORS_ALLOWED_ORIGINS` with your frontend URL
- [ ] Run `python manage.py collectstatic`
- [ ] Run `python manage.py migrate`
- [ ] Create superuser account
- [ ] Setup SSL/HTTPS certificate
- [ ] Configure static and media files serving
- [ ] Test all functionality in production
Access url
Frontend : https://mohammedshahalatholi.github.io/frontend-portfolio/
backend : https://mohammedshahal.pythonanywhere.com/admin/
## License

This project is open source and available under the MIT License.

