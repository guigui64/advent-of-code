# from https://www.reddit.com/user/joshbduncan/

from collections import defaultdict
import time

start = time.time_ns()

data = open("07.txt").read().strip()
sizes = defaultdict(int)
path = []
for line in data.split("\n"):
    if line.startswith("$ cd"):
        d = line.split()[2]
        if d == "/":
            path.append("/")
        elif d == "..":
            path.pop()
        else:
            path.append(f"{path[-1]}{'/' if path[-1] != '/' else ''}{d}")
    if line[0].isnumeric():
        for p in path:
            sizes[p] += int(line.split()[0])

print(f"Part 1: {sum(s for s in sizes.values() if s <= 100_000)}")
print(f"Part 2: {min(s for s in sizes.values() if s >= 30_000_000 - (70_000_000 - sizes['/']))}")
print((time.time_ns() - start) / 1e6, "ms")
