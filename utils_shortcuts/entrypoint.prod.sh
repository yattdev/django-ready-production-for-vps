#!/bin/sh

# This variable is to define first startup
CONTAINER_ALREADY_STARTED=".CONTAINER_ALREADY_STARTED_PLACEHOLDER"

if [ "$DATABASE" = "postgres" ]
then
    echo "Waiting for postgres..."

    if ! nc -z $SQL_HOST $SQL_PORT; then
        echo "Delete file:" $CONTAINER_ALREADY_STARTED
        rm -f .CONTAINER_ALREADY_STARTED_PLACEHOLDER
    fi
    sleep 1

    while ! nc -z $SQL_HOST $SQL_PORT; do
      sleep 0.1
    done

    echo "PostgreSQL started"
    sleep 1
fi

# Following statements will be run just once time, that's container startup
if [ ! -e $CONTAINER_ALREADY_STARTED ]; then
    echo "-- First container startup --"
    # Update database with migrate
    python manage.py migrate --noinput --traceback && sleep 1

    # Run test with test
    # python manage.py test --noinput --traceback && sleep 1

    # Run collectstatic with collectstatic
    python manage.py collectstatic --noinput --traceback && sleep 1

    # --------
    touch $CONTAINER_ALREADY_STARTED
else
    echo "-- Not first container startup --"
fi

exec "$@"
