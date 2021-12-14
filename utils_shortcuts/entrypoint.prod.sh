#!/bin/sh

if [ "$DATABASE" = "postgres" ]
then
    echo "Waiting for postgres..."

    while ! nc -z $SQL_HOST $SQL_PORT; do
      sleep 0.1
    done

    echo "PostgreSQL started"
fi

# Following statements will be run just once time, that's container startup
CONTAINER_ALREADY_STARTED=".CONTAINER_ALREADY_STARTED_PLACEHOLDER"
if [ ! -e $CONTAINER_ALREADY_STARTED ]; then
    echo "-- First container startup --"
    # Update database with migrate
    python manage.py migrate --noinput --traceback

    # Run test with test
    python manage.py test --noinput --traceback

    # Run collectstatic with collectstatic
    python manage.py collectstatic --noinput --traceback

    # --------
    touch $CONTAINER_ALREADY_STARTED
else
    echo "-- Not first container startup --"
fi

exec "$@"
