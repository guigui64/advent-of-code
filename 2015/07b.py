def getsignal(key):
    op = signals[key]
    done = False
    if op.isdigit():
        return int(op)
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
    print "getsignal({}) -> {}".format(key, result & 0xFFFF)
    signals[key] = str(result & 0xFFFF)
    return result & 0xFFFF # force to unsigned 16-bit


operations = {
        "AND"   : lambda x,y: x & y,
        "OR"    : lambda x,y: x | y,
        "NOT"   : lambda x,y: ~y,
        "LSHIFT": lambda x,y: x << y,
        "RSHIFT": lambda x,y: x >> y
        }

signals = {}

f = open("07.txt", "r")
for line in f.readlines():
    op, id = line[:-1].replace(' ','').split("->")
    signals[id] = op
signals["b"] = "46065"

print getsignal("a")
