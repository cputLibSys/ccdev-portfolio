#!/usr/bin/sh

export DJANGO_SUPERUSER_EMAIL=cadetcyuzuzo@gmail.com
export DJANGO_SUPERUSER_PASSWORD=0785610104

echo "Installing the latest version of poetry..."

pip install --upgrade pip

pip install poetry==1.2.0

rm poetry.lock

poetry lock

python -m poetry install
pip install dj-database-url
pip install django-jquery
pip install django-bootstrap-v5
pip install psycopg2

rm -rf staticfiles

python manage.py collectstatic --no-input
