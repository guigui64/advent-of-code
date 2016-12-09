alphabet = "abcdefghijklmnopqrstuvwxyz"

# passwd must be a list
def incr(passwd):
    for i in range(len(passwd)-1,-1,-1):
        j = alphabet.find(passwd[i])
        if j == len(alphabet)-1:
            passwd[i] = alphabet[0]
            # continue with previous char
        else:
            passwd[i] = alphabet[j+1]
            break

# s must be a str
def rule1(s):
    for i in range(len(alphabet)-2):
        if alphabet[i:i+3] in s:
            return True
    return False

# s must be a str
def rule2(s):
    for l in "iol":
        if l in s:
            return False
    return True

# s must be a str
def rule3(s):
    count = 0
    for i in range(len(alphabet)):
        count += 1 if s.find(alphabet[i]*2) != -1 else 0
    return count >= 2

if __name__ == "__main__":
    input = list("cqjxjnds")
    found = 0
    while True:
        incr(input)
        s = ''.join(input)
        if rule1(s) and rule2(s) and rule3(s):
            print(s)
            found += 1
            if found == 2:
                break

