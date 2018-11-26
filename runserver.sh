#!/bin/sh

set -a; . /home/SeniorDesign/.env; set +a
python3 ./manage.py runserver 0.0.0.0:8000
