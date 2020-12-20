#!/usr/bin/env python

import re

# from itertools import product


# def evaluate(rules, id):
#     if '"' in rules[id]:
#         return list(rules[id][1])  # get letter in '"x"'
#     if "|" in rules[id]:
#         left, right = [
#             ["".join(p) for p in product(*[evaluate(rules, x) for x in side.split()])]
#             for side in rules[id].split(" | ")
#         ]
#         return left + right
#     return [
#         "".join(p) for p in product(*[evaluate(rules, x) for x in rules[id].split()])
#     ]


def buildregex(rules, id):
    if '"' in rules[id]:
        return rules[id][1]
    if "|" in rules[id]:
        left, right = [
            "".join(buildregex(rules, x) for x in side.split())
            for side in rules[id].split(" | ")
        ]
        return f"({left}|{right})"
    if part == 2 and id in ["8", "11"]:
        append = "{NB}" if id == "11" else "+"
        # append = "+"
        return "".join(
            r + append for r in [buildregex(rules, x) for x in rules[id].split()]
        )
    else:
        return "".join(buildregex(rules, x) for x in rules[id].split())


def solve(fname):
    with open(fname) as f:
        rules, messages = [group.split("\n") for group in f.read()[:-1].split("\n\n")]
    rules = {rule.split(": ")[0]: rule.split(": ")[1] for rule in rules}
    # possibilities = evaluate(rules, "0")
    # return sum([message in possibilities for message in messages])
    if part == 1:
        regex = re.compile(buildregex(rules, "0"))
        return sum(regex.fullmatch(message) is not None for message in messages)
    else:
        """TODO replace NB range strategy by something more elegant
        like len(reg42) == len(reg31) but why is it not working ?
        or maybe some badass regex with group name..."""
        regex = buildregex(rules, "0")
        count = sum(
            any(
                re.fullmatch(regex.replace("NB", str(n)), message) is not None
                for n in range(1, 10)
            )
            for message in messages
        )
        # for message in messages:
        #     if re.fullmatch(regex, message) is not None:
        #         reg42, reg31 = [buildregex(rules, i) for i in ("42", "31")]
        #         if len(re.findall(reg42, message)) == len(re.findall(reg31, message)):
        #             count += 1
        return count


if __name__ == "__main__":
    # print("part1:", solve("19ex.txt"))
    part = 1
    print("part1:", solve("19.txt"))
    part = 2
    print("part2:", solve("19.txt"))
