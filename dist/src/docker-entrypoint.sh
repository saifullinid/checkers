#!/bin/sh

flask db init
flask db migrate
flask db upgrade
python src/script_db.py
flask run --host=0.0.0.0 --port=8000