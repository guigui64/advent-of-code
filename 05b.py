input = "uqwqemis"

import hashlib

code = ['']*8
chars_found = 0
index = 0

while chars_found < 8:
    m = hashlib.md5()
    m.update(input + str(index))
    hash = m.hexdigest()
    if hash.startswith("0"*5) and hash[5] in "01234567" and code[int(hash[5])] == '':
        code[int(hash[5])] = hash[6]
        chars_found += 1
        print code
    index += 1

print "DONE :", ''.join(code)
