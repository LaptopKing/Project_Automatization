#!/bin/bash

sudo apt install python3
sudo apt install python3.7
clear
var2="https://raw.githubusercontent.com/LaptopKing/Project_Automatization/main/Project%20Automatization/startup_script.py"
wget -q -O - "$var2" | python3