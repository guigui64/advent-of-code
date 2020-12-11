#!/usr/bin/env python

if __name__ == "__main__":
    groups = open("06.txt").read().split("\n\n")
    print(sum([len(set("".join(g.split()))) for g in groups]))
    alphabet = [chr(x) for x in range(ord("a"), ord("z") + 1)]
    print(
        sum(
            [
                sum([all([letter in g for g in group.split()]) for letter in alphabet])
                for group in groups
            ]
        )
    )
