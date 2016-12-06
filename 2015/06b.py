f = open("06.txt", "r")

grid = [[0]*1000 for i in range(1000)]

for line in f.readlines():
    # determine action and positions
    split = line[:-1].rsplit(" ", 3)
    action = split[0]
    start = [int(s) for s in split[1].split(",")]
    end   = [int(s) for s in split[3].split(",")]
    # act
    for x in range(start[0], end[0]+1):
        for y in range(start[1], end[1]+1):
            if   action == "turn on":
                grid[x][y] += 1
            elif action == "turn off":
                grid[x][y] -= 1
                if grid[x][y] < 0: grid[x][y] = 0
            else: # toggle
                grid[x][y] += 2

# count lights on
sum = 0
for gridline in grid:
    for light in gridline:
        sum += light
print sum
