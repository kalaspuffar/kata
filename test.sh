#!/bin/bash
while :
do
inotifywait -e modify *.py
python -m doctest *.py
done
