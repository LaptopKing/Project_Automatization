#!/bin/bash

echo "Your path to the python file: "
var1=$(locate sajt.py)
echo $var1
echo
python "$var1"