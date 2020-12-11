#!/usr/bin/env python

import re

instr_pattern = re.compile(r"(\w+) ([-+]\d+)")


def exec_once(instructions):
    acc = 0
    pc = 0
    executed = []
    infinite_loop = False
    while True:
        if pc in executed:
            infinite_loop = True
            break
        if pc >= len(instructions):
            break
        executed.append(pc)
        instr = instructions[pc]
        op, value = instr_pattern.fullmatch(instr).group(1, 2)
        value = int(value)
        offset = 1
        if op == "nop":
            pass
        elif op == "acc":
            acc += value
        elif op == "jmp":
            offset = value
        pc += offset
    return infinite_loop, acc


def alter(instructions, index, pat, subst):
    new_instructions = [i for i in instructions]
    new_instructions[index] = new_instructions[index].replace(pat, subst)
    return new_instructions


if __name__ == "__main__":
    instructions = [line.strip() for line in open("08.txt")]
    print("infinite loop:", exec_once(instructions)[1])
    for pat, subst in [("nop", "jmp"), ("jmp", "nop")]:
        indices = [i for i, line in enumerate(instructions) if pat in line]
        for index in indices:
            infinite_loop, acc = exec_once(alter(instructions, index, pat, subst))
            if not infinite_loop:
                print(f"replacing {pat} by {subst} at line {index}:", acc)
