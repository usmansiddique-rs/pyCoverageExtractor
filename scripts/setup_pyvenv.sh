#!/bin/bash

python3 -m venv .pyvenv
source .pyvenv/bin/activate
pip install --upgrade pip
echo -e "\n"
pip list
echo -e "\n"
python3 -m pip install -r requirements.txt
echo -e "\n"
pip list
