input = "iwrupvqb"

import hashlib

answer = 1
found5 = False
found6 = False

while not found5 or not found6:
    m = hashlib.md5()
    m.update(input + str(answer))
    hash = m.hexdigest()
    if not found5 and hash.startswith("0"*5):
        print "For five zeroes :", answer
        found5 = True
    elif not found6 and hash.startswith("0"*6):
        print "For six zeroes :", answer
        found6 = True
    answer += 1
