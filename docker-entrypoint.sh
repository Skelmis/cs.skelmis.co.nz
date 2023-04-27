#!/bin/bash
python manage.py migrate
exec gunicorn cheatsheet_redirect.wsgi:application -c gunicorn.conf.py