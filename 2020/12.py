#!/usr/bin/env python

"""
Directions in x,y where:
    +--> x
    |
    v y
"""
EAST = (1, 0)
SOUTH = (0, 1)
WEST = (-1, 0)
NORTH = (0, -1)

if __name__ == "__main__":
    # with open("12ex.txt") as f:
    with open("12.txt") as f:
        instructions = [line.strip() for line in f]
    pos = [0, 0]
    directions = [NORTH, EAST, SOUTH, WEST]
    direction = 1  # EAST
    for instr in instructions:
        cmd, value = instr[0], int(instr[1:])
        if cmd in "FNSWE":  # move
            if cmd == "F":  # forward
                d = directions[direction]
            elif cmd == "N":
                d = NORTH
            elif cmd == "S":
                d = SOUTH
            elif cmd == "W":
                d = WEST
            elif cmd == "E":
                d = EAST
            pos = [pos[i] + d[i] * value for i in [0, 1]]
        else:  # turn
            if cmd == "L":
                value = -value
            direction = (direction + int(value / 90)) % len(directions)
    print("part1:", sum([abs(p) for p in pos]))
    waypoint = [10, -1]
    pos = [0, 0]
    for instr in instructions:
        cmd, value = instr[0], int(instr[1:])
        if cmd == "F":  # move to waypoint
            pos = [pos[i] + waypoint[i] * value for i in [0, 1]]
        elif cmd in "NSWE":  # move waypoint
            if cmd == "N":
                d = NORTH
            elif cmd == "S":
                d = SOUTH
            elif cmd == "W":
                d = WEST
            elif cmd == "E":
                d = EAST
            waypoint = [waypoint[i] + d[i] * value for i in [0, 1]]
        else:  # turn waypoint around ship
            value = value % 360
            if cmd == "L":
                if value == 270:
                    value = 90
                elif value == 90:
                    value = 270
            if value == 90:
                waypoint = [-waypoint[1], waypoint[0]]
            elif value == 180:
                waypoint = [-waypoint[0], -waypoint[1]]
            elif value == 270:
                waypoint = [waypoint[1], -waypoint[0]]
    print("part2:", sum([abs(p) for p in pos]))
