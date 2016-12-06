def rule(sizes):
    return      sizes[0] + sizes[1] > sizes[2] \
            and sizes[0] + sizes[2] > sizes[1] \
            and sizes[2] + sizes[1] > sizes[0]

f = open("03.txt", "r")
sizes = []
lines = f.readlines()
for i in range(0, len(lines), 3):
    sizes[i:i+2] = [[],[],[]]
    for j in range(3):
        sizes[i+0] = sizes[i+0] + [int(lines[i+j].split()[0])]
        sizes[i+1] = sizes[i+1] + [int(lines[i+j].split()[1])]
        sizes[i+2] = sizes[i+2] + [int(lines[i+j].split()[2])]
count = 0
for size in sizes:
    if rule(size): count += 1
print count
