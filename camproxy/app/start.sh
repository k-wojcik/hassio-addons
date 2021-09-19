#!/usr/bin/with-contenv bashio

echo Starting server
gunicorn --bind 0.0.0.0:5445 main:app
