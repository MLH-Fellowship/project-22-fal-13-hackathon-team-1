#!/bin/bash

#reset tmux sessions
tmux kill-server

#cd into project
cd portfolio-project

#make sure /main is up to date
git fetch && git reset origin/main --hard

#Start new tmux session named "portfolio-deployed"
tmux new -d -s portfolio

#go into virtual env && install dependencies
tmux send-keys -t portfolio "source python3-virtualenv/bin/activate" C-m
tmux send-keys -t portfolio "pip install -r requirements.txt" C-m

#start flask server
tmux send-keys -t portfolio "flask run --host=0.0.0.0" C-m

#tmux detach
tmux send-keys -t portfolio "tmux detach" C-m

#Check if server is running
if [[ -n $(pgrep tmux) ]]; then
  echo "Tmux Server running successfully"
else
  echo "Tmux Server failed to run"
fi