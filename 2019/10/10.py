import math
import os
from collections import defaultdict


def solve(input):
    asteroids = []  # list of coordinates
    for y in range(len(input)):
        for x in range(len(input[y])):
            if input[y][x] == "#":
                asteroids.append((x, y))
    detections = defaultdict(lambda: defaultdict(list))
    for (x, y) in asteroids:
        for (xx, yy) in asteroids:
            if (x, y) == (xx, yy):
                continue
            if x == xx:
                alpha = math.pi / 2 * (-1 if yy < y else 1)
            elif y == yy:
                alpha = 0 if xx > x else math.pi
            else:
                alpha = math.atan2(yy - y, xx - x)
            detections[(x, y)][alpha].append((xx, yy))
    best_pos, best_detections_nb = max(
        [(pos, len(detection)) for pos, detection in detections.items()],
        key=lambda elt: elt[1],
    )

    targets = detections[best_pos]
    laser_angles = sorted(targets.keys())
    shift = 0
    for i, a in enumerate(laser_angles):
        shift = i
        if a >= -math.pi / 2:
            break
    laser_angles = laser_angles[shift:] + laser_angles[:shift]
    laser_idx = 0
    nb_victims = 0
    target_200 = None
    while True:
        laser = laser_angles[laser_idx]
        if len(targets[laser]) > 0:
            nb_victims += 1
            if nb_victims == 200:
                target_200 = targets[laser][0]
                break
            targets[laser] = targets[laser][1:]
        laser_idx += 1
        if laser_idx >= len(laser_angles):
            laser_idx = 0

    return [best_detections_nb, target_200[0] * 100 + target_200[1]]


if __name__ == "__main__":
    __location__ = os.path.realpath(
        os.path.join(os.getcwd(), os.path.dirname(__file__))
    )
    with open(os.path.join(__location__, "./input_aoc.txt")) as f:
        input = [line.strip() for line in f.readlines()]
        print(f"Solution : {solve(input)}")
