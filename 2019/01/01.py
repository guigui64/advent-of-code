import os


def fuel_for_mass(mass):
    return int(mass / 3) - 2


def part1(input):
    return sum([fuel_for_mass(mass) for mass in [int(line) for line in input]])


def recursive_fuel_for_mass(mass):
    fuel = fuel_for_mass(mass)
    if fuel > 0:
        return fuel + recursive_fuel_for_mass(fuel)
    else:
        return 0


def part2(input):
    fuel = 0
    for mass in [int(line) for line in input]:
        fuel += recursive_fuel_for_mass(mass)
    return fuel


if __name__ == "__main__":
    __location__ = os.path.realpath(
        os.path.join(os.getcwd(), os.path.dirname(__file__))
    )
    with open(os.path.join(__location__, "./input.txt")) as f:
        input = [line.strip() for line in f.readlines()]
        print(f"Part1 solution : {part1(input)}")
        print(f"Part2 solution : {part2(input)}")
