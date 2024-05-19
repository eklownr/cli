#!/bin/bash

mkdir ~/neo
cp infofetch.py ~/neo
cp ubuntu.logo ~/neo
cp ~/.bashrc ~/.bashrc.org
echo "alias neo='python3 ~/neo/infofetch.py'" >>~/.bashrc
source ~/.bashrc
python3 ~/neo/infofetch.py
