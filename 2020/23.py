#!/usr/bin/env python

""" My take at AoC 2020/23. Elegant but not fast enough for part 2... """


def exec_move(cups, cur, cmin, cmax):
    # print(f"-- move {move + 1} --")
    # print("cups:", cups)
    cur_label = cups[cur]
    three = []
    for _ in range(3):
        three.append(cups.pop((cups.index(cur_label) + 1) % len(cups)))
    # print("pick up:", three)
    destination = cur_label - 1
    while destination not in cups:
        destination -= 1
        if destination < cmin:
            destination = cmax
    # print("destination:", destination)
    for _ in range(3):
        cups.insert(cups.index(destination) + 1, three.pop())
    cur = (cups.index(cur_label) + 1) % len(cups)
    return cur


if __name__ == "__main__":
    # cups = "389125467"
    cups = "562893147"
    cups = [int(c) for c in cups]
    ori = cups[:]
    cur = 0
    cmin, cmax = min(cups), max(cups)
    for move in range(100):
        cur = exec_move(cups, cur, cmin, cmax)
    one = cups.index(1)
    print("part1:", "".join(str(c) for c in cups[one + 1 :] + cups[:one]))
    cups = ori[:] + list(range(cmax + 1, 1_000_000 + 1))
    for move in range(10_000_000):
        print(f"\r{move+1:8d}", end="", flush=True)
        cur = exec_move(cups, cur, cmin, cmax)
    print()
    one = cups.index(1)
    print("part2:", cups[(one + 1) % len(cups)] * cups[(one + 2) % len(cups)])
