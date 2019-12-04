import os


def compute(move, path):
    dir = move[0]
    dist = int(move[1:])
    last_pos = path[-1]
    for i in range(dist):
        if dir == "U":
            path += [(last_pos[0], last_pos[1] + i + 1)]
        elif dir == "D":
            path += [(last_pos[0], last_pos[1] - i - 1)]
        elif dir == "L":
            path += [(last_pos[0] - i - 1, last_pos[1])]
        elif dir == "R":
            path += [(last_pos[0] + i + 1, last_pos[1])]
        else:
            raise Exception("ERROR: could not handle move " + move)


def manhattan(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])


def solve(input):
    paths = []
    spaths = []
    for wire in input:
        path = [(0, 0)]
        for move in wire.split(","):
            compute(move, path)
        paths += [path]
        spaths += [set(path)]
    crossed = spaths[0].intersection(*spaths[1:])
    crossed.remove((0, 0))
    print("Min distance : {}".format(min(map(lambda p: manhattan((0, 0), p), crossed))))
    stepss = []
    for path in paths:
        steps = dict()
        for step, pos in enumerate(path):
            if pos in crossed and pos not in steps.keys():
                steps[pos] = step
        stepss += [steps]
    print(
        "Min steps : {}".format(
            min(map(lambda c: sum([steps[c] for steps in stepss]), crossed))
        )
    )


if __name__ == "__main__":
    __location__ = os.path.realpath(
        os.path.join(os.getcwd(), os.path.dirname(__file__))
    )
    with open(os.path.join(__location__, "./input.txt")) as f:
        input = [line.strip() for line in f.readlines()]
        solve(input)
