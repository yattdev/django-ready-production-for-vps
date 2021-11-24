#!/bin/sh

if [ "$DATABASE" = "postgres" ]
then
    echo "Waiting for postgres..."

    while ! nc -z $POSTGRES_HOST $POSTGRES_PORT; do
      sleep 0.1
    done

    echo "PostgreSQL started"
fi

# Some stuff when build done and postgres ready
python manage.py makemigrations --noinput --traceback
python manage.py migrate --noinput
python manage.py collectstatic -n --noinput --clean

exec "$@"
