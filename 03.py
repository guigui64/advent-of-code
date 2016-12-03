def rule(sizes):
    return      sizes[0] + sizes[1] > sizes[2] \
            and sizes[0] + sizes[2] > sizes[1] \
            and sizes[2] + sizes[1] > sizes[0]

f = open("03.txt", "r")

count = 0
for line in f.readlines():
    sizes = [int(s) for s in line.split()]
    if rule(sizes): count += 1
print count
