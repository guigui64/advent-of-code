#!/usr/bin/env python

import aoc


def bounds(img):
    x = min(x for x, _ in img)
    y = min(y for _, y in img)
    X = max(x for x, _ in img)
    Y = max(y for _, y in img)
    return (x, X), (y, Y)


def index(img, x, y, xmin, xmax, ymin, ymax, out_is_lit=False):
    sb = ""
    for dy in (-1, 0, 1):
        for dx in (-1, 0, 1):
            if (x + dx, y + dy) in img:
                sb += "1"
            elif x + dx < xmin or x + dx > xmax or y + dy < ymin or y + dy > ymax:
                sb += "1" if out_is_lit else "0"
            else:
                sb += "0"
    return int(sb, base=2)


def printimg(img):
    (xmin, xmax), (ymin, ymax) = bounds(img)
    for y in range(ymin, ymax + 1):
        for x in range(xmin, xmax + 1):
            print("#" if (x, y) in img else ".", end="")
        print()
    print()


def main():
    lines = aoc.input()
    enhancement = lines[0]
    img = set()
    for y, line in enumerate(lines[2:]):
        for x, pix in enumerate(line):
            if pix == "#":
                img.add((x, y))

    for step in range(50):
        # printimg(img)
        output = set()
        (xmin, xmax), (ymin, ymax) = bounds(img)
        out_is_lit = False
        if step % 2 != 0 and enhancement[0] == "#":
            out_is_lit = True
        for y in range(ymin - 1, ymax + 2):
            for x in range(xmin - 1, xmax + 2):
                idx = index(img, x, y, xmin, xmax, ymin, ymax, out_is_lit)
                if enhancement[idx] == "#":
                    output.add((x, y))
        img = output
        if step == 1:
            print(len(img))
    # printimg(img)
    print(len(img))


__name__ == "__main__" and main()
