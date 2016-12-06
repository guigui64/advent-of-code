#!/usr/bin/python

f = open("03.txt", "r")

robotsturn = False
x = 0
y = 0
robotx = 0
roboty = 0
positions = [[0,0]]

for c in f.read():
    if robotsturn:
        if   c == '>': robotx = robotx + 1
        elif c == '<': robotx = robotx - 1
        elif c == 'v': roboty = roboty - 1
        elif c == '^': roboty = roboty + 1

        if [robotx,roboty] not in positions:
             positions = positions + [[robotx,roboty]]
    else:
        if   c == '>': x = x + 1
        elif c == '<': x = x - 1
        elif c == 'v': y = y - 1
        elif c == '^': y = y + 1

        if [x,y] not in positions:
            positions = positions + [[x,y]]

    robotsturn = not robotsturn

print len(positions)
