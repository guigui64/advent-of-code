import os
import threading
from itertools import permutations
from queue import Queue


def intcode(name, code, in_queue, out_queue):
    idx = 0
    while True:
        try:
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
                input = in_queue.get()
                code[code[idx + 1]] = input
                idx += length
            elif opcode == 4:  # Output
                length = 2
                params = get_params(length)
                out_queue.put(params[0])
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
                return code
            else:  # should not happen
                print(f"{name} : Error, opcode {opcode} unknown at index {idx}")
                return -1
        except IndexError:
            print(f"{name} : Index out of range")
            return -1


def part1(input):
    software = [int(i) for i in input[0].split(",")]
    highest_signal = 0
    for phases in permutations(range(5), 5):
        signal = 0
        for i, amplifier in enumerate("ABCDE"):
            name = "amplifier-" + amplifier
            in_queue = Queue()
            in_queue.put(phases[i])
            in_queue.put(signal)
            out_queue = Queue()
            intcode(name, software.copy(), in_queue, out_queue)
            signal = out_queue.get()  # should be the only element
        highest_signal = max(highest_signal, signal)
    return highest_signal


def part2(input):
    software = [int(i) for i in input[0].split(",")]
    highest_signal = 0
    for phases in permutations(range(5, 10), 5):
        N = 5
        queues = [Queue() for _ in range(N)]
        for i in range(N):
            queues[i].put(phases[i])
        queues[0].put(0)
        amplifiers = []
        for i, letter in enumerate("ABDCE"):
            name = "amplifier-" + letter
            amplifier = threading.Thread(
                name=name,
                target=intcode,
                args=(name, software.copy(), queues[i], queues[(i + 1) % N]),
            )
            amplifier.start()
            amplifiers.append(amplifier)
        for amp in amplifiers:
            amp.join()
        highest_signal = max(highest_signal, queues[0].get())
    return highest_signal


if __name__ == "__main__":
    __location__ = os.path.realpath(
        os.path.join(os.getcwd(), os.path.dirname(__file__))
    )
    with open(os.path.join(__location__, "./input.txt")) as f:
        input = [line.strip() for line in f.readlines()]
        print(f"Part1 solution : {part1(input)}")
        print(f"Part2 solution : {part2(input)}")
