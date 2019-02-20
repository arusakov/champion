#!/usr/bin/env bash

cd /usr/local/champion
exec env/bin/gunicorn champion.wsgi -c deploy/gunicorn.conf.py
