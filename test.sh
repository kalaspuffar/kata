#!/bin/bash
while :
do
inotifywait -e modify -r .
composer exec kahlan
done
