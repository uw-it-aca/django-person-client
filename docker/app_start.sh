#!/bin/bash

echo "Waiting for postgres..."

while ! nc -z $POSTGRES_HOST $POSTGRES_PORT; do
    sleep 0.1
done

echo "PostgreSQL started"

source "/app/bin/activate"

if [ "$ENV"  = "localdev" ]
then

  python manage.py migrate

fi
