# aoms
Web Development Test using Django. The reason this application is developed is
to aid business process of pre-order based store.

## Application Rundown
  - API, by using Django Framework
  - Clients by using web, desktop and mobile version. It is possible to use web
    in mobile version, but it will be hard to make the web version responsive to
    any kind of features.

## Requirements
  - Django ^1.11
  - Database of your choice

## Run
  - make a separate setting file `aoms\local_settings.py` that contains
    `SECRET_KEY` and `DATABASES` settings. You can rename the file
    `aoms\local_settings.temp` into `aoms\local_settings.py`.
  - Make migration
    run `python manage.py makemigrations`
  - Migrate to database
    run `python manage.py migrate`
  - Migrate admin page
  - For Testing, run in local server
    run `python manage.py runserver 8999` or whatever you like (port)

## License
MIT
