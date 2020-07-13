#!/bin/bash

for var in $(ccrypt -d -c settings.env.cpt); do
	export "$var"
done
echo $var
python manage.py runserver
#python manage.py createsuperuser
