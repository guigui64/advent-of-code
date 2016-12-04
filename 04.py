f = open("04.txt", "r")
sum = 0
for line in f.readlines():
    checksum = line.split('[')[1].strip()[:-1]
    id = int(line.split('[')[0].rsplit('-',1)[-1])
    letters = line.split('[')[0].rsplit('-',1)[0].replace('-','')
    map = {}
    for l in letters:
        if map.has_key(l): map[l] += 1
        else: map[l] = 1
    sorted_list = sorted(map, key=map.__getitem__, reverse=True)
    for i in range(len(sorted_list) - 1):
        if map[sorted_list[i]] == map[sorted_list[i+1]] \
                and sorted_list[i] > sorted_list[i+1]:
            tmp = sorted_list[i]
            sorted_list[i] = sorted_list[i+1]
            sorted_list[i+1] = tmp
    real_checksum = ''.join(sorted_list[:5])
    if (real_checksum == checksum): sum += id
print sum
