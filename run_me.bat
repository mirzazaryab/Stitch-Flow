@echo off
echo Starting Stitch Flow Project...

REM Activate virtual environment
call venv\Scripts\activate

REM Run migrations
python manage.py migrate

REM Start server
python manage.py runserver

pause
