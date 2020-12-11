#!/usr/bin/env python

import re

if __name__ == "__main__":

    pattern = re.compile(r"(\d+)-(\d+) (\w): (\w+)")
    valid = 0
    valid2 = 0
    entries = []
    with open("02.txt") as f:
        for line in f:
            match = pattern.fullmatch(line.strip())
            min, max = map(int, match.group(1, 2))
            letter, password = match.group(3, 4)
            if min <= password.count(letter) <= max:
                valid += 1
            if (password[min - 1] == letter) != (password[max - 1] == letter):
                valid2 += 1
    print(valid, "passwords are valid with policy 1")
    print(valid2, "passwords are valid with policy 2")
