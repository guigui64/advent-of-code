#!/usr/bin/env python

import re
from collections import defaultdict
from dataclasses import dataclass, field
from typing import List, Tuple


@dataclass
class Bag:
    name: str = ""
    parents: List[str] = field(default_factory=list)
    children: List[Tuple[str, int]] = field(default_factory=list)


if __name__ == "__main__":
    bags_tree = defaultdict(Bag)
    pattern = re.compile(r"(\d+) (.+) bags?")
    for line in open("07.txt"):
        line = line[:-2]
        name, content = line.split(" bags contain ")
        bags_tree[name].name = name
        if content != "no other bags":
            content = map(
                lambda x: pattern.fullmatch(x).group(1, 2), content.split(", ")
            )
            for n, bag in content:
                bags_tree[name].children.append((bag, int(n)))
                bags_tree[bag].parents.append(name)
    name = "shiny gold"
    containing_bags = []

    def add_bags(name):
        for parent in bags_tree[name].parents:
            containing_bags.append(parent)
            add_bags(parent)

    add_bags(name)
    print(len(set(containing_bags)))

    def count_bags(name):
        s = 0
        for c, n in bags_tree[name].children:
            s += n * (1 + count_bags(c))
        return s

    print(count_bags(name))
