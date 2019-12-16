import os
import re
from itertools import combinations

regexp = r"(-?\d+).*?(-?\d+).*?(-?\d+)"


def part1(input):
    moons = []
    for line in input:
        m = re.search(regexp, line)
        moons.append((list(map(int, m.group(1, 2, 3))), [0, 0, 0]))
    for step in range(1000):
        # gravity
        for (i, j) in combinations(range(len(moons)), 2):
            for k in range(3):
                if moons[i][0][k] == moons[j][0][k]:
                    continue
                delta = moons[j][0][k] - moons[i][0][k]
                delta = delta / abs(delta)
                moons[i][1][k] += delta
                moons[j][1][k] -= delta
        # velocity
        for i in range(len(moons)):
            for k in range(3):
                moons[i][0][k] += moons[i][1][k]
    energy = sum(
        [
            sum([abs(moon[0][i]) for i in range(3)])
            * sum([abs(moon[1][i]) for i in range(3)])
            for moon in moons
        ]
    )
    return int(energy)


def part2(input):
    pass


if __name__ == "__main__":
    __location__ = os.path.realpath(
        os.path.join(os.getcwd(), os.path.dirname(__file__))
    )
    with open(os.path.join(__location__, "./input.txt")) as f:
        input = [line.strip() for line in f.readlines()]
        print(f"Part1 solution : {part1(input)}")
        print(f"Part2 solution : {part2(input)}")
