import md5

#input = "jlmsuwbz"
input = "abc"

def findletterntimes(str, n):
    for i in range(len(str) - n + 1):
        if str[i]*n == str[i:i+n]:
            return str[i]
    return None

# list structure:
# "x" string, id, order id
candidates = []

# list of valid ids
validhashes = []

i = 0
order = 0
while len(validhashes) < 64:
    hash = md5.new(input + str(i)).hexdigest()
    letter = findletterntimes(hash, 3)
    if letter:
        # print(hash)
        # print("found 3", letter)
        # print(i, "is candidate")
        candidates.append([letter, i, order])
        order += 1
    for c in candidates:
        if c[0]*5 in hash and i in range(c[1] + 1, c[1] + 1000 + 1):
            # print(hash)
            # print("found 5", letter)
            # print(c[1], "is valid")
            validhashes.append([c[1], c[2]])
            candidates.remove(c)
    i += 1

print(validhashes)
print(validhashes[64])
