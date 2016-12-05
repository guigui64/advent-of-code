def rule1(s):
    for i in range(len(s) - 1):
        if s.count(s[i:i+2]) >= 2:
            print "[rule1] found", s[i:i+2], "at least twice"
            return True
    return False

def rule2(s):
    for i in range(len(s) - 2):
        if s[i] == s[i+2]:
            print "[rule2] found", s[i:i+3]
            return True
    return False

f = open("05.txt","r")
count = 0
for line in f.readlines():
    print line
    if rule1(line) and rule2(line): count += 1
print count
