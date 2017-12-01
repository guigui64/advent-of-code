grid = [[] for _ in range(100)]
lines = [line.strip() for line in open("18.txt", "r").readlines()]
#grid = [[] for _ in range(6)]
#lines = [".#.#.#", "...##.", "#....#", "..#...", "#.#..#", "####.."]
for l in range(len(lines)):
    grid[l] = [c == '#' for c in lines[l]]

def get_state(l, c):
    if l not in range(len(grid)) or c not in range(len(grid[l])):
        return False
    return grid[l][c]

def next_state(l, c):
    # count neighbors on
    states = [get_state(lx, cx) for lx in range(l-1, l+2) for cx in range(c-1, c+2)]
    #print(states)
    count = sum(states)
    count -= get_state(l, c)
    if get_state(l, c):
        next = count == 2 or count == 3
    else:
        next = count == 3
    return next

def pprint():
    for line in grid:
        cline = ['#' if col else '.' for col in line]
        print(''.join(cline))

for step in range(100):
    pprint()
    print("Step", step+1)
    grid2 = [[] for _ in range(len(grid))]
    for l in range(len(grid)):
        grid2[l] = [next_state(l, c) for c in range(len(grid[l]))]
    grid = grid2

count = 0
for l in range(len(grid)):
    count += sum(grid[l][c] for c in range(len(grid[l])))
pprint()
print(count)
