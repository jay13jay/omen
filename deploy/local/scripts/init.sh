#!/bin/bash

echo `whoami`
echo `pwd`

sudo apt-get update -y
sudo apt-get install python3-pip -y
python3 -m pip install --upgrade pip
python3 -m pip install -r /var/www/requirements.txt --user

echo `whoami`
echo `pwd`