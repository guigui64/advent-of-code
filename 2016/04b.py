f = open("04.txt", "r")
alphabet = "abcdefghijklmnopqrstuvwxyz"
for line in f.readlines():
    id = int(line.split('[')[0].rsplit('-',1)[-1])
    letters = line.split('[')[0].rsplit('-',1)[0].replace('-',' ')
    print id, letters
    newletters = ""
    for l in letters:
        if l == ' ':
            newletters += l
        else:
            idx = alphabet.index(l)
            idx = (idx+id)%len(alphabet)
            newletters += alphabet[idx]
    print "->", newletters
