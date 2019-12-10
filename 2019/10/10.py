import os
from collections import defaultdict


def part1(input):
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
                arctan = "y" if y > yy else "-y"
            else:
                arctan = (yy - y) / (xx - x)
                if y > yy:
                    arctan = f"-y{arctan}"
                elif x > xx:
                    arctan = f"-x{arctan}"
            detections[(x, y)][arctan].append((xx, yy))
    return max([len(detection) for detection in detections.values()])


def part2(input):
    pass


if __name__ == "__main__":
    __location__ = os.path.realpath(
        os.path.join(os.getcwd(), os.path.dirname(__file__))
    )
    with open(os.path.join(__location__, "./input_aoc.txt")) as f:
        input = [line.strip() for line in f.readlines()]
        print(f"Part1 solution : {part1(input)}")
        print(f"Part2 solution : {part2(input)}")
