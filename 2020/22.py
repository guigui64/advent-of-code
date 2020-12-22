#!/usr/bin/env python

from collections import deque


def parse(fname):
    with open(fname) as f:
        players_decks = [
            deque([int(line.strip()) for line in group.split("\n")[1:]])
            for group in f.read()[:-1].split("\n\n")
        ]
    return players_decks


if __name__ == "__main__":
    fname = "22ex.txt"
    players_decks = parse(fname)
    while all(len(deck) != 0 for deck in players_decks):
        top_cards = [deck.popleft() for deck in players_decks]
        winner = max((v, i) for (i, v) in enumerate(top_cards))[1]
        [players_decks[winner].append(f(top_cards)) for f in (max, min)]
    deck = [deck for deck in players_decks if len(deck) > 0][0]
    deck.reverse()
    print("part1:", sum((i + 1) * v for (i, v) in enumerate(deck)))
    players_decks = parse(fname)
