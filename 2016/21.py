from itertools import permutations

def swap_pos(s, x, y):
    x, y = sorted((x, y))
    return s[:x] + s[y] + s[x+1:y] + s[x] + s[y+1:]

def swap_letter(s, x , y):
    return s.replace(x, '#').replace(y, x).replace('#', y)

def rotate_left(s, x, revers=False):
    if revers:
        return rotate_right(s, x)
    else:
        x = x % len(s)
        return s[x:] + s[:x]

def rotate_right(s, x, revers=False):
    if revers:
        return rotate_left(s, x)
    else:
        x = x % len(s)
        return s[-x:] + s[:-x]

def rotate_pos_based(s, x, revers=False):
    i = s.find(x)
    if i >= 4:
        i += 1
    return rotate_right(s, i + 1, revers)

def reverse(s, x, y):
    return s[:x] + s[x:y+1][::-1] + s[y+1:]

def move(s, x, y, revers=False):
    if revers:
        x, y = y, x
    save = s[x]
    r = s[:x] + s[x+1:]
    return r[:y] + save + r[y:]

# Example
# input = "abcde"
# scrambled = input
# print(scrambled)
# scrambled = swap_pos(scrambled, 4, 0)
# print(scrambled)
# scrambled = swap_letter(scrambled, 'd', 'b')
# print(scrambled)
# scrambled = reverse(scrambled, 0, 4)
# print(scrambled)
# scrambled = rotate_left(scrambled, 1)
# print(scrambled)
# scrambled = move(scrambled, 1, 4)
# print(scrambled)
# scrambled = move(scrambled, 3, 0)
# print(scrambled)
# scrambled = rotate_pos_based(scrambled, 'b')
# print(scrambled)
# scrambled = rotate_pos_based(scrambled, 'd')
# print(scrambled)

def execute(line, scrambled, revers=False):
    if   line.startswith("swap position"):
        scrambled = swap_pos(scrambled, int(line.split()[2]), int(line.split()[5]))
    elif line.startswith("swap letter"):
        scrambled = swap_letter(scrambled, line.split()[2], line.split()[5])
    elif line.startswith("rotate left"):
        scrambled = rotate_left(scrambled, int(line.split()[2]), revers)
    elif line.startswith("rotate right"):
        scrambled = rotate_right(scrambled, int(line.split()[2]), revers)
    elif line.startswith("rotate based"):
        scrambled = rotate_pos_based(scrambled, line.split()[6], revers)
    elif line.startswith("reverse"):
        scrambled = reverse(scrambled, int(line.split()[2]), int(line.split()[4]))
    elif line.startswith("move"):
        scrambled = move(scrambled, int(line.split()[2]), int(line.split()[5]), revers)
    return scrambled

# Store lines for both parts
lines = [line.strip() for line in open("21.txt", "r").readlines()]

# Part 1
scrambled = "abcdefgh"
for line in lines:
    scrambled = execute(line, scrambled)
print(scrambled)

# Part 2

# Bugged method...
# Impossible to invert the rotate_pos_based !
# unscrambled = "fbgdceah"
# for line in lines[::-1]:
#     unscrambled = execute(line, unscrambled, revers=True)
# print(unscrambled)

# Brute force method !
scrambled = "fbgdceah"
for perm in permutations(list(scrambled)):
    scrambled2 = ''.join(perm)
    for line in lines:
        scrambled2 = execute(line, scrambled2)
    if scrambled2 == scrambled:
        print(''.join(perm))
        break
