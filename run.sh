#!/bin/bash

source venv/bin/activate
pip install -r requirements.txt
export FLASK_APP=app/app.py
flask run
