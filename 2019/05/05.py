import os


def intcode(code, input):
    outputs = []
    idx = 0
    while True:
        instr = f"{code[idx]:05}"
        opcode = int(instr[-2:])
        modes = instr[:-2][::-1]

        def get_params(length):
            return [
                code[idx + i] if modes[i - 1] == "1" else code[code[idx + i]]
                for i in range(1, length)
            ]

        if opcode == 1:  # Add
            length = 4
            params = get_params(length)
            code[code[idx + 3]] = params[0] + params[1]
            idx += length
        elif opcode == 2:  # Mutliply
            length = 4
            params = get_params(length)
            code[code[idx + 3]] = params[0] * params[1]
            idx += length
        elif opcode == 3:  # Save input
            length = 2
            code[code[idx + 1]] = input
            idx += length
        elif opcode == 4:  # Output
            length = 2
            params = get_params(length)
            outputs.append(params[0])
            idx += length
        elif opcode == 5:  # Jump if true
            length = 3
            params = get_params(length)
            if params[0] != 0:
                idx = params[1]
            else:
                idx += length
        elif opcode == 6:  # Jump if false
            length = 3
            params = get_params(length)
            if params[0] == 0:
                idx = params[1]
            else:
                idx += length
        elif opcode == 7:  # Less than
            length = 4
            params = get_params(length)
            if params[0] < params[1]:
                code[code[idx + 3]] = 1
            else:
                code[code[idx + 3]] = 0
            idx += length
        elif opcode == 8:  # Equals
            length = 4
            params = get_params(length)
            if params[0] == params[1]:
                code[code[idx + 3]] = 1
            else:
                code[code[idx + 3]] = 0
            idx += length
        elif opcode == 99:  # Halt
            return [code, outputs]
        else:  # should not happen
            print(f"Error, opcode {opcode} unknown at index {idx}")
            return -1


def part1(input):
    code = [int(i) for i in input[0].split(",")]
    outputs = intcode(code, 1)[1]
    for i, diag in enumerate(outputs[:-1]):
        print(f"Diagnostic {i + 1}/{len(outputs) - 1} : {'OK' if diag == 0 else 'KO'}")
    return outputs[-1]


def part2(input):
    code = [int(i) for i in input[0].split(",")]
    return intcode(code, 5)[1][0]


if __name__ == "__main__":
    __location__ = os.path.realpath(
        os.path.join(os.getcwd(), os.path.dirname(__file__))
    )
    with open(os.path.join(__location__, "./input.txt")) as f:
        input = [line.strip() for line in f.readlines()]
        print(f"Part1 solution : {part1(input)}")
        print(f"Part2 solution : {part2(input)}")
