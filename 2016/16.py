def checksum(str):
    cs = ""
    for i in range(0, len(str), 2):
        if str[i] == str[i+1]:
            cs += "1"
        else:
            cs += "0"
    return cs

def solve(size):

    dragon = "10001001100000001"

    while len(dragon) < size:
        a = dragon
        b = a[::-1].replace('1', '#').replace('0', '1').replace('#', '0')
        dragon = a + "0" + b

    dragon = dragon[:size]
    cs = checksum(dragon)
    while len(cs) % 2 == 0:
        cs = checksum(cs)

    return cs

if __name__ == '__main__':
    print(solve(272))
    print(solve(35651584))
