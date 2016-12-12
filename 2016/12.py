f = open("12.txt", "r")

map = {}
lines = f.readlines()
i = 0
while True:
    line = lines[i]
    if line.startswith("cpy"):
        x,y = line[4:].split()
        if not map.has_key(y):
            map[y] = 0
        if x.isdigit():
            map[y] = int(x)
        else:
            map[y] = map[x]
    elif line.startswith("inc"):
        x = line[4:].split()[0]
        if not map.has_key(x):
            map[x] = 0
        map[x] += 1
    elif line.startswith("dec"):
        x = line[4:].split()[0]
        if not map.has_key(x):
            map[x] = 0
        map[x] -= 1
    else:
        x,y = line[4:].split()
        if x.isalpha() and not map.has_key(x):
            map[x] = 0
        if not((x.isdigit() and int(x) == 0) or (not x.isdigit() and map[x] == 0)):
            i += int(y)
            continue
    i += 1
    print(map)

print(map)
