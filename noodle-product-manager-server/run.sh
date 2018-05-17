#!/bin/bash
export FLASK_APP=noodle
#export FLASK_ENV=development
export DB_URL='localhost:3306'
export DB_NAME='noodle_coding_challenge'
export DB_USER='noodle_user'
export DB_PASSWORD='REDACTED'
source $(pipenv --venv)/bin/activate
flask run -h 0.0.0.0
