#!/bin/bash

mkdir ~/neo
cp infofetch.py ~/neo
cp ubuntu.logo ~/neo
cp ubuntu.txt ~/neo
cp ~/.bashrc ~/.bashrc.org
echo "alias neo='python3 ~/neo/infofetch.py'" >>~/.bashrc
source ~/.bashrc
python3 ~/neo/infofetch.py
