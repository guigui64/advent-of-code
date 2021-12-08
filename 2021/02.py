#! /usr/bin/env python
import aoc


def move(pos, depth, order):
    dir, units = order.split()
    units = int(units)
    if dir == "forward":
        pos += units
    elif dir == "down":
        depth += units
    else:  # up
        depth -= units
    return pos, depth


def move_aim(pos, depth, aim, order):
    dir, units = order.split()
    units = int(units)
    if dir == "up":
        aim -= units
    elif dir == "down":
        aim += units
    else:  # forward
        pos += units
        depth += aim * units
    return pos, depth, aim


if __name__ == "__main__":
    # part 1
    pos, depth = 0, 0
    lines = aoc.input()
    for line in lines:
        pos, depth = move(pos, depth, line)
    print(pos * depth)
    # part 2
    pos, depth, aim = 0, 0, 0
    for line in lines:
        pos, depth, aim = move_aim(pos, depth, aim, line)
    print(pos * depth)
