#!/bin/bash

echo "Waiting for postgres..."

while ! nc -z $SQL_HOST $SQL_PORT; do
    sleep 0.1
done

echo "PostgreSQL started"

source "/app/bin/activate"

if [ "$ENV"  = "localdev" ]
then

  python manage.py migrate
  #python manage.py loaddata person.json employee.json term.json major.json student.json adviser.json transfer.json transcript.json hold.json sport.json

fi
