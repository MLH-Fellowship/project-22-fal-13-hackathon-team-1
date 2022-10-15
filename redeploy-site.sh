#!/bin/bash

#cd into project
cd portfolio-project

#make sure /main is up to date
git fetch && git reset origin/main --hard

#go into virtual env && install dependencies
source python3-virtualenv/bin/activate
pip install -r requirements.txt

#ensure SQL DB is working
sudo systemctl start mysqld.service
sudo systemctl enable mysqld

#restart myportfolio systemd service
        #located at /etc/systemd/system/myportfolio.service
systemctl start myportfolio
systemctl enable myportfolio

#show status of myportfolio `start`
systemctl status myportfolio

