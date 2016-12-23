from collections import defaultdict

instructions = [line.strip() for line in open("23.txt", "r").readlines()]

i = 0
map = defaultdict(int)
map['a'] = 7

def value(x):
    if x.isalpha():
        return map[x]
    else:
        return int(x)

while True:
    if i >= len(instructions):
        break
    inst = instructions[i]
    print(inst)
    if   inst.startswith("cpy"):
        x, y = inst.split()[1:]
        if y.isalpha():
            map[y] = value(x)
    elif inst.startswith("jnz"):
        x, y = [value(z) for z in inst.split()[1:]]
        if x != 0:
            i += y
            print(map)
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
            print(map)
            continue
        target = instructions[i + x]
        print("Target is", target)
        if target.startswith("inc"):
            target = target.replace("inc", "dec")
        elif target[:3] in ("dec", "tgl"):
            target = target.replace(target[:3], "inc")
        elif target.startswith("jnz"):
            target = target.replace("jnz", "cpy")
        else:
            target = target.replace(target[:3], "jnz")
        print("Target becomes", target)
        instructions[i + x] = target
    print(map)
    i += 1

print(map['a'])
