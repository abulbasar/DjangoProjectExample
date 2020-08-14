
# Create virtual env
virtualenv venv

# Activate virtual env
source venv/bin/activate

# View installed packages
pip list

pip install django

If cloned git repo)
pip install -r requirements.txt 

# Steps
#1. Create Project
#2. Create App. One project can have multiple apps

# Create project
```
$ django-admin startproject my-django-project

$ tree MyDjangoProject/
MyDjangoProject/
├── MyDjangoProject
│   ├── __init__.py
│   ├── asgi.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
└── manage.py
```


# Create app
```
$ cd MyDjangoProject
$ django-admin startapp invoice_app
$ tree .
.
├── MyDjangoProject
│   ├── __init__.py
│   ├── asgi.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── invoice_app
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── migrations
│   │   └── __init__.py
│   ├── models.py
│   ├── tests.py
│   └── views.py
└── manage.py
```


# Run server
python manage.py runserver



# Updates database schema. Manages both apps with migrations and those without.
# It will apply model changes to the databases 
python manage.py migrate


# create superuser to login to admin page. You can create standard users as well 
# if your  application does not  support self registration

python manage.py createsuperuser

After this if you go to the database, you can see the tables created.
$ python manage.py dbshell
sqlite> .tables
auth_group                  auth_user_user_permissions
auth_group_permissions      django_admin_log          
auth_permission             django_content_type       
auth_user                   django_migrations         
auth_user_groups            django_session  


Enable Templates
1. created a directory called templates under project root (the directory that contains manage.py)
2. Update MyDjangoProject/settings.py to specify templates


# https://docs.djangoproject.com/en/3.1/topics/migrations/
# Creates new migration(s) for apps.

Django identifies the changes in the current model by comparing it 
history captured in the form of migration steps under invoice_app/migrations

python manage.py makemigrations invoice_app

Django will apply the db migration steps as required
python manage.py migrate

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


from faker import Faker
fake = Faker()
for i in range(10):
    r = CustomerModel()
    r.name = fake.name()
    r.tax_id = fake.ssn()
    r.email = fake.email()
    r.save()



# Deploy
pip install gunicorn
gunicorn -w 10 DjangoProject.wsgi

Launch 
pip install gunicorn
GUNICORN_CMD_ARGS="--bind=0.0.0.0 --workers=10" gunicorn MyDjangoProject.wsgi
