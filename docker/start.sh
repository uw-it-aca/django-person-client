#!/bin/bash

echo "Waiting for postgres..."

while ! nc -z localhost 5432; do
  sleep 0.1
done

echo "PostgreSQL started"

python manage.py flush --no-input
python manage.py migrate
python manage.py runserver 0:$PORT
