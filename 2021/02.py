#! /usr/bin/env python


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
    file = "02.txt"
    # file = "02.ex"
    # part 1
    pos, depth = 0, 0
    with open(file) as f:
        for line in f:
            pos, depth = move(pos, depth, line.strip())
        print(pos * depth)
    # part 2
    pos, depth, aim = 0, 0, 0
    with open(file) as f:
        for line in f:
            pos, depth, aim = move_aim(pos, depth, aim, line.strip())
        print(pos * depth)
