import os
import threading
from collections import defaultdict
from queue import Empty, Queue

from defaultlist import defaultlist

from aoc import intcode, intcodeLambda

EMPTY = 0
WALL = 1
BLOCK = 2
PADDLE = 3
BALL = 4

NEUTRAL = 0
LEFT = -1
RIGHT = 1


def part1(input):
    software = defaultlist(int)
    for i, v in enumerate(input[0].split(",")):
        software[i] = int(v)
    inq = Queue()
    outq = Queue()
    # arcade = threading.Thread(
    #     name="ARCADE", target=intcode, args=("ARCADE", software, inq, outq)
    # )
    intcode("ARCADE", software, inq, outq)
    nb_blocks = 0
    try:
        while True:
            x = outq.get_nowait()
            y = outq.get_nowait()
            tile_id = outq.get_nowait()
            if tile_id == BLOCK:
                nb_blocks += 1
    except Empty:
        return nb_blocks


def part2(input):
    software = defaultlist(int)
    for i, v in enumerate(input[0].split(",")):
        software[i] = int(v)
    software[0] = 2  # free game !
    joystick = NEUTRAL
    inl = lambda: joystick
    outq = Queue()
    arcade = threading.Thread(
        name="ARCADE", target=intcodeLambda, args=("ARCADE", software, inl, outq)
    )
    paddle_x, ball_x = 0, 0
    arcade.start()
    try:
        while True:
            x = outq.get(timeout=9)
            y = outq.get()
            if x == -1 and y == 0:
                score = outq.get()
                print(score)
            else:
                tile_id = outq.get()
                paddle_x = x if tile_id == PADDLE else paddle_x
                ball_x = x if tile_id == BALL else ball_x
                joystick = NEUTRAL
                if paddle_x > ball_x:
                    joystick = LEFT
                elif paddle_x < ball_x:
                    joystick = RIGHT
    except Empty:
        return score


if __name__ == "__main__":
    __location__ = os.path.realpath(
        os.path.join(os.getcwd(), os.path.dirname(__file__))
    )
    with open(os.path.join(__location__, "./input.txt")) as f:
        input = [line.strip() for line in f.readlines()]
        print(f"Part1 solution : {part1(input)}")
        print(f"Part2 solution : {part2(input)}")
