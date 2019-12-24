import os
from collections import defaultdict
from math import ceil


def part1(input):
    reactions = defaultdict(lambda: defaultdict(int))
    for line in input:
        inp, out = line.split(" => ")
        for i, j in [x.split() for x in inp.split(", ")]:
            reactions[out.split()[1]][j] = (int(i), int(out.split()[0]))
    needed = {"FUEL": 1}
    leftovers = defaultdict(int)

    def get_resources(needed, leftovers):
        needed2 = defaultdict(int)
        for i, j in needed.items():
            for k in reactions[i].keys():
                qty = ceil(j / reactions[i][k][1])
                needed2[k] += reactions[i][k][0] * qty
                leftovers[k] += qty * reactions[i][k][1] - j
        return needed2

    while len(needed) > 0:
        needed = get_resources(needed, leftovers)
        print(needed, leftovers)
    pass


def part2(input):
    pass


if __name__ == "__main__":
    __location__ = os.path.realpath(
        os.path.join(os.getcwd(), os.path.dirname(__file__))
    )
    with open(os.path.join(__location__, "./input_ex2.txt")) as f:
        input = [line.strip() for line in f.readlines()]
        print(f"Part1 solution : {part1(input)}")
        print(f"Part2 solution : {part2(input)}")
