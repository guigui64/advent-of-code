#!/usr/bin/python

f = open("01.txt", "r")
s = f.read()
i = 0
j = 0
position_found = False
for c in s:
    if c == '(':
        i = i + 1
    elif c == ')':
        i = i - 1
    j = j + 1
    if (not position_found) and (i == -1):
        print "Position =", j
        position_found = True
print "Floor =", i
