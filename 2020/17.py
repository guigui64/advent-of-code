#!/usr/bin/env python

from itertools import product


def solve(fname, dimensions=3):
    space = set()

    def toggle(elt, space):
        if elt in space:
            space.remove(elt)
        else:
            space.add(elt)

    def active(elt, space):
        return elt in space

    def neighbors(elt, space):
        deltas = list(product((1, 0, -1), repeat=dimensions))
        deltas.remove(tuple([0] * dimensions))
        return sum(
            active(tuple(e + d for e, d in zip(elt, delta)), space) for delta in deltas
        )

    with open(fname) as f:
        y = x = 0
        for line in f:
            x = 0
            for c in line.strip():
                if c == "#":
                    toggle((x, y) + tuple([0] * (dimensions - 2)), space)
                x += 1
            y += 1
    cycles = 6
    for _ in range(cycles):
        new = space.copy()
        count = 0
        bounds = [
            (min(e[dim] for e in space) - 1, max(e[dim] for e in space) + 2)
            for dim in range(dimensions)
        ]
        for point in product(*[list(range(*bounds[dim])) for dim in range(dimensions)]):
            if (active(point, space) and not (2 <= neighbors(point, space) <= 3)) or (
                not active(point, space) and neighbors(point, space) == 3
            ):
                toggle(point, new)
            if active(point, new):
                count += 1
        space = new.copy()
    return count


if __name__ == "__main__":
    print(solve("17.txt"))
    print(solve("17.txt", 4))
