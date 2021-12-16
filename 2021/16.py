#!/usr/bin/env python

import aoc
from math import prod


def read_int(bits, size, base=2):
    s = bits[:size]
    return int(s, base), bits[size:]


def parse_packet(bits, versions):
    version, bits = read_int(bits, 3)
    versions.append(version)
    type, bits = read_int(bits, 3)
    packet_length = 6
    value = 0
    if type == 4:  # literal
        number = ""
        while True:
            packet_length += 5
            leading, group = bits[0], bits[1:5]
            bits = bits[5:]
            number += group
            if leading == "0":
                break
        value = int(number, 2)
    else:  # operator
        length_id, bits = read_int(bits, 1)
        packet_length += 1
        values = []
        if length_id == 0:  # total length
            length, bits = read_int(bits, 15)
            packet_length += 15
            subpackets_lengths = 0
            while subpackets_lengths < length:
                bits, spl, val = parse_packet(bits, versions)
                subpackets_lengths += spl
                values.append(val)
            packet_length += subpackets_lengths
        else:  # number of subpackets
            number, bits = read_int(bits, 11)
            packet_length += 11
            subpackets_lengths = 0
            for _ in range(number):
                bits, spl, val = parse_packet(bits, versions)
                subpackets_lengths += spl
                values.append(val)
            packet_length += subpackets_lengths
        if type == 0:  # sum
            value = sum(values)
        elif type == 1:  # prod
            value = prod(values)
        elif type == 2:  # min
            value = min(values)
        elif type == 3:  # max
            value = max(values)
        elif type == 5:  # greater than
            value = 1 if (values[0] > values[1]) else 0
        elif type == 6:  # less than
            value = 1 if (values[0] < values[1]) else 0
        elif type == 7:  # equal
            value = 1 if (values[0] == values[1]) else 0
    return bits, packet_length, value


def main():
    for hexa in aoc.input():
        bits = bin(int(hexa, base=16))[2:]
        bits = "0" * (4 * len(hexa) - len(bits)) + bits
        versions = []
        _, _, value = parse_packet(bits, versions)
        print(sum(versions), value)


__name__ == "__main__" and main()
