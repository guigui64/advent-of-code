#!/usr/bin/env python

from collections import deque


def parse(fname):
    with open(fname) as f:
        players_decks = [
            deque([int(line.strip()) for line in group.split("\n")[1:]])
            for group in f.read()[:-1].split("\n\n")
        ]
    return players_decks


def combat(players_decks, recursive=False):
    old_states = []
    while all(len(deck) != 0 for deck in players_decks):
        # Manage old states
        if recursive and str(players_decks) in old_states:
            return 0  # No infinite game => player 1 wins
        old_states.append(str(players_decks))
        # Draw cards
        top_cards = [deck.popleft() for deck in players_decks]
        if recursive and all(len(players_decks[i]) >= top_cards[i] for i in range(2)):
            # sub-game
            new_decks = [
                deque(list(players_decks[i])[: top_cards[i]]) for i in range(2)
            ]
            winner = combat(new_decks, True)
        else:
            winner = max((v, i) for (i, v) in enumerate(top_cards))[1]
        players_decks[winner].append(top_cards.pop(winner))
        players_decks[winner].append(top_cards.pop())
    winner = [i for (i, deck) in enumerate(players_decks) if len(deck) != 0][0]
    return winner


if __name__ == "__main__":
    fname = "22.txt"
    # Part 1 : Combat
    players_decks = parse(fname)
    winner = combat(players_decks)
    deck = players_decks[winner]
    deck.reverse()
    print("part1:", sum((i + 1) * v for (i, v) in enumerate(deck)))
    # Part 2 : Recursive Combat
    players_decks = parse(fname)
    winner = combat(players_decks, True)
    deck = players_decks[winner]
    deck.reverse()
    print("part2:", sum((i + 1) * v for (i, v) in enumerate(deck)))
