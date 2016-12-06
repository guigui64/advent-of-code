f = open("06.txt","r")
map = {}
for line in f.readlines():
    for i in range(len(line)-1):
        if not map.has_key(i): map[i] = {}
        if not map[i].has_key(line[i]): map[i][line[i]] = 1
        else: map[i][line[i]] += 1
answer = ""
for i in range(len(map)):
    m = map[i]
    answer += sorted(m, key=m.__getitem__, reverse=False)[0]
print answer
