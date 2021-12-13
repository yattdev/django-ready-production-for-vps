#!/bin/sh

if [ "$DATABASE" = "postgres" ]
then
    echo "Waiting for postgres..."

    while ! nc -z $SQL_HOST $SQL_PORT; do
      sleep 0.1
    done
    echo "PostgreSQL started"

fi

# This condition if juste to run following on container startup
if ! $INITIALIZE
then
    # Update database with migrate
    python manage.py migrate --noinput --traceback

    # Run test with test
    python manage.py test --noinput --traceback

    # Collectstatic files with collectstatic command
    python manage.py collectstatic --noinput --traceback

    export INITIALIZE="DONE"
fi

exec "$@"
