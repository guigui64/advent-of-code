import os


def solve(input):
    width = 25
    height = 6
    size = width * height
    layers = [input[i : i + size] for i in range(0, len(input), size)]
    counts = None

    def count(layer, value):
        return sum(map(lambda x: 1 if x == value else 0, layer))

    for layer in layers:
        c = [count(layer, char) for char in "012"]
        if counts is None or counts[0] > c[0]:
            counts = c.copy()

    layers2 = [
        [layer[i : i + width] for i in range(0, len(layer), width)] for layer in layers
    ]
    img = [[" " for _ in range(width)] for _ in range(height)]
    for layer in layers2[::-1]:
        for h in range(height):
            for w in range(width):
                if layer[h][w] == "0":  # black
                    img[h][w] = " "
                elif layer[h][w] == "1":  # white
                    img[h][w] = "#"

    return [counts[1] * counts[2], "\n" + "\n".join(["".join(line) for line in img])]


if __name__ == "__main__":
    __location__ = os.path.realpath(
        os.path.join(os.getcwd(), os.path.dirname(__file__))
    )
    with open(os.path.join(__location__, "./input.txt")) as f:
        input = [line.strip() for line in f.readlines()][0]
        solution = solve(input)
        print(f"Part1 solution : {solution[0]}")
        print(f"Part2 solution : {solution[1]}")
