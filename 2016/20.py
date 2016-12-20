MIN = 0
MAX = 4294967295

def get_range(line):
    return list(map(int, line.split('-')))

with open("20.txt", "r") as f:
    ranges = sorted([get_range(line.strip()) for line in f])

count = 0
imin, imax = ranges[0]
first_found = None
for r in ranges[1:]:
    if imin > MIN:
        if first_found is None:
            first_found = MIN
        count += imin - MIN
    if r[0] <= imax + 1:
        imax = max(imax, r[1])
    else:
        if first_found is None:
            first_found = imax + 1
        count += r[0] - imax - 1
        imax = r[1]
if imax < MAX:
    if first_found is None:
        first_found = imax + 1
    count += MAX - imax

print(first_found)
print(count)
