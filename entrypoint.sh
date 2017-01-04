#!/usr/bin/env bash

python /usr/src/app/manage.py migrate
python /usr/src/app/manage.py collectstatic --noinput

uwsgi --ini /usr/src/app/caldav2ical/uwsgi.ini
