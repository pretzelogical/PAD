#!/usr/bin/env bash
# Migrates django database from one version to another

python manage.py makemigrations
python manage.py migrate
