#! /bin/bash

python3 manage.py makemigrations --no-input

python3 manage.py migrate --no-input

python3 manage.py collectstatic --no-input

exec gunicorn WebOralia2.wsgi:application -b 0.0.0.0:8000 --reload
