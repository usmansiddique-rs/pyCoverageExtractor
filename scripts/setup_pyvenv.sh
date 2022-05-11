#!/bin/bash

# check if pip package virtualenv is installed or not
CHECK1=$(virtualenv --version)
CHECK1=$(echo $CHECK1 | awk '{print $1}')

if [[ $CHECK1 = 'virtualenv' ]]
then
    echo -e "PIP package virtualenv INSTALLED. \n"
else
    echo -e "INSTALLING PIP package virtualenv"
    python3 -m pip install virtualenv
fi

# create virtual env
virtualenv .pyvenv
source .pyvenv/bin/activate
pip install --upgrade pip
echo -e "\n"
pip list
echo -e "\n"
python3 -m pip install -r requirements.txt
echo -e "\n"
pip list
echo -e "\n"