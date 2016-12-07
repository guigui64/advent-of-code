import string

f = open("08.txt", "r")
toriginal = 0
trepresentation = 0
for line in f.readlines():
    print line[:-1]
    original = len(line)-1 # - '\n'
    repr = "\"" + line[:-1].replace("\\","\\\\").replace("\"","\\\"") + "\""
    print repr
    representation = len(repr)
    print original, representation
    toriginal += original
    trepresentation += representation
print trepresentation, "-", toriginal, "=", trepresentation - toriginal
