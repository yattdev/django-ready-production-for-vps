#!/bin/sh

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

exec "$@"
