#!/bin/sh

if [ "$DATABASE" = "postgres" ]
then
    echo "Waiting for postgres..."

    while ! nc -z $SQL_HOST $SQL_PORT; do
      sleep 0.1
    done

    echo "PostgreSQL started"
fi

# Update database with migrate
python manage.py migrate --noinput --traceback

# Run test with test
# python manage.py test --noinput --traceback

exec "$@"
