import os


def intcode(code):
    idx = 0
    while True:
        if code[idx] == 1: # Add
            code[code[idx+3]] = code[code[idx+1]] + code[code[idx+2]]
            idx += 4
        elif code[idx] == 2: # Mutliply
            code[code[idx+3]] = code[code[idx+1]] * code[code[idx+2]]
            idx += 4
        elif code[idx] == 99: # Halt
            return code[0]
        else: # should not happen
            print(f"Error, opcode {code[idx]} unknown at index {idx}")
            return -1


def part1(input):
    code = [int(i) for i in input[0].split(",")]
    code[1] = 12
    code[2] = 2
    return intcode(code)


def part2(input, target):
    code = [int(i) for i in input[0].split(",")]
    for noun in range(100):
        for verb in range(100):
            attempt = code.copy()
            attempt[1] = noun
            attempt[2] = verb
            if intcode(attempt) == target:
                return 100*noun + verb


if __name__ == "__main__":
    __location__ = os.path.realpath(
        os.path.join(os.getcwd(), os.path.dirname(__file__))
    )
    with open(os.path.join(__location__, "./input.txt")) as f:
        input = [line.strip() for line in f.readlines()]
        print(f"Part1 solution : {part1(input)}")
        print(f"Part2 solution : {part2(input,19690720)}")
