import os
import threading
from collections import defaultdict
from queue import Empty, Queue

from defaultlist import defaultlist

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


def intcode(name, code, in_queue, out_queue):
    idx = 0
    relative_base = 0
    while True:
        try:
            instr = f"{code[idx]:05}"
            opcode = int(instr[-2:])
            modes = instr[:-2][::-1]

            def get_params_add(length):
                # 0 == position mode, 1 == immediate mode, 2 == relative mode
                return [
                    idx + i
                    if modes[i - 1] == "1"
                    else relative_base + code[idx + i]
                    if modes[i - 1] == "2"
                    else code[idx + i]
                    for i in range(1, length)
                ]

            if opcode == 1:  # Add
                length = 4
                params_add = get_params_add(length)
                code[params_add[2]] = code[params_add[0]] + code[params_add[1]]
                idx += length
            elif opcode == 2:  # Mutliply
                length = 4
                params_add = get_params_add(length)
                code[params_add[2]] = code[params_add[0]] * code[params_add[1]]
                idx += length
            elif opcode == 3:  # Save input
                length = 2
                params_add = get_params_add(length)
                input = in_queue.get()
                code[params_add[0]] = input
                idx += length
            elif opcode == 4:  # Output
                length = 2
                params_add = get_params_add(length)
                out_queue.put(code[params_add[0]])
                idx += length
            elif opcode == 5:  # Jump if true
                length = 3
                params_add = get_params_add(length)
                if code[params_add[0]] != 0:
                    idx = code[params_add[1]]
                else:
                    idx += length
            elif opcode == 6:  # Jump if false
                length = 3
                params_add = get_params_add(length)
                if code[params_add[0]] == 0:
                    idx = code[params_add[1]]
                else:
                    idx += length
            elif opcode == 7:  # Less than
                length = 4
                params_add = get_params_add(length)
                if code[params_add[0]] < code[params_add[1]]:
                    code[params_add[2]] = 1
                else:
                    code[params_add[2]] = 0
                idx += length
            elif opcode == 8:  # Equals
                length = 4
                params_add = get_params_add(length)
                if code[params_add[0]] == code[params_add[1]]:
                    code[params_add[2]] = 1
                else:
                    code[params_add[2]] = 0
                idx += length
            elif opcode == 9:  # Adjust base
                length = 2
                params_add = get_params_add(length)
                relative_base += code[params_add[0]]
                idx += length
            elif opcode == 99:  # Halt
                return code
            else:  # should not happen
                print(f"{name} : Error, opcode {opcode} unknown at index {idx}")
                return -1
        except IndexError:
            print(f"{name} : Index out of range")
            return -1


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
