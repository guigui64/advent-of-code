#!/usr/bin/env python

import aoc


def main():
    segments = [
        "abcefg",  #    0
        "cf",  #        1
        "acdeg",  #     2
        "acdfg",  #     3
        "bcdf",  #      4
        "abdfg",  #     5
        "abdefg",  #    6
        "acf",  #       7
        "abcdefg",  #   8
        "abcdfg",  #    9
    ]
    lengths = [len(s) for s in segments]
    l2d = {2: 1, 3: 7, 4: 4, 7: 8}  # length to unique digits

    line: str
    count = 0
    total = 0
    for line in aoc.input():
        decoded = {}  # digit to pattern
        patterns, values = [
            ["".join(sorted(elt)) for elt in group.split()] for group in line.split(" | ")
        ]
        # print(patterns, values)
        # part1
        unique = [v for v in values if len(v) in l2d.keys()]
        count += len(unique)
        # part2
        # - find unique digits
        for pat in patterns:
            if len(pat) in l2d:
                decoded[l2d[len(pat)]] = pat
        # - find 6-length digits: 0, 6 and 9
        #   - find 6: length is 6 and one segment from 1 is not in it
        for pat in patterns:
            if len(pat) == lengths[6] and any([c not in pat for c in decoded[1]]):
                decoded[6] = pat
                break
        #   - find 0: out of two remaining 6-length (0 and 9) it is the only one to have one segment that is not
        # in 4
        for pat in patterns:
            if (
                len(pat) == lengths[0]
                and pat not in decoded.values()
                and any([c not in pat for c in decoded[4]])
            ):
                decoded[0] = pat
                break
        #   - last 6-length is 9
        decoded[9] = [
            pat for pat in patterns if len(pat) == lengths[9] and pat not in decoded.values()
        ][0]
        # - find 5-length digits: 2, 3 and 5
        #   - find 5: all segments from 5 are in 6
        for pat in patterns:
            if (
                len(pat) == lengths[5]
                and pat not in decoded.values()
                and all([c in decoded[6] for c in pat])
            ):
                decoded[5] = pat
                break
        #   - find 3: all segments from 3 are in 9
        for pat in patterns:
            if (
                len(pat) == lengths[3]
                and pat not in decoded.values()
                and all([c in decoded[9] for c in pat])
            ):
                decoded[3] = pat
                break
        #   - last 5-length is 2
        decoded[2] = [
            pat for pat in patterns if len(pat) == lengths[2] and pat not in decoded.values()
        ][0]

        # reverse map from pat to digit to digit to pat
        decoded = {v: k for k, v in decoded.items()}
        # print(decoded)

        # compute displayed number
        number = int("".join([str(decoded[val]) for val in values]))
        # print(number)
        total += number

    print(count)
    print(total)


__name__ == "__main__" and main()
