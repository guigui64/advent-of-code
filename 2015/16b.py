machine = {
    "children": 3,
    "cats": 7,
    "samoyeds": 2,
    "pomeranians": 3,
    "akitas": 0,
    "vizslas": 0,
    "goldfish": 5,
    "trees": 3,
    "cars": 2,
    "perfumes": 1
}

with open("16.txt", "r") as f:
    for line in f:
        number = int(line.split(':')[0].split()[1])
        found = True
        for s in line.split(':', 1)[1].split(','):
            key, quantity = [s.strip() for s in s.split(':')]
            quantity = int(quantity)
            if key in ["cats", "trees"]:
                if machine[key] >= quantity:
                    found = False
                    break
            elif key in ["pomeranians", "goldfish"]:
                if machine[key] <= quantity:
                    found = False
                    break
            else:
                if machine[key] != quantity:
                    found = False
                    break
        if found:
            print(number)
            break
