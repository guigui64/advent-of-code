#!/usr/bin/python

def area(sizes):
    return 2*sizes[0]*sizes[1] + 2*sizes[1]*sizes[2] + 2*sizes[0]*sizes[2] + sizes[0]*sizes[1]

def length(sizes):
    return sizes[0]*2 + sizes[1]*2 + sizes[0]*sizes[1]*sizes[2]

f = open("02.txt", "r")

total_area = 0
total_length = 0
for line in f:
    sizes = [int(i) for i in line.split("x")]
    sizes.sort()
    total_area += area(sizes)
    total_length += length(sizes)

f.close()

print "Total area   =", total_area
print "Total length =", total_length
