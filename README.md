# Calorie Counter App

A Django-based web application to track daily calorie intake with PostgreSQL backend and Tailwind CSS styling.

## Features

- Add food items with calorie counts
- View all food items for the day
- Remove individual items
- Calculate total daily calories
- Reset all items for the day
- Responsive design with Tailwind CSS

## Tech Stack

- Python 3.x
- Django 3.x
- PostgreSQL
- Tailwind CSS
- HTML5/CSS3

## Installation

1. Clone the repository:
```bash
git clone <your-repo-url>
cd calorie_counter
Create virtual environment:

bash
python -m venv venv
source venv/Scripts/activate  # On Windows: venv\Scripts\activate
Install dependencies:

bash
pip install django psycopg2-binary
Configure PostgreSQL:

Create database named calorie_db

Update database credentials in settings.py

Run migrations:

bash
python manage.py makemigrations
python manage.py migrate
Start the server:

bash
python manage.py runserver
Deployment (Render)
Push code to GitHub

Create a new Web Service on Render

Connect your repository

Add environment variables:

DATABASE_URL (PostgreSQL connection string)

SECRET_KEY

Set build command: pip install -r requirements.txt

Set start command: gunicorn calorie_project.wsgi

Live Demo
[Add your deployed link here]

License
MIT

text

## Step 11: Create requirements.txt

```bash
pip freeze > requirements.txt
Quick Deployment Commands
For deployment, create requirements.txt:

text
Django>=3.2,<4.0
psycopg2-binary
gunicorn
whitenoise
Final Checklist
 PostgreSQL Setup: Create database and update credentials
 Run migrations: python manage.py migrate
 Test locally: python manage.py runserver
 Git initialization:

bash
git init
git add .
git commit -m "Initial commit: Complete Calorie Counter app"
 Deploy to Render: Follow Render's Django deployment guide