#!/bin/bash

#reset tmux sessions
tmux kill-session -t portfolio

#cd into project
cd portfolio-project

#make sure /main is up to date
git fetch && git reset origin/main --hard

#go into virtual env && install dependencies
source python3-virtualenv/bin/activate
pip install -r requirements.txt

#Start new tmux session named "portfolio" && run flask
tmux new-session -d -s portfolio "flask run --host=0.0.0.0"

#Check if server is running
if [[ -n $(pgrep tmux) ]]; then
  echo "Tmux Server running successfully"
else
  echo "Tmux Server failed to run"
fi

