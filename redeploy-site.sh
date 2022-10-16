#!/bin/bash
cd portfolio
# make sure git repo in VPS has the latest changes from the main branch on GH
git fetch && git reset origin/main --hard
python -m venv python3-virtualenv
source python3-virtualenv/bin/activate
pip3 install -r requirements.txt
cd ..
cd /etc/systemd/system
systemctl daemon-reload
systemctl restart myportfolio
