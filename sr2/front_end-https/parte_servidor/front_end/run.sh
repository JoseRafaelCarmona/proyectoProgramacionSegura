#!/bin/bash

export REQUEST_CA_BUNDLE=/tmp/servicios_cert.crt

sleep 15

su -c 'python3 -u manage.py makemigrations' user
su -c 'python3 -u manage.py migrate' user
su -c 'gunicorn --bind :8000 front_end.wsgi:application --reload'
