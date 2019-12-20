import os
import threading
from collections import defaultdict
from queue import Empty, Queue

from defaultlist import defaultlist

from aoc import intcode

BLACK = 0
WHITE = 1
UP = 0
RIGHT = 1
DOWN = 2
LEFT = 3


def turn(direction, way):
    if way == 0:
        return (direction - 1) % 4
    else:
        return (direction + 1) % 4


def move(position, direction):
    if direction == UP:
        return (position[0], position[1] + 1)
    elif direction == DOWN:
        return (position[0], position[1] - 1)
    elif direction == RIGHT:
        return (position[0] + 1, position[1])
    else:
        return (position[0] - 1, position[1])


def paint(input, color_start=BLACK):
    software = defaultlist(int)
    for i, v in enumerate(input[0].split(",")):
        software[i] = int(v)
    inq = Queue()
    inq.put(color_start)
    outq = Queue()
    robot = threading.Thread(
        name="ROBOT", target=intcode, args=("ROBOT", software, inq, outq)
    )
    pos = (0, 0)
    dir = UP
    hull = defaultdict(lambda: (BLACK, False))
    nb_painted = 0
    robot.start()
    try:
        while True:
            color = outq.get(timeout=0.3)
            if not hull[pos][1]:
                nb_painted += 1
            hull[pos] = (color, True)
            way = outq.get()
            dir = turn(dir, way)
            pos = move(pos, dir)
            inq.put(hull[pos][0])
    except Empty:
        pass
    return (nb_painted, hull)


def part1(input):
    return paint(input)[0]


def part2(input):
    hull = paint(input, WHITE)[1]
    xmin, xmax, ymin, ymax = 0, 0, 0, 0
    for p in hull:
        xmin = min(xmin, p[0])
        xmax = max(xmax, p[0])
        ymin = min(ymin, p[1])
        ymax = max(ymax, p[1])
    for y in range(ymax, ymin - 1, -1):
        for x in range(xmin, xmax + 1):
            print("#" if hull[(x, y)][0] == WHITE else " ", end="")
        print()
    return None


if __name__ == "__main__":
    __location__ = os.path.realpath(
        os.path.join(os.getcwd(), os.path.dirname(__file__))
    )
    with open(os.path.join(__location__, "./input.txt")) as f:
        input = [line.strip() for line in f.readlines()]
        print(f"Part1 solution : {part1(input)}")
        print(f"Part2 solution : {part2(input)}")
