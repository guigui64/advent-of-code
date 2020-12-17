#!/usr/bin/env python

from math import prod


def solve(fname):
    with open(fname) as f:
        groups = [block.split("\n") for block in f.read()[:-1].split("\n\n")]
    fields = {}
    for entry in groups[0]:
        name, rest = entry.split(": ")
        fields[name] = [[int(x) for x in e.split("-")] for e in rest.split(" or ")]
    my_ticket = [int(x) for x in groups[1][1].split(",")]
    nearby_tickets = [[int(x) for x in e.split(",")] for e in groups[2][1:]]
    erroneous = []
    erroneous_tickets = set()
    for i, ticket in enumerate(nearby_tickets):
        for value in ticket:
            if not any(
                [a <= value <= b for ranges in fields.values() for (a, b) in ranges]
            ):
                erroneous += [value]
                erroneous_tickets.add(i)
    print("part1:", sum(erroneous))
    nearby_tickets = [
        ticket for i, ticket in enumerate(nearby_tickets) if i not in erroneous_tickets
    ]
    indices = {}
    pool = list(range(len(my_ticket)))
    while len(pool) > 0:
        for i in pool:
            matches = [
                name
                for name, ranges in fields.items()
                if all(
                    any(a <= ticket[i] <= b for (a, b) in ranges)
                    for ticket in nearby_tickets
                )
            ]
            if len(matches) == 1:
                name = matches[0]
                indices[name] = i
                del fields[name]
                pool.remove(i)
                break
    print(
        "part2:",
        prod(my_ticket[v] for (k, v) in indices.items() if k.startswith("departure")),
    )


if __name__ == "__main__":
    # solve("16ex.txt")
    # solve("16ex2.txt")
    solve("16.txt")
