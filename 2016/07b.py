f = open("07.txt","r")
count = 0
for line in f.readlines():
    found = False
    segments = line[:-1].replace("[","]").split("]")
    for s in range(0,len(segments),2): # even segments : look for ABA
        segment = segments[s]
        for i in range(len(segment)-2):
            if segment[i] != segment[i+1] and segment[i] == segment[i+2]:
                aba = segment[i:i+3]
                bab = aba[1]+aba[0]+aba[1]
                for t in range(1,len(segments),2): # odd segments : look for corresponding BAB
                    if bab in segments[t]:
                        print line[:-1]
                        print "found ABA", aba, "and BAB", bab
                        found = True
                        break
                if found:
                    break
        if found:
            break
    if found: 
        count += 1
print count
