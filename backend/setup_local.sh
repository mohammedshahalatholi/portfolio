#!/bin/bash
# Setup script for local development

echo "Setting up local development environment..."

# Create .env file if it doesn't exist
if [ ! -f .env ]; then
    echo "Creating .env file..."
    cat > .env << EOF
# Django Settings for Local Development
SECRET_KEY=django-insecure-change-this-in-production
DEBUG=True
ALLOWED_HOSTS=localhost,127.0.0.1,*

# CORS Settings for Local Development
CORS_ALLOWED_ORIGINS=http://localhost:3000,http://localhost:3001,http://127.0.0.1:3000,http://127.0.0.1:3001
CORS_ALLOW_ALL_ORIGINS=True

# Security Settings (not needed for local development)
SECURE_SSL_REDIRECT=False
EOF
    echo ".env file created!"
else
    echo ".env file already exists."
fi

# Install dependencies
echo ""
echo "Installing dependencies..."
pip install -r requirements.txt

# Run migrations
echo ""
echo "Running migrations..."
python manage.py migrate

echo ""
echo "Setup complete!"
echo ""
echo "To start the server, run:"
echo "  python manage.py runserver"
echo ""

