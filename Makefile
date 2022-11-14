env:
	cp .env_example .env

up:
	docker-compose -f docker-compose.local.yml up -d

stop:
	docker-compose -f docker-compose.local.yml stop

build:
	docker-compose -f docker-compose.local.yml up -d --force-recreate --build

fix:
	docker exec -it name-app python manage.py loaddata core/fixtures/admin_user.json

migrate:
	docker exec -it name-app python manage.py migrate

migrations:
	docker exec -it name-app python manage.py makemigrations

app_shell:
	docker exec -it name-app bash

shell_plus:
	docker exec -it name-app python manage.py shell

test:
	docker exec -it name-app python manage.py test