#!/usr/bin/env python

# memo = {}


def transform(value, subject=7):
    # if value in memo:
    #     return memo[value]
    # arg = value
    value *= subject
    value %= 20201227
    # memo[arg] = value
    return value


if __name__ == "__main__":
    with open("25.txt") as f:
        door_pub, card_pub = (int(line.strip()) for line in f.readlines())
    # example
    # door_pub, card_pub = 17807724, 5764801
    door_loop_size, card_loop_size = 0, 0
    loop_size = 0
    key = 1
    while door_loop_size == 0 or card_loop_size == 0:
        key = transform(key)
        loop_size += 1
        if key == door_pub:
            door_loop_size = loop_size
            print("door loop size is", door_loop_size)
        if key == card_pub:
            card_loop_size = loop_size
            print("card loop size is", card_loop_size)
    key = 1
    for i in range(card_loop_size):
        key = transform(key, subject=door_pub)
    print("part1:", key)
