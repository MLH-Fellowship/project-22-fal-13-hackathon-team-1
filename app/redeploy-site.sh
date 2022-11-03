#!/bin/bash
cd project-22-fal-13-hackathon-team-1
# make sure git repo in VPS has the latest changes from the main branch on GH
git fetch && git reset origin/main --hard
source python3-virtualenv/bin/activate
pip3 install -r requirements.txt
systemctl restart myportfolio
