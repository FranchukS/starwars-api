#!/bin/sh

while !</dev/tcp/swapi_db/5432;
do
    echo waiting for Postgres to start...;
    sleep 3;
done;

python manage.py migrate
make load_data


python manage.py runserver 0.0.0.0:8000
