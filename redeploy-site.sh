#!/bin/bash
tmux kill-session -a
cd portfolio
# make sure git repo in VPS has the latest changes from the main branch on GH
git fetch && git reset origin/main --hard
tmux new -d -s ta_portfolio
tmux send -t tal_portfolio 'python -m venv python3-virtualenv' ENTER
tmux send -t tal_portfolio 'pip3 install -r requirements.txt' ENTER
tmux send -t tal_portfolio 'flask run --host=0.0.0.0' ENTER
