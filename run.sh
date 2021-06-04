#!/bin/bash

source venv/bin/activate
pip install -r app/requirements.txt
export FLASK_APP=app/app.py
flask run
