#!/usr/bin/env python

""" Inspired by solution of StasDeep """

from itertools import count


def run(cups, num_iterations):
    d = {c1: c2 for c1, c2 in zip(cups, cups[1:] + [cups[0]])}
    cur = cups[0]
    for x in range(num_iterations):
        x = cur
        pickup = [x := d[x] for _ in range(3)]
        dest = next(
            cup
            for i in count(1)
            if (cup if (cup := cur - i) > 0 else (cup := len(cups) + cup)) not in pickup
        )

        d[cur], d[pickup[-1]], d[dest] = d[pickup[-1]], d[dest], d[cur]

        cur = d[cur]

    x = 1
    return [x := d[x] for _ in cups]


if __name__ == "__main__":
    # cups = "389125467"
    cups = "562893147"
    cups = [int(c) for c in cups]
    after_100 = run(cups, 100)
    print("part1:", "".join(str(c) for c in after_100[:-1]))
    cups = cups + list(range(max(cups) + 1, 1_000_000 + 1))
    after_10m = run(cups, 10_000_000)
    print("part2:", after_10m[0] * after_10m[1])
