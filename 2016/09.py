def decompress(s, version="One"):
    if '(' not in s: return len(s)
    ret = 0
    while '(' in s:
        ret += s.find('(')
        s = s[s.find('('):]
        chars, times = [int(c) for c in s[1:s.find(')')].split('x')]
        s = s[s.find(')')+1:]
        if version == "One":
            ret += chars * times
        else:
            ret += decompress(s[:chars], "Two") * times
        s = s[chars:]
    ret += len(s)
    return ret


f = open("09.txt", "r")
line = f.readline()[:-1]
#line = "X(8x2)(3x3)ABCY"

print(decompress(line, "One"))
print(decompress(line, "Two"))

