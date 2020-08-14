
# Create virtual env
virtualenv venv

# Activate virtual env
source venv/bin/activate

# View installed packages
pip list

# Steps
#1. Create Project
#2. Create App. One project can have multiple apps


# Create project
django-admin startproject invoice_app

# Create app
django-admin startproject first_app

# Run server
python manage.py runserver

# Updates database schema. Manages both apps with migrations and those without.
python manage.py migrate


# https://docs.djangoproject.com/en/3.1/topics/migrations/
# Creates new migration(s) for apps.
python manage.py makemigrations invoice_app

# create superuser
python manage.py createsuperuser


# View sql table creation commands
python manage.py sqlmigrate invoice_app 0001

# Launch db shell
python manage.py dbshell

# View schema in sqllite
sqlite> .schema invoice_app_customer --indent

# Show migrations
python manage.py showmigrations

# Unapply all changes to model
python manage.py migrate invoice_app zero

# Launch shell
pip install ipython
python manage.py shell -i ipython

>> from invoice_app import models
>> list(models.Customer.objects.raw("select * from invoice_app_customer where name = %s", ["abul"]))
>> models.Customer.objects.get(id = 4)
>> models.Customer.objects.filter(name = "Abul")


# Deploy
pip install gunicorn
gunicorn -w 10 DjangoProject.wsgi

