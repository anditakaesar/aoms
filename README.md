# aoms
Web Development Test using Django

## Requirements
  - Django ^1.11
  - Database of your choice

## Run
  - make a separate setting file `aoms\local_settings.py` that contains
    `SECRET_KEY` and `DATABASES` settings
  - Make migration
    run `python manage.py makemigrations`
  - Migrate to database
    run `python manage.py migrate`
  - Migrate admin page
  - For Testing, run in local server
    run `python manage.py runserver 8999` or whatever you like (port)

## License
MIT
