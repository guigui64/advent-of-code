#!/usr/bin/env python

import aoc

import heapq


class PriorityQueue:
    def __init__(self):
        self.elements = []

    def empty(self):
        return not self.elements

    def put(self, item, priority):
        heapq.heappush(self.elements, (priority, item))

    def get(self):
        return heapq.heappop(self.elements)[1]


def a_star(neighbors, cost, heuristic, start, end):
    frontier = PriorityQueue()
    frontier.put(start, 0)
    came_from = {}
    cost_so_far = {}
    came_from[start] = None
    cost_so_far[start] = 0
    while not frontier.empty():
        current = frontier.get()
        if current == end:
            break
        for next in neighbors(*current, end):
            new_cost = cost_so_far[current] + cost(*next)
            if next not in cost_so_far or new_cost < cost_so_far[next]:
                cost_so_far[next] = new_cost
                priority = new_cost + heuristic(*next, end)
                frontier.put(next, priority)
                came_from[next] = current
    return cost_so_far, came_from


def neighbors(x, y, limits):
    W, H = limits
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    for dx, dy in directions:
        if x + dx < 0 or y + dy < 0:
            continue
        if x + dx > W or y + dy > H:
            continue
        yield (x + dx, y + dy)


def heuristic(x, y, goal):
    X, Y = goal
    return abs(x - X) + abs(y - Y)


def main():
    risks = {}
    for y, line in enumerate(aoc.input()):
        for x, c in enumerate(line):
            risks[(x, y)] = int(c)

    W = max(x for x, _ in risks.keys()) + 1
    H = max(y for _, y in risks.keys()) + 1

    start = (0, 0)
    end = (W - 1, H - 1)
    cost = lambda x, y: risks[(x, y)]
    cost_so_far, _ = a_star(neighbors, cost, heuristic, start, end)
    print(cost_so_far[end])

    big_risks = {}
    for xs in range(5):
        for ys in range(5):
            for (x, y) in risks.keys():
                x2 = xs * W + x
                y2 = ys * H + y
                new_risk = risks[(x, y)] + xs + ys
                while new_risk > 9:
                    new_risk -= 9
                big_risks[(x2, y2)] = new_risk
    risks = big_risks
    W = max(x for x, _ in risks.keys()) + 1
    H = max(y for _, y in risks.keys()) + 1

    start = (0, 0)
    end = (W - 1, H - 1)
    cost = lambda x, y: risks[(x, y)]
    cost_so_far, _ = a_star(neighbors, cost, heuristic, start, end)
    print(cost_so_far[end])


__name__ == "__main__" and main()
