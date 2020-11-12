#!/bin/bash

# url = "https://raw.githubusercontent.com/LaptopKing/Project_Automatization/main/Project%20Automatization/startup_script.py"
# wget -q $url

var1=$(find startup_script.py)
python3 "$var1"
