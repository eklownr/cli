#!/bin/bash

mkdir ~/neo
cp infofetch.py ~/neo
echo "alias neo='~/neo/infofetch.py'" >>~/.bashrc
source ~/.bashrc
python3 ~/neo/infofetch.py
