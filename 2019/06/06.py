import os
from collections import defaultdict

from anytree import Node, Walker


def solve(input):
    orbits_dict = defaultdict(list)
    orbits_set = set()
    orbits_tree = {}
    for line in input:
        parts = line.split(")")
        orbits_set.add(parts[0])
        orbits_set.add(parts[1])
        orbits_dict[parts[0]].append(parts[1])
    for i in orbits_set:
        orbits_tree[i] = Node(i)

    # Construct tree
    for center, satellites in orbits_dict.items():
        orbits_tree[center].children = [orbits_tree[sat] for sat in satellites]

    total = 0
    for node in orbits_tree:
        total += orbits_tree[node].depth

    w = Walker()
    routes = w.walk(orbits_tree["YOU"], orbits_tree["SAN"])
    transfers = len(routes[0]) + len(routes[2]) - 2  # upwards + downwards - YOU and SAN

    return [total, transfers]


if __name__ == "__main__":
    __location__ = os.path.realpath(
        os.path.join(os.getcwd(), os.path.dirname(__file__))
    )
    with open(os.path.join(__location__, "./input.txt")) as f:
        input = [line.strip() for line in f.readlines()]
        print(f"Solution : {solve(input)}")
