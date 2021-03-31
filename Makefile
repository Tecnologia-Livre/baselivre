build:
		docker-compose build

rebuild:
		docker-compose build --no-cache

migrations:
		docker-compose run web python ./manage.py makemigrations

migrate:
		docker-compose run web python ./manage.py migrate

migrate-fake:
		docker-compose run web python ./manage.py migrate --fake

showmigrations:
		docker-compose run web python ./manage.py showmigrations

superuser:
		docker-compose run web python ./manage.py createsuperuser

shell:
		docker-compose run web python ./manage.py shell

bash:
		docker-compose run web bash

start:
		docker-compose up -d

vstart:
		docker-compose up	

stop:
		docker-compose stop

down: 
		docker-compose down