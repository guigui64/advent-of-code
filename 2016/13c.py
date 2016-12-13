favorite = 1362

def open(x, y):
    formula = x*x + 3*x + 2*x*y + y + y*y + favorite
    return bin(formula).count('1',2) % 2 == 0

visited = set()

    def next_nodes(current):
    ret = []
    for spot in current:
        x, y = spot
        if x != 0:
            if (x - 1, y) not in visited and open(x - 1, y):
                visited.add(tuple([x - 1, y]))
                ret.append(tuple([x - 1, y]))
        if y != 0:
            if (x, y - 1) not in visited and open(x, y - 1):
                visited.add(tuple([x, y - 1]))
                ret.append(tuple([x, y - 1]))
        if (x + 1, y) not in visited and open(x + 1, y):
            visited.add(tuple([x + 1, y]))
            ret.append(tuple([x + 1, y]))
        if (x, y + 1) not in visited and open(x, y + 1):
            visited.add(tuple([x, y + 1]))
            ret.append(tuple([x, y + 1]))
    return ret


steps = 0
p2 = 0
here = [(1, 1)]
while (31, 39) not in here:
    steps += 1
    here = next_nodes(here)
    if steps == 50:
        p2 = len(visited)
print "Part 1:", steps
print "Part 2:", p2
