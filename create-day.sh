#!/bin/bash

[[ $# < 2 ]] && echo "Usage $0 YEAR DAY" && exit 1

YEAR=$1
DAY=$2

[[ -d $YEAR/$DAY ]] && echo "$YEAR/$DAY already exists, delete it if you want to re-create it" && exit 1

mkdir -v --parents $YEAR/$DAY
cp -v aoc.template.py $YEAR/$DAY/$DAY.py

