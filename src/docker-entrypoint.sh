#!/bin/sh

flask db init
flask db migrate
flask db upgrade
python src/script_db.py
flask run