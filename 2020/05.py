#!/usr/bin/env python


plane_rows = 128
plane_columns = 8


def compute_id(p):
    binf, bsup = 0, plane_rows - 1
    for letter in p[:7]:
        if letter == "F":
            bsup -= int((bsup - binf + 1) / 2)
        else:
            binf += int((bsup - binf + 1) / 2)
    row = bsup
    binf, bsup = 0, plane_columns - 1
    for letter in p[-3:]:
        if letter == "L":
            bsup -= int((bsup - binf + 1) / 2)
        else:
            binf += int((bsup - binf + 1) / 2)
    col = bsup
    return row * plane_columns + col


if __name__ == "__main__":
    passes = [line.strip() for line in open("05.txt")]
    ids = []
    for p in passes:
        seat_id = compute_id(p)
        ids.append(seat_id)
    highest_id = max(ids)
    print("Highest seat id is", highest_id)
    for id in range(min(ids), highest_id):
        if id not in ids:
            print("Seat", id, "is free")
