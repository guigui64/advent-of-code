#!/usr/bin/env python

import re
from collections import Counter

pattern = re.compile(r"(.*) \(contains (.*)\)")


def solve(fname):
    # allergens is a dict of sets of ingredients per allergen
    allergens = {}
    # ingredients is a Counter of the ingredients
    ingredients = Counter()
    with open(fname) as f:
        for line in f:
            i_ingredients, i_allergens = pattern.fullmatch(line[:-1]).group(1, 2)
            i_ingredients = i_ingredients.split()
            i_allergens = i_allergens.split(", ")
            for allergen in i_allergens:
                if allergen in allergens:
                    allergens[allergen] = allergens[allergen] & set(i_ingredients)
                else:
                    allergens[allergen] = set(i_ingredients)
            for ing in i_ingredients:
                ingredients[ing] += 1
    # safe ingredients are ingredients that cannot have any of the allergens found
    safe_ingredients = set(ingredients)
    for ing in allergens.values():
        safe_ingredients -= ing
    # answer to part1 is the number of times all safe ingredients where found
    part1 = str(sum(ingredients[ing] for ing in safe_ingredients))
    # remove safe ingredients from allergens
    for ing in allergens.values():
        ing -= safe_ingredients
    # eliminate
    allergens_final = {}  # dict whose key is NOW the ingredient
    while len(allergens) > 0:
        for allergen in allergens:
            allergens[allergen] -= set(allergens_final.keys())
            if len(ing := allergens[allergen]) == 1:
                allergens_final[list(ing)[0]] = allergen
                del allergens[allergen]
                break
    # answer to part 2 is the canonical dangerous ingredient list sorted alphabetically by their
    # allergen
    part2 = ",".join(ing for ing in sorted(allergens_final, key=allergens_final.get))
    return part1, part2


if __name__ == "__main__":
    print("\n".join(" ".join(z) for z in zip(("part1:", "part2:"), solve("21ex.txt"))))
    print("\n".join(" ".join(z) for z in zip(("part1:", "part2:"), solve("21.txt"))))
