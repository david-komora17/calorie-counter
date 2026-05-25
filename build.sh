#!/usr/bin/env bash
# exit on error
set -o errexit

echo "Installing project dependencies..."
pip install -r requirements.txt

echo "Collecting modern static assets..."
python manage.py collectstatic --no-input

echo "Running target schema migrations..."
python manage.py migrate

echo "Build phase pipeline successfully initialized!"