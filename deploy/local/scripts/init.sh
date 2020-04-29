#!/bin/bash

echo `whoami`
echo `pwd`

apt-get update -y
apt-get install python3-pip rabbitmq-server -y
systemctl start rabbitmq-server
python3 -m pip install --upgrade pip
python3 -m pip install -r /var/www/requirements.txt --user



echo `whoami`
echo `pwd`