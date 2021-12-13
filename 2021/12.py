#!/usr/bin/env python

from collections import defaultdict
import aoc


def main():
    G = defaultdict(list)
    for line in aoc.input():
        a, b = line.split("-")
        G[a] += [b]
        G[b] += [a]

    def traverse(cave, path, paths, part2=False, revisited=None):
        for cave in G[cave]:
            if cave == "end":
                path.append(cave)
                paths.append(path)
            elif cave.islower() and cave in path:
                if part2 and revisited is None and cave != "start":
                    npath = path.copy()
                    npath.append(cave)
                    traverse(cave, npath, paths, True, cave)
                else:
                    pass
            else:
                npath = path.copy()
                npath.append(cave)
                traverse(cave, npath, paths, part2, revisited)

    paths = []
    traverse("start", ["start"], paths)
    print(len(paths))
    paths = []
    traverse("start", ["start"], paths, True)
    print(len(paths))


__name__ == "__main__" and main()
