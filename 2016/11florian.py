from itertools import combinations
from sets import ImmutableSet
from collections import defaultdict

getother = lambda e: e+10 if e < E else e-10
isGen = lambda e: e < E
isChip = lambda e: e > E
isElevator = lambda e: e == E

def hasgen(floor):
    for e in floor:
        if isGen(e): return True
    return False

def isvalid(floor):
    if hasgen(floor):
        for c in filter(isChip, floor):
            if not getother(c) in floor:
                return False
        return True
    else:
        return True

def newfloors(floors, newfloor1, elevator1, newfloor2, elevator2):
    nfloors = []
    for i, floor in enumerate(floors):
        if i == elevator1:
            nfloors.append(newfloor1)
        elif i == elevator2:
            nfloors.append(newfloor2)
        else:
            nfloors.append(floors[i])
    return tuple(nfloors)

def getnstates(state, neighbors):
    elevator = state[0]
    floors = state[1]
    nstates = []
    for f in neighbors[elevator]:
        for c in combinations(floors[elevator], 2):
            nfloor = floors[f] | ImmutableSet(c)
            if isvalid(nfloor):
                nfloors = newfloors(floors, nfloor, f, floors[elevator] - ImmutableSet(c), elevator)
                nstates.append((f, nfloors))
        for e in floors[elevator]:
            nfloor = floors[f] | ImmutableSet([e])
            if isvalid(nfloor):
                nfloors = newfloors(floors, nfloor, f, floors[elevator] - ImmutableSet([e]), elevator)
                nstates.append((f, nfloors))
    return nstates

def bfs(root, neighbors, idx):
    parent = defaultdict()
    parent[root] = None
    visited = [root]
    queue = [root]
    while queue:
        current = queue.pop(0)
        for n in getnstates(current, neighbors):
            if n not in visited:
                visited.append(n)
                parent[n] = current
                if not n[1][idx]:
                    p = parent[n]
                    count = 0
                    while p:
                        count += 1
                        p = parent[p]
                    return count, n
                queue.append(n)

SG = 1
PG = 2
TG = 3
RG = 4
CG = 5

SM = 11
PM = 12
TM = 13
RM = 14
CM = 15

TmG = 1
PuG = 2
SrG = 3
PmG = 4
RuG = 5
ElG = 6
DlG = 7

E = 8

TmM = 11
PuM = 12
SrM = 13
PmM = 14
RuM = 15
ElM = 16
DlM = 17

F0 = 0
F1 = 1
F2 = 2
F3 = 3

##### PART1 #######

root1 = (F0, (ImmutableSet([TmG, TmM, PuG, SrG]),      # 0
             ImmutableSet([PuM, SrM]),                 # 1
             ImmutableSet([PmG, PmM, RuG, RuM]),       # 2
             ImmutableSet([])))                        # 3

root1 = (F0, (ImmutableSet([SG, SM, PG, PG]),      # 0
             ImmutableSet([TG, RG, RM, CG, CM]),                 # 1
             ImmutableSet([TM]),       # 2
             ImmutableSet([])))                        # 3

neighbors1 = [[1],    #0
              [0],    #1
             [3],    #2
             [2]]    #3

neighbors2 = [[1],    #0
             [2],    #1
             [1],    #2
             [2]]    #3

neighbors3 = [[1],    #0
             [2],    #1
             [3],    #2
             [2]]    #3

print 'part1'
count2, root2 = bfs(root1, neighbors1, 0)
print 'count2=',count2
count3, root3 = bfs(root2, neighbors2, 1)
print 'count3=',count3
count4, root4 = bfs(root3, neighbors3, 2)
print 'count4=',count4
print 'total=',count2+count3+count4

##### PART2 #######

root1 = (F0, (ImmutableSet([TmG, TmM, PuG, SrG, ElG, ElM, DlG, DlM]),      # 0
             ImmutableSet([PuM, SrM]),                 # 1
             ImmutableSet([PmG, PmM, RuG, RuM]),       # 2
             ImmutableSet([])))                        # 3


root1 = (F0, (ImmutableSet([SG, SM, PG, PG, ElG, ElM, DlG, DlM]),      # 0
             ImmutableSet([TG, RG, RM, CG, CM]),                 # 1
             ImmutableSet([TM]),       # 2
             ImmutableSet([])))                        # 3

print 'part2'
count2, root2 = bfs(root1, neighbors1, 0)
print 'count2=',count2
count3, root3 = bfs(root2, neighbors2, 1)
print 'count3=',count3
count4, root4 = bfs(root3, neighbors3, 2)
print 'count4=',count4
print 'total=',count2+count3+count4
