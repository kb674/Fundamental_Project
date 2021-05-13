#!/bin/bash

#install python, virtual env and pip, needed for selenium 
sudo apt update
sudo apt install python3
sudo apt install python3-venv
sudo apt install python3-pip

sudo apt install chromium-browser -y



# add and activate virtual environment
python3 -m venv env
source env/bin/activate
pip3 install -r requirements.txt

# configure variables
export DATABASE_URI
export SECRET_KEY

# run pytest
python3 -m pytest --doctest-modules --junitxml=junit/test-results.xml --cov=application --cov-report=xml --cov-report=html