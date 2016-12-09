# solution for http://adventofcode.com/2016/day/2

file  = open('02.txt', 'r')

pos  = 10


right = [6,7,10,11,12,13,16,17]
left  = [7,8,11,12,13,14,17,18]
up    = [7,11,12,13,16,17,18,22]
down  = [2,6,7,8,11,12,13,17]

codes  = [
' ', ' ', '1', ' ', ' ',
' ', '2', '3', '4', ' ',
'5', '6', '7', '8', '9',
' ', 'A', 'B', 'C', ' ',
' ', ' ', 'D', ' ', ' ']
answer = ''

for line in file.readlines() :
	for d in line :
		if   d == 'U' and (pos in up) :
			pos -= 5
		elif d == 'D' and (pos in down) :
			pos += 5
		elif d == 'R' and (pos in right) :
			pos += 1
		elif d == 'L' and (pos in left) :
			pos -= 1

	answer += codes[pos]

print answer
