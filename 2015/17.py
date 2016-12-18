from itertools import combinations

containers = []
with open("17.txt", "r") as f:
    for line in f:
        containers.append(int(line.strip()))
print(containers)

def solve(part2=False):
    count = 0
    for i in range(len(containers)):
        for c in combinations(containers, i+1):
            if sum(c) == 150:
                count += 1
        if count > 0 and part2:
            break
    return count
print(solve())
print(solve(part2=True))
