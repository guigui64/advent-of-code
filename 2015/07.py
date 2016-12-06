def getsignal(key):
    if not signals.has_key(key):
        signals[key] = 0
    return signals[key]

f = open("07.txt", "r")

operations = {
        "AND"   : lambda x,y: x & y,
        "OR"    : lambda x,y: x | y,
        "NOT"   : lambda x,y: ~y,
        "LSHIFT": lambda x,y: x << y,
        "RSHIFT": lambda x,y: x >> y
        }

signals = {}

for line in f.readlines():
    op, id = line[:-1].replace(' ','').split("->")
    done = False
    for operation in operations:
        if operation in op:
            loperand, roperand = op.split(operation)
            if roperand.isalpha():
                roperand = getsignal(roperand)
            else:
                roperand = int(roperand)
            if loperand == '':
                loperand = 0
            elif loperand.isalpha():
                loperand = getsignal(loperand)
            else:
                loperand = int(loperand)
            result = operations[operation](loperand, roperand)
            done = True
    if not done:
        if op.isalpha():
            result = getsignal(op)
        else:
            result = int(op)
    getsignal(id)
    signals[id] = result & 0xFFFF # force to unsigned 16-bit

for key in sorted(signals):
    print key, ":", signals[key]

# TODO : recursive funtion
