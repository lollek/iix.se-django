#! /usr/bin/env bash

python manage.py collectstatic --noinput --settings iixse_django.settings_prod
uwsgi \
    --http 0:80 \
    --wsgi-file iixse_django/wsgi.py \
    --static-map /static/="${STATIC_ROOT}"
