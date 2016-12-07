f = open("07.txt","r")
count = 0
for line in f.readlines():
    found = [False, False] # Good segments (even), bad segments (odd)
    segments = line[:-1].replace("[","]").split("]")
    for s in range(len(segments)):
        if found[s%2]:
            continue
        segment = segments[s]
        for i in range(len(segment)-3):
            if segment[i] != segment[i+1] and segment[i] == segment[i+3] and segment [i+1] == segment[i+2]:
                found[s%2] = True
                break
    if found[0] and not found[1]: 
        count += 1
print count
