#!/bin/bash


if [ -z "$1" ]; then
	echo -e "no arguments !!!"
	echo -e "usage 1: ./django_handler.sh startapp [app_name]"
	echo -e "usage 2: ./django_handler.sh makemigrations"
	echo -e "usage 3: ./django_handler.sh migrate"
	echo -e "usage 4: ./django_handler.sh runserver"
	exit
fi

if [ "$1" == "help" ] || [ "$1" == "-h" ]; then
	echo -e "usage 1: ./django_handler.sh startapp [app_name]"
	echo -e "usage 2: ./django_handler.sh makemigrations"
	echo -e "usage 3: ./django_handler.sh migrate"
	echo -e "usage 4: ./django_handler.sh runserver"
	exit
fi

python3 manage.py $1 $2
