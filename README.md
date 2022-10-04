# [VIMM]

## Loklane odpalenie aplikacji

1. Stwórz plik `.env`: `make env`
2. WYstartuj kontenery: `make up`
3. Dokonaj migracji do bazy danych: `make migrate`
4. Załaduj Ffixy: `make fix`
5. Aplikacja jest dostępna na `localhost:80`

## Komendy MAKE

Poniżej znajdziesz instrukcję jak zainstalować MAKE.

| KOMENDA | OPIS |
|-----------|-----------|
|**env**|`cp .env_example .env`|
|**up**|`docker-compose -f docker-compose.local.yml up -d`|
|**stop**|`docker-compose -f docker-compose.local.yml stop`|
|**build**|`docker-compose -f docker-compose.local.yml up --force-recreate --build`|
|**fix**|`docker exec -it name-app python manage.py loaddata core/fixtures/admin_user.json`|
|**migrate**|`docker exec -it name-app python manage.py migrate`|
|**migrations**|`docker exec -it name-app python manage.py makemigrations`|
|**app_shell**|`docker exec -it name-app bash`|
|**shell_plus**|`docker exec -it name-app python manage.py shell`|
|**test**|`docker exec -it name-app python manage.py test`|


## Development

### Pre-commit hooks

[Pre-commit](https://pre-commit.com/) runs automaticaly tools like mypy, black, isort to ensure code quality and PEP8 rules.

After cloning repository, run `pre-commit install` to install hooks.

### Makefile

> Make sure you have make installed.
>
> Ubuntu/Debian: `$ sudo apt-get install build-essential`
>
> Mac: `$ brew install make`
>
> Windows (as always, more complicated) https://stackoverflow.com/questions/32127524/how-to-install-and-use-make-in-windows

Makefile was created for convinient usage of all sorts of project related commands. Feel free to add some more, but remember to update README.

### Fixtures

Update admin data permission to admin panel in `core/fixtures/admin_user.json`, now it is deafult:

* login: test@email.pl
* password: test

> How to generate new hashed password? Make sure you have started container `$ make up`
>
> 1. Get in to shell django on container: `$ make shell_plus`
>
> 2. Import password generator: `$ from django.contrib.auth.hashers import make_password`
>
> 3. Encode your new password: `$make_password('test')`
> 4. Copy hased password and paste in fixture.
> 5. Call `$ exit()` to exit.