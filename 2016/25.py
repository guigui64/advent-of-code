from collections import defaultdict

def value(x):
    if x.isalpha():
        return map[x]
    else:
        return int(x)

def solve(map):
    instructions = [line.strip() for line in open("25.txt", "r").readlines()]
    i = 0
    out = 1
    while True:
        if i >= len(instructions):
            break
        inst = instructions[i]
        if   inst.startswith("cpy"):
            x, y = inst.split()[1:]
            if y.isalpha():
                map[y] = value(x)
        elif inst.startswith("jnz"):
            x, y = [value(z) for z in inst.split()[1:]]
            if x != 0:
                i += y
                continue
        elif inst.startswith("inc"):
            x = inst.split()[1]
            if x.isalpha():
                map[x] += 1
        elif inst.startswith("dec"):
            x = inst.split()[1]
            if x.isalpha():
                map[x] -= 1
        elif inst.startswith("tgl"):
            x = inst.split()[1]
            x = value(x)
            if (i + x) < 0 or (i + x) >= len(instructions):
                i += 1
                continue
            target = instructions[i + x]
            if target.startswith("inc"):
                target = target.replace("inc", "dec")
            elif target[:3] in ("dec", "tgl"):
                target = target.replace(target[:3], "inc")
            elif target.startswith("jnz"):
                target = target.replace("jnz", "cpy")
            else:
                target = target.replace(target[:3], "jnz")
            instructions[i + x] = target
        elif inst.startswith("out"):
            x = inst.split()[1]
            x = value(x)
            if x == (out + 1) % 2:
                out = x
            else:
                return False
        i += 1

# Part 1
a = 1
while True:
    map = defaultdict(int)
    map['a'] = a
    print("Testing", a)
    if not solve(map):
        print("Wrong !")
        a += 1
