# solution for http://adventofcode.com/2016/day/1

import sys

file  = open('01.txt', 'r')
input = file.readline()

up    = 0
right = 0

N = 0
E = 1
S = 2
W = 3

orientation = N

locations = []

for direction in input.split(', '):
	if direction[0] == 'R' :
		orientation = (orientation + 1) % 4
	else :	
		orientation = (orientation + 4 - 1) % 4

	count = int(direction[1:])

	for i in range(count) :
		if orientation == N :
			up += 1
		elif orientation == E :
			right += 1
		elif orientation == S :
			up -= 1
		else :
			right -= 1

		for location in locations :
			if location[0] == up and location[1] == right:
				print (abs(up) + abs(right))
				sys.exit(0)

		locations = [[up, right]] + locations
