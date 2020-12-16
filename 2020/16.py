#!/usr/bin/env python


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
            # ok = False
            # for bounds in fields.values():
            #     for a, b in bounds:
            #         if a <= value <= b:
            #             ok = True
            # if not ok:
            #     erroneous += [value]
            if not any(
                [a <= value <= b for bounds in fields.values() for (a, b) in bounds]
            ):
                erroneous += [value]
                erroneous_tickets.add(i)
    print("part1:", sum(erroneous))
    # nearby_tickets = [
    #     ticket for i, ticket in enumerate(nearby_tickets) if i not in erroneous_tickets
    # ]


if __name__ == "__main__":
    solve("16ex.txt")
    solve("16ex2.txt")
    solve("16.txt")
