@echo off

rem Check if Python is installed
where python >nul 2>nul
if %errorlevel% neq 0 (
    echo Python is not installed. Please install Python and run the script again.
    exit /b 1
) else (
    echo Python is installed
)

rem Check if virtual environment exists, and create one if not
if not exist venv (
    python -m venv venv
)

rem Activate virtual environment
call venv\Scripts\activate

rem Install dependencies
pip install -r requirements.txt

rem Run migrations
python manage.py makemigrations
python manage.py migrate

rem Seed the database (adjust the command accordingly)
python manage.py createdefaultusers

rem Collect static files
python manage.py collectstatic --noinput

rem Run the development server
python manage.py runserver