from itertools import permutations
from collections import defaultdict

people = set()
dict = defaultdict(int)

with open("13.txt", "r") as f:
    for line in f:
        A, _, gain, happiness, _, _, _, _, _, _, B = line[:-2].split()
        if gain == "lose":
            happiness = - int(happiness)
        else:
            happiness = int(happiness)
        print(A, happiness, B)
        people.add(A)
        people.add(B)
        dict[(A, B)] = happiness

def solve():
    optimal = -99999999999999999
    for solution in permutations(people):
        total = 0
        for i in range(len(solution)):
            A = solution[i]
            if i == len(solution) - 1:
                B = solution[0]
            else:
                B = solution[i+1]
            total += dict[(A, B)] + dict[(B, A)]
        if total > optimal:
            optimal = total
            best = solution
    return best, optimal

print(solve())
for p in people:
    dict[("Me", p)] = 0
    dict[(p, "Me")] = 0
people.add("Me")
print(solve())
