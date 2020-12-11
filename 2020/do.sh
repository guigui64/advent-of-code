#!/bin/bash
day=$1
ls $day | entr bash -c "time python $day"
