#!/bin/bash

[[ $# < 2 ]] && echo "Usage $0 YEAR DAY" && exit 1

YEAR=$1
DAY=$2

find $YEAR/$DAY | entr bash -c 'time python3.6 '$YEAR/$DAY/$DAY'.py'

