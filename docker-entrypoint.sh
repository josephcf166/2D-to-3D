#!/bin/bash

ls -al

# Collect static files
echo "Collect static files"
python /code/app/manage.py collectstatic --noinput

# Apply database migrations
echo "Apply database migrations"
python /code/app/manage.py migrate

# Start server
echo "Starting server"
python /code/app/manage.py runserver 0.0.0.0:8000
