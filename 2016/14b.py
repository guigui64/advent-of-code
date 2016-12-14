from hashlib import md5

input = "jlmsuwbz"
#input = "abc"

def findletterntimes(str, n):
    for i in range(len(str) - n + 1):
        if str[i]*n == str[i:i+n]:
            return str[i]
    return None

# list structure:
# "x" string, id, validated
candidates = []

# list of valid ids
validhashes = []

i = 0
while len(validhashes) < 64:
    hash = md5("{}{}".format(input,i).encode()).hexdigest()
    for _ in range(2016):
        hash = md5(hash.encode()).hexdigest()
    letter = findletterntimes(hash, 3)
    if letter:
        # print(hash)
        # print("found 3", letter)
        # print(i, "is candidate")
        candidates.append([letter, i, False])
    for c in candidates:
        if not c[2] and c[0]*5 in hash and i in range(c[1] + 1, c[1] + 1000 + 1):
            # print(hash)
            # print("found 5", letter)
            validhashes.append(c[1])
            c[2] = True
            print("{} - hash {} validates {} with char {}".format(len(validhashes), i, c[1], c[0]))
    i += 1

print(validhashes)
print(validhashes[63])
