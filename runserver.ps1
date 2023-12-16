# Check if Python is installed
if (Test-Path -Path "$(Get-Command python -ErrorAction SilentlyContinue)") {
    Write-Output "Python is installed"
} else {
    Write-Output "Python is not installed. Please install Python and run the script again."
    exit 1
}

# Check if virtual environment exists, and create one if not
if (-not (Test-Path -Path .\venv)) {
    python -m venv venv
}

# Activate virtual environment
. .\venv\Scripts\Activate

# Install dependencies
pip install -r requirements.txt

# Run migrations
python manage.py makemigrations
python manage.py migrate

# Seed the database (adjust the command accordingly)
python manage.py createdefaultusers

# Collect static files
python manage.py collectstatic --noinput

# Run the development server
python manage.py runserver
