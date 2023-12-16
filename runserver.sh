#!/bin/bash

# Check if Python is installed
if command -v python3 &>/dev/null; then
    echo "Python is installed"
else
    echo "Python is not installed. Please install Python and run the script again."
    exit 1
fi

# Check if virtual environment exists, and create one if not
if [ ! -d "venv" ]; then
    python3 -m venv venv
fi

# Activate virtual environment
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Run migrations
python3 manage.py makemigrations
python3 manage.py migrate

# Seed the database (adjust the command accordingly)
python3 manage.py createdefaultusers

# Collect static files
python3 manage.py collectstatic --noinput

# Run the development server
python3 manage.py runserver
