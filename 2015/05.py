vowels = "aeiou"
forbidden = ["ab", "cd", "pq", "xy"]

def rule1(s):
    nb = 0
    for c in s:
        if c in vowels:
            nb += 1
    #print "[rule1] nb=", nb
    return nb >= 3

def rule2(s):
    previous = s[0]
    for current in s[1:]:
        if current == previous:
            #print "[rule2] Found", current, "that appears twice"
            return True
        else:
            previous = current
    return False

def rule3(s):
    for f in forbidden:
        if f in s:
            #print "[rule3] Found forbidden", f
            return False
    return True

def is_nice(s):
    return rule1(s) and rule2(s) and rule3(s)

count = 0
f = open("05.txt", "r")
for s in f.readlines():
    if is_nice(s):
        count += 1

print count
