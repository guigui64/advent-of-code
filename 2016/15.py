def compute_pos(disc, time):
    return (disc[1] + time) % disc[0]

def solve(discs):
    time = 0
    while True:
        get = True
        subtime = time + 1
        for d in discs:
            if compute_pos(discs[d], subtime) != 0:
                time += 1
                get = False
                break
            else:
                subtime += 1
        if get:
            return time
            break

if __name__ == '__main__':
    discs = {
        1: [13, 10],
        2: [17, 15],
        3: [19, 17],
        4: [ 7,  1],
        5: [ 5,  0],
        6: [ 3,  1]
    }
    print(solve(discs))

    discs[7] = [11,  0]
    print(solve(discs))
