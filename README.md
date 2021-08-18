# [APP NAME]

## Running app locally

1. Create `.env` file: `make env`
2. Run containers: `make up`
3. Migrate existing migrations: `make migrate`
4. Upload fixtures: `make fix`
5. App is now available on `localhost:8000`

## Make commands
| COMMAND | DESCRIPTION |
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

## Git flow

Branch `main` is the branch that reflects what is currently production code.

Branch `staging` is the main branch and all pull requests should be compared with this branch.

For new features we use feature branches and their names should be copied from Clickup.

When PR is open, contributor is responsible for assigning reviewers, resolving conflicts, merging after at least one approval from reviewers. When merging use `Squash and merge` and delete branch after successful merge.

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