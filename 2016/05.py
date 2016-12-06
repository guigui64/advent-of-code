input = "uqwqemis"

import hashlib

code = ""
index = 0

while len(code) < 8:
    while True:
        m = hashlib.md5()
        m.update(input + str(index))
        hash = m.hexdigest()
        if hash.startswith("0"*5):
            code += str(hash[5])
            print index, hash, code
            index += 1
            break
        index += 1

print "DONE :", code
