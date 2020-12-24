#!/usr/bin/env python


"""
Second take at AoC 2020/23 with a linked list.
Unfortunately not giving the right answer for part 2 :'(
"""


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class CircularLinkedList:
    def __init__(self, iterable):
        self.index = {}  # dict of nodes for faster look-up
        n = Node(iterable[0])
        self.index[n.data] = n
        self.head = n
        for item in iterable[1:]:
            ns = Node(item)
            self.index[ns.data] = ns
            n.next = ns
            n = ns
        n.next = self.head

    def to_list(self, starting_point=None):
        nodes = []
        for node in self.traverse(starting_point):
            nodes.append(node.data)
        return nodes

    def __repr__(self):
        nodes = self.to_list()
        return " -> ".join(str(n) for n in nodes)

    def traverse(self, starting_point=None):
        if starting_point is None:
            starting_point = self.head
        node = starting_point
        while node is not None and (node.next != starting_point):
            yield node
            node = node.next
        yield node

    def get(self, data):
        return self.index[data]

    def next(self, number=1):
        next = []
        node = self.head
        for _ in range(number):
            node = node.next
            next.append(node.data)
        return next


def exec_move(cups, cmin, cmax, move):
    # print(f"-- move {move + 1} --")
    # print("cups:", cups)
    cur_label = cups.head.data
    three = cups.next(3)
    # print("pick up:", three)
    destination = cur_label
    while destination in three + [cur_label]:
        destination -= 1
        if destination < cmin:
            destination = cmax
    # print("destination:", destination)
    first = cups.head.next
    last = first.next.next
    cups.head.next = last.next
    dest = cups.get(destination)
    following = dest.next
    dest.next = first
    last.next = following
    cups.head = cups.head.next


if __name__ == "__main__":
    cups_in = "389125467"
    # cups_in = "562893147"
    cups_in = [int(c) for c in cups_in]
    cmin, cmax = min(cups_in), max(cups_in)
    ori = cups_in.copy()
    cups = CircularLinkedList(cups_in)
    for move in range(100):
        exec_move(cups, cmin, cmax, move)
    cups.head = cups.get(1)
    print("part1:", "".join(str(c) for c in cups.to_list()[1:]))
    cups_in = ori[:] + list(range(cmax + 1, 1_000_000 + 1))
    cups = CircularLinkedList(cups_in)
    for move in range(10_000_000):
        print(f"\r{move+1:8d}", end="", flush=True)
        cur = exec_move(cups, cmin, cmax, move)
    print()
    cups.head = cups.get(1)
    next = cups.next(2)
    print(next)
    print("part2:", next[0] * next[1])
