# Project Requirements

## Framework & Libraries
- Python 3.x
- Django 5.2.2
- crispy_forms
- crispy_bootstrap4

## Apps
- learn
- recall
- time_management

## Database
- SQLite3 (default: `db.sqlite3`)

## User Management
- Uses Django's built-in `auth.User` model.
- Custom `UserProfile` model with fields:
  - phone_no
  - profile_picture
  - date_joined
  - last_login
  - is_active
  - is_staff

## Features

### Learn App
- Subject and goal planning via `Plan` model.
- User profile management.
- Subject-specific views and URLs.
- Authentication (register, login, logout).
- Profile page at `/Profile/`.

### Recall App
- Flashcard creation and management via `Flashcard` model.
- Each flashcard linked to a user.

### Time Management App
- (Details not shown, but present in workspace.)

## Static & Media Files
- Static files served from `learn/static/`.
- Media files (e.g., profile pictures) stored in `media/`.

## Templates
- HTML templates stored in `learn/templates/` and `recall/templates/`.

## Other
- Password validation enabled.
- Internationalization: `en-us`, timezone: `UTC`.
- Crispy forms configured for Bootstrap 4.

## How to Run
1. Install dependencies (see below).
2. Run migrations:  
   ```sh
   python manage.py migrate
   ```
3. Start development server:  
   ```sh
   python manage.py runserver
   ```

## Python Package Requirements

```
Django==5.2.2
django-crispy-forms
crispy-bootstrap4
```

Add other dependencies as needed for your environment.