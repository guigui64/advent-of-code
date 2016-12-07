import string

f = open("08.txt", "r")
tcode = 0
tmemory = 0
for line in f.readlines():
    print line[:-1]
    code = len(line)-1 # - '\n'
    line = line[1:-2]
    while True:
        idx = line.find("\\")
        if idx == -1:
            break
        if line[idx+1] == '\\' or line[idx+1] == '\"':
            line = line[:idx] + '_' + line[idx+2:]
        elif line[idx+1] == 'x' and line[idx+2] in string.hexdigits and line[idx+3] in string.hexdigits:
            line = line[:idx] + '_' + line[idx+4:]
    memory = len(line)
    print line, code, memory
    tcode += code
    tmemory += memory
print tcode, "-", tmemory, "=", tcode - tmemory
