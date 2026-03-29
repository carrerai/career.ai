# AICAREER - Psychometric Career Guidance Platform

## Overview
A Django-based psychometric career guidance platform that assesses users across Aptitude, Interest (RIASEC), and Personality (Big Five) to provide AI-powered career recommendations using Google's Gemini AI.

## Tech Stack
- **Framework**: Django 5.2 (Python 3.12)
- **Database**: SQLite (`db.sqlite3`)
- **AI**: Google Generative AI (Gemini 2.5 Flash) via `google-generativeai`
- **Static Files**: WhiteNoise
- **Production Server**: Gunicorn
- **Auth**: Django built-in auth (email-based login)

## Project Structure
- `AICAREER/` - Django project config (settings, URLs, WSGI)
- `core/` - Main application
  - `models.py` - Questions, Options, TestSessions, UserResponses, Results
  - `views.py` - Test workflow views
  - `career_logic.py` - Scoring algorithms and AI prompt engineering
  - `urls.py` - App URL routing
  - `templates/core/` - HTML templates
  - `static/core/` - CSS and JS assets
  - `management/commands/` - DB seeding commands

## Running the App
The app runs on port 5000 via Django's development server:
```
python manage.py runserver 0.0.0.0:5000
```

## Environment Variables
- `GEMINI_API_KEY` - Required for AI career recommendations (Google Gemini API)

## Setup Notes
- `ALLOWED_HOSTS = ['*']` and `CSRF_TRUSTED_ORIGINS` set for Replit proxy compatibility
- Static files collected into `staticfiles/` via `python manage.py collectstatic`
- Migrations already applied; database pre-populated with questions
