#!/bin/bash

for var in $(ccrypt -d -c settings.env.cpt); do
	export "$var"
done
python manage.py runserver 0.0.0.0:8080
#python manage.py createsuperuser
