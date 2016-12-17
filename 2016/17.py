from hashlib import md5
from collections import defaultdict

def open_doors(to_hash):
    return [c in open for c in md5(to_hash.encode()).hexdigest()]

def invalid_directions(position):
    invalid = []
    x, y = position
    if x == 0:
        invalid.append('L')
    elif x == 3:
        invalid.append('R')
    if y == 0:
        invalid.append('U')
    elif y == 3:
        invalid.append('D')
    return invalid

def next_position(position, direction):
    x, y = position
    if direction == 'U':
        y -= 1
    elif direction == 'D':
        y += 1
    elif direction == 'L':
        x -= 1
    else: # 'R'
        x += 1
    return (x, y)

def next_nodes(node):
    position, path = node
    nodes = set()
    x, y = position
    od = open_doors(input + path)
    inv = invalid_directions(position)
    for d in [di for di in directions if di not in inv]:
        if od[directions[d]]:
            nodes.add((next_position(position, d), path + d))
    return nodes

def solve(node, best_path="FIRST", worst_path=""):
    pos, path = node
    if pos == vault:
        if best_path == "FIRST":
            best_path = path
        elif len(path) < len(best_path):
            best_path = path
        if len(path) > len(worst_path):
            worst_path = path
    else:
        for n in next_nodes(node):
            best_path, worst_path = solve(n, best_path, worst_path)
    return best_path, worst_path

# main
if __name__ == '__main__':

    input = "hhhxzeay"

    open = "bcdef"
    directions = {'U' : 0, 'D' : 1, 'L' : 2, 'R' : 3}

    # goal
    vault = (3, 3)

    # start
    node = ((0, 0), '')

    # solve
    best, worst = solve(node)
    print(best)
    print(len(worst))
