from itertools import permutations
from collections import defaultdict
from re import findall

def possibilities(ingredients):
    possibilities = []
    for i in range(0,101):
        for j in range(0,101-i):
            for k in range(0,101-(i+j)):
                possibilities.append(
                    (
                        (ingredients[0], i),
                        (ingredients[1], j),
                        (ingredients[2], k),
                        (ingredients[3], 100-(i+j+k))
                    )
                )
    return possibilities

ingredients = defaultdict(lambda : defaultdict(int))
with open("15.txt", "r") as f:
    for line in f:
        name = line.split(':')[0]
        ingredients[name]["capacity"], \
            ingredients[name]["durability"], \
            ingredients[name]["flavor"], \
            ingredients[name]["texture"], \
            ingredients[name]["calories"] = [int(s) for s in findall(r"-?\d+", line)]

highest = 0
for perm in permutations(ingredients):
    for sol in possibilities(perm):
        subscore = 0
        for s in sol:
            ing, spoons = s
            if spoons == 0:
                subscore = 1
                break
            subscore += ingredients[ing]["calories"]*spoons
        if subscore != 500:
            continue
        score = 1
        for property in ["capacity", "durability", "flavor", "texture"]:
            subscore = 0
            for s in sol:
                ing, spoons = s
                if spoons == 0:
                    subscore = 1
                    break
                subscore += ingredients[ing][property]*spoons
            subscore = max(subscore, 0)
            score *= subscore
        highest = max(highest, score)

print(highest)
