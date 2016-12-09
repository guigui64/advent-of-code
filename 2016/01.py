# solution for http://adventofcode.com/2016/day/1

file  = open('01.txt', 'r')
input = file.readline()

up    = 0
right = 0

N = 0
E = 1
S = 2
W = 3

orientation = N

for direction in input.split(', '):
	if direction[0] == 'R' :
		orientation = (orientation + 1) % 4
	else :	
		orientation = (orientation + 4 - 1) % 4

	count = int(direction[1:])

	if orientation == N :
		up += count
	elif orientation == E :
		right += count
	elif orientation == S :
		up -= count
	else :
		right -= count

print (abs(up) + abs(right))