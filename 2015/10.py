input = "3113322113"

next = input
#print(next)
for t in range(50):
    previous = next
    next = ""
    i = 0
    s = 1
    while True:
        if i == len(previous):
            break
        if i + 1 != len(previous) and previous[i+1] == previous[i]:
            i += 1
            s += 1
        else:
            next += str(s) + previous[i]
            i += 1
            s = 1
    #print(next)
    if t == 39:
        print(len(next))
print(len(next))
