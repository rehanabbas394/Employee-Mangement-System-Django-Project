# Employee Management System (Django)

This is a Django-based Employee Management System that allows you to manage employee information, roles, departments, and more.

## Setup Instructions

### Prerequisites
- Python 3.6+
- pip (Python package installer)

### Installation Steps

1. **Clone the repository**
   ```
   git clone <repository-url>
   cd Employee-Mangement-System-Django-Project
   ```

2. **Create a virtual environment (recommended)**
   ```
   python -m venv venv
   ```

3. **Activate the virtual environment**
   - On Linux/Mac:
     ```
     source venv/bin/activate
     ```
   - On Windows:
     ```
     venv\Scripts\activate
     ```

4. **Install required dependencies**
   ```
   pip install -r requirements.txt
   ```

5. **Create the info.py file (if it doesn't exist)**
   
   Create a file at `Employee_management_system/info.py` with your email settings:
   ```python
   EMAIL_USE_TLS = True
   EMAIL_HOST = 'smtp.gmail.com'
   EMAIL_HOST_USER = "your-email@gmail.com" 
   EMAIL_HOST_PASSWORD = "your-password"
   EMAIL_PORT = 587
   ```
   Note: You need to set up an app password if using Gmail with 2FA.

6. **Database setup**
   
   The project uses SQLite by default. Run migrations to set up the database:
   ```
   python manage.py migrate
   ```

7. **Create a superuser (admin)**
   ```
   python manage.py createsuperuser
   ```

8. **Run the development server**
   ```
   python manage.py runserver
   ```

9. **Access the application**
   - Web Interface: http://127.0.0.1:8000/
   - Admin Interface: http://127.0.0.1:8000/admin/

## Features

- Employee management (add, edit, delete employees)
- Department management
- Role management
- User authentication
- Email notifications

## Tech Stack

- Django 5.0
- SQLite (database)
- HTML/CSS/JavaScript (frontend)

## For Developers

### Generating requirements.txt

If you've added new dependencies to the project, update the requirements.txt file:

```
pip freeze > requirements.txt
```

Or add only the specific packages you know are needed:

```
pip install pipreqs
pipreqs .
``` 