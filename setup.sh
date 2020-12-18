#!/bin/bash

# installs upower utility if is not already present
sudo apt install upower

# give permission to binary file
chmod +x ./dist/bat-draw 

# copy binary to user path
sudo cp ./dist/bat-draw /usr/local/bin/