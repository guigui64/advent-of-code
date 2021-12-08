#! /usr/bin/env python
import aoc

if __name__ == "__main__":
    fish = [0] * 9  # number of fishes per "count"
    for f in aoc.input()[0].split(","):
        fish[int(f)] += 1
    for day in range(256):
        fish.append(
            fish.pop(0)
        )  # remove number of fish with count 0 and add same amount for count 8 (new children)
        fish[6] += fish[8]  # same amount of children for parents that reset their counter
        if day == 79:
            print(sum(fish))
    print(sum(fish))
