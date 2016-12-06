#!/usr/bin/python

f = open("03.txt", "r")

x = 0
y = 0
positions = [[0,0]]

for c in f.read():
    if   c == '>': x = x + 1
    elif c == '<': x = x - 1
    elif c == 'v': y = y - 1
    elif c == '^': y = y + 1

    if [x,y] not in positions:
        positions = positions + [[x,y]]

print len(positions)
