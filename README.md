# BaseLIVRE
**BaseLIVRE** is a simple MVC base to a web form software made with Django and AdminLTE 3

### Features

+ Login,  register and recovery password
+ CRUD for Users and Groups
+ User active change password form
+ Templatetags: breadcrumbs, search field for lists
+ Bootstrap Pagination

## Install

### 1. Clone the project and adapt it to your needs

`$ git clone https://github.com/Tecnologia-Livre/baselivre.git`


### 2.  Change ENV file

Copy the .env.example file to a new .env file and change the data like the exemple below:

```
#DATABASE POSTGRESQL
DATABASE_NAME=tecnologialivre
DATABASE_USER=tecnologialivre
DATABASE_PASSWORD=tecnologialivre
DATABASE_HOST=db 
DATABASE_ROOT_PASSWORD=tecnologialivre
DATABASE_PORT=5432


#DJANGO
DJANGO_SECRET_KEY=
DJANGO_DEBUG=True
```

* DATABASE_NAME = name of your app database name

* DATABASE_USER = username of your database user (avoid use the admin postgres to manage your database with django)

* DATABASE_PASSWORD = password of the user

* DATABASE_HOST = the name of the PostgreSQL service in the docker-compose.yml file. Default is db.

* DATABASE_ROOT_PASSWORD = The admin postgres user password used by docker to start and config the database container. If you need to connect to this database as a admin, you need to use the user 'postgres' and this password.

* DATABASE_PORT = default port to PostgreSQL is 5432

* DJANGO_SECRET_KEY = to avoid some risks you can remove your DJANGO_SECRET_KEY from django settings ant put it here.

* DJANGO_DEBUG = for the devlopment environment is ok use TRUE here to know about the errors, but avoid to use it in production.

### 3. Run docker

`$ make start`

### 4. Create role (user) and database for your django application

1. Connect

Connect to the PostgresSQL server container using your favorite Database GUI manager. (If you don't have one, we recommend DBeaver Community Edition, it's free, user friendly and you can use it with a lot of others databases such MySQL, Firebird, etc).

DBeaver or another GUI will ask:

* Host: default is localhost
* Database: How it is your first connection you can use de 'postgres' default database
* Username: Again, for the first time use the 'posgres' user for the first connection
* Password: here you need to use the same password gave in DATABASE_ROOT_PASSWORD

2. Create role like you created in DATABASE_USER with permission to login and create databases

3. Refresh your connection

4. Create a database named as in DATABASE_NAME and set the role created above as its owner.

### 5. Run migrations

`$ make migrations`
`$ make migrate`

### 6. Create super user

`$ make superuser`

### 7. Login

Now you need to use your favorite browser to connet to the BaseLIVRE application with the url http://localhost/login

### 8. Have fun

## **Dev Advices**

###  [ *Broken code* ]

some times, your changes on the code can broke the system and even if you fix the problem the django can't run again the changes by it self, than you need to stop the container and start it again:

`$ make stop`
`$ make start`

### [ *Makefile* ]

Take a look at the Makefile to see all commands and understand what they exactly do. 

Fill free to make you owns commands automations.

### [ *Change the project name* ]

1. Rename the oldprojectname directory to newprojectname

1. manage.py: Change os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'oldprojectname.settings')

1. newprojectname/wsgi.py: Change os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'oldprojectname.settings')

1. newprojectname/settings.py: Change ROOT_URLCONF = 'oldprojectname.urls' and change WSGI_APPLICATION = 'oldprojectname.wsgi.application'

## Frameworks and libs

### 1. Backend
+ Django==3.1.7
+ django-adminlte3==0.1.6
+ django-seed==0.2.2
+ psycopg2==2.8.6
+ python-environ==0.4.54
+ django-crispy-forms==1.11.2

### 2. Frontend
+ Bootstrap-select v1.13.14
+ toastr v2.1.3
+ AdminLTE 3

### 3. DevOps
+ Python 3.6.12
+ PostgreSQL 12
+ Docker / Docker Compose
