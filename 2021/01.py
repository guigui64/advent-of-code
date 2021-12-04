#! /usr/bin/env python

if __name__ == "__main__":
    file = "01.txt"
    # file = "01.ex"
    # part 1
    with open(file) as f:
        count = 0
        previous = None
        for line in f:
            depth = int(line.strip())
            if previous is not None:
                if depth > previous:
                    count += 1
            previous = depth
    print(count)
    # part 2
    with open(file) as f:
        depths = [int(line.strip()) for line in f]
        three_measurements = [sum(depths[i : i + 3]) for i in range(len(depths) - 2)]
        # print(three_measurements)
        count = 0
        previous = None
        for three in three_measurements:
            if previous is not None:
                if three > previous:
                    count += 1
            previous = three
    print(count)
