#!/bin/sh

python3 /usr/src/app/ceiphr_proj/manage.py runserver 0.0.0.0:8000
python3 /usr/src/app/ceiphr_proj/manage.py makemigrations
python3 /usr/src/app/ceiphr_proj/manage.py migrate
python3 /usr/src/app/ceiphr_proj/manage.py collectstatic --noinput --clear
