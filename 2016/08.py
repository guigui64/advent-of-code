def printgrid(g):
    for l in g:
        line = "".join(l)
        print line

f = open("08.txt", "r")

grid = [['.']*50 for x in range(6)]
printgrid(grid)

for line in f.readlines():
    if "rect" in line:
        width, height = [int(x) for x in line.split("rect ")[1].split("x")]
        for h in range(height):
            for w in range(width):
                grid[h][w] = '#'
    elif "rotate" in line:
        cr, length = [int(x) for x in line.split("=")[1].split(" by ")]
        for l in range(length):
            if "row" in line:
                store = grid[cr][-1]
                for c in range(len(grid[cr])):
                    tmp = grid[cr][c]
                    grid[cr][c] = store
                    store = tmp
            elif "column" in line:
                store = grid[-1][cr]
                for r in range(len(grid)):
                    tmp = grid[r][cr]
                    grid[r][cr] = store
                    store = tmp
    print line[:-1]
    printgrid(grid)

count = 0
for gr in grid:
    for g in gr:
        if g == '#':
            count += 1
print count
