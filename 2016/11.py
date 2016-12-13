import itertools
import deepcopy from copy

types = "TPSR"
floors = {1: {"G" : ["T", "P", "S"], "M" : ["T"]},
          2: {"G" : [],              "M" : ["P", "S"]},
          3: {"G" : ["P", "R"],      "M" : ["P", "R"]},
          4: {"G" : [],              "M" : []}}
elevator = 1

def moves(floors, elevator):
    """ Computes the possibles moves """
    moves = []
    floor = floors[elevator]
    tuples = [(x, y) for x in floor for y in floor[x]]
    loads = *itertools.combinations(tuples, 2) + *itertools.combinations(tuples,1)
    for load in loads:
        # up
        if elevator < 4:
            floor = floors[elevator + 1]
            for (n,t) in load:
                floor[n] += [t]
            if not invalid(floor):
                newfloors = deepcopy(floors)
                newfloors[elevator] = #remove
                newfloors[elevator + 1] = #add
                moves.append
        # down

def invalid(floor):
    for type in types:
        if type in floor["M"] and not type in floor["G"] and len(floor["G"]) != 0 :
            return True
    return False

steps = 0
# while
