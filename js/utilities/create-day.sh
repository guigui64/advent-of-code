#!/bin/bash

if [[ $# < 3 ]] ; then
  echo "Usage: $0 [--aoc-only|--page-only] year day title"
  exit -1
fi

if [[ $1 == "--aoc-only" ]] ; then
  aocOnly="true"
  shift
elif [[ $1 == "--page-only" ]] ; then
  pageOnly="true"
  shift
fi

year=$1
day=$2
title="$3"

if [ ! -d pages ] ; then
  echo "$0 must be launched in the root folder (the one containing pages/)"
  exit -1
fi

pageTarget="pages/$year-$day.js"
aocTarget="aoc/$year-$day.js"
aocTestTarget="aoc/$year-$day.test.js"

if [[ $pageOnly != "true" ]] ; then
  if [ -e $aocTarget ] ; then
    echo "$aocTarget already exists"
  else
    cp `dirname $0`/aoc.template $aocTarget
    sed -i 's/#year#/'$year'/ ; s/#day#/'$day'/ ; s/#title#/'"$title"'/' $aocTarget
    echo "$aocTarget generated"
  fi
  if [ -e $aocTestTarget ] ; then
    echo "$aocTestTarget already exists"
  else
    cp `dirname $0`/aoc.test.template $aocTestTarget
    sed -i 's/#year#/'$year'/ ; s/#day#/'$day'/ ; s/#title#/'"$title"'/' $aocTestTarget
    echo "$aocTestTarget generated"
  fi
fi

if [[ $aocOnly != "true" ]] ; then
  if [ -e $pageTarget ] ; then
    echo "$pageTarget already exists"
  else
    cp `dirname $0`/day.template $pageTarget
    sed -i 's/#year#/'$year'/ ; s/#day#/'$day'/ ; s/#title#/'"$title"'/' $pageTarget
    echo "$pageTarget generated"
  fi
fi
exit 0
