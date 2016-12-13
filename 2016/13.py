from heapq import *

favorite = 1362

def is_wall(x, y):
    formula = (x+3)*x + 2*x*y + (y+1)*y + favorite
    return bin(formula).count('1',2) % 2 == 1

def best_first_search(init, victory, score, valid_moves):
    best = 99999999999999999999999999999999999999
    queue = []
    heappush(queue, (0, init))

    while len(queue) > 0:
        _, state = heappop(queue)

        # victory() is a function that return (bool, int)
        reached, moves = victory(state)
        if reached:
            print("Success @", moves)
            if moves < best:
                best = moves
                continue

        # valid_moves generates adjacent states
        for move in valid_moves(state):
            # score prioritizes states (lower is better)
            sc = score(move)
            heappush(queue, (sc, move))

    return best

def victory(state):
    x,y,m = state
    if (x,y) == (31,39):
        return (True, m)
    return (False, None)

def score(state):
    x,y,_ = state
    return abs(31 - x) + abs(39 - y)

visited = set()
# walls = 0

def valid_moves(state):
    global walls

    x,y,m = state

    for dx, dy in [(1,0), (0,1), (-1,0), (0,-1)]:
        nx = x + dx
        ny = y + dy

        if nx < 0 or ny < 0:
            continue

        if (nx, ny) in visited:
            continue

        visited.add((nx,ny))

        if is_wall(nx, ny):
            # walls += 1
            continue

        yield (nx, ny, m + 1)

print(best_first_search((1,1,0), victory, score, valid_moves))
