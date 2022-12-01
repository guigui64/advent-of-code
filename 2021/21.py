#!/usr/bin/env python

import aoc


def main():
    positions = list(map(int, [line[-1] for line in aoc.input()]))
    part1(positions.copy())
    part2(positions.copy())


def part1(positions):
    scores = [0, 0]
    dice = 1
    rolls = 0
    play = True
    while play:
        for player in range(2):
            move = 0
            for _ in range(3):
                move += dice
                if dice == 100:
                    dice = 1
                else:
                    dice += 1
                rolls += 1
            positions[player] = (positions[player] + move - 1) % 10 + 1
            scores[player] += positions[player]
            if scores[player] >= 1000:
                play = False
                break
    print(rolls * [s for s in scores if s < 1000][0])


def part2(pos):  # credits to davearussel
    ways = [0, 0, 0, 1, 3, 6, 7, 6, 3, 1]  # How many ways can 3 dice sum to each number?
    worlds = {  # (p1_pos, p2_pos, p1_score, p2_score, next_player) -> n_worlds
        (pos[0], pos[1], 0, 0, 0): 1,
    }
    wins0 = wins1 = 0
    while worlds:
        new_worlds = {}
        for (p0, p1, s0, s1, turn), n in worlds.items():
            for roll in range(3, 10):
                if turn == 0:
                    _p0 = (p0 + roll) % 10
                    _s0 = s0 + (_p0 or 10)
                    if _s0 >= 21:
                        wins0 += n * ways[roll]
                    else:
                        state = (_p0, p1, _s0, s1, 1)
                        new_worlds[state] = new_worlds.get(state, 0) + n * ways[roll]
                else:
                    _p1 = (p1 + roll) % 10
                    _s1 = s1 + (_p1 or 10)
                    if _s1 >= 21:
                        wins1 += n * ways[roll]
                    else:
                        state = (p0, _p1, s0, _s1, 0)
                        new_worlds[state] = new_worlds.get(state, 0) + n * ways[roll]
        worlds = new_worlds
    print(max(wins0, wins1))


__name__ == "__main__" and main()
