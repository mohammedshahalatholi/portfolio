#!/bin/bash
# Deployment script for portfolio backend

echo "Starting deployment..."

# Activate virtual environment if it exists
if [ -d "venv" ]; then
    source venv/bin/activate
fi

# Install/update dependencies
echo "Installing dependencies..."
pip install -r requirements.txt

# Run migrations
echo "Running migrations..."
python manage.py migrate

# Collect static files
echo "Collecting static files..."
python manage.py collectstatic --noinput

# Create superuser if needed (uncomment if needed)
# echo "Creating superuser..."
# python manage.py createsuperuser

echo "Deployment complete!"
echo "To start the server:"
echo "  Development: python manage.py runserver"
echo "  Production: gunicorn portfolio.wsgi"

