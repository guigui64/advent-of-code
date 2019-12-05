import os


def solve(input):
    [start, end] = [int(i) for i in input[0].split("-")]
    matches = set()
    matches_part2 = set()
    for tested in [str(t) for t in range(start, end + 1)]:
        if list(tested) == sorted(tested):
            for digit in tested:
                count = tested.count(digit)
                if count >= 2:
                    matches.add(tested)
                if count == 2:
                    matches_part2.add(tested)
    return [len(matches), len(matches_part2)]


if __name__ == "__main__":
    __location__ = os.path.realpath(
        os.path.join(os.getcwd(), os.path.dirname(__file__))
    )
    with open(os.path.join(__location__, "./input.txt")) as f:
        input = [line.strip() for line in f.readlines()]
        print(f"Solution : {solve(input)}")
