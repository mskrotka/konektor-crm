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

### MAKE

Make sure you have make installed.
Ubuntu/Debian: `$ sudo apt-get install build-essential`
Mac: `$ brew install make`
Windows: https://stackoverflow.com/questions/32127524/how-to-install-and-use-make-in-windows

Makefile został stworzony w celu wygodnego korzystania z wszelkiego rodzaju poleceń związanych z projektem. Możesz dodać więcej, ale pamiętaj o aktualizacji README.

### Fixtures

Załaduj przykładowe dane oraz konto administratora `core/fixtures/admin_user.json`, dane logowania to:

* login: test@email.pl
* password: test

Jak wygenerować własne hasło do fixów? Bądź pewny, że kontenery są odpalone `$ make up`

1. Wejdź do kontenera z Django: `$ make shell_plus`
2. Zaimportuj generator haseł: `$ from django.contrib.auth.hashers import make_password`
3. Zakoduj swoje hasło: `$ make_password('test')`
4. Skopiuj do fixtur.
5. Wywołaj `$ exit()` aby wyjść.