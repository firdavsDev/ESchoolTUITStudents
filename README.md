## Online School Portal

### Usage:
- Clone the repository
- Create a virtual environment: `python -m venv venv`
- Activate the virtual environment: `source venv/bin/activate`(Linux) or `venv\Scripts\activate`(Windows)
- Install the requirements: `pip install -r requirements.txt`
- Run migrations: `python manage.py makemigrations` and `python manage.py migrate`
- Run the server using `python manage.py runserver` or just run `sh start.sh`
- Create a superuser using `python manage.py createsuperuser`

### Used Technologies:
- Python
- Django
- HTML
- CSS
- Bootstrap
- JavaScript
- SQLite
- Pillow (for image handling)

### Database tables:
- Teacher
- Course
- Event
- Contact (alert on telegram)
