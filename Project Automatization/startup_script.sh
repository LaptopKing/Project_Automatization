#!/bin/bash

var2="https://raw.githubusercontent.com/LaptopKing/Project_Automatization/main/Project%20Automatization/startup_script.py"
wget -q "$var2"

var1=$(find startup_script.py)
python3 "$var1"
