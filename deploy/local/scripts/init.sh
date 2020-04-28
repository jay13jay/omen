#!/bin/bash

echo `whoami`
echo `pwd`

sudo apt-get update -y
sudo apt-get install python3-pip -y
pip3 install -r requirements.txt --user

echo `whoami`
echo `pwd`