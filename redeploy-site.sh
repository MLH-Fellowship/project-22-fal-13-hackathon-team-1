#!/bin/bash
tmux kill-session -t ta_portfolio
cd portfolio
# make sure git repo in VPS has the latest changes from the main branch on GH
git fetch && git reset origin/main --hard
python -m venv python3-virtualenv
source python3-virtualenv/bin/activate
pip3 install -r requirements.txt
tmux new-session -d -s ta_portfolio 'flask run --host=0.0.0.0'
