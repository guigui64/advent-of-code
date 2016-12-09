# solution for http://adventofcode.com/2016/day/2

file  = open('02.txt', 'r')

x = 1 
y = 1
code = 0

for line in file.readlines() :
	for d in line :
		if   d == 'U' and y > 0 :
			y -= 1
		elif d == 'D' and y < 2 :
			y += 1
		elif d == 'R' and x < 2 :
			x += 1
		elif d == 'L' and x > 0 :
			x -= 1

	code = code*10 + (1 + x + y*3)

print code
