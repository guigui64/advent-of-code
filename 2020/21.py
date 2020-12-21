#!/usr/bin/env python

import re
from collections import defaultdict, Counter

pattern = re.compile(r"(.*) \(contains (.*)\)")


def solve(fname):
    # allergens is a dict of lists of ingredients list per allergen
    allergens = defaultdict(list)
    # ingredients is a Counter of the ingredients
    ingredients = Counter()
    with open(fname) as f:
        for line in f:
            i_ingredients, i_allergens = pattern.fullmatch(line[:-1]).group(1, 2)
            i_ingredients = i_ingredients.split()
            i_allergens = i_allergens.split(", ")
            for allergen in i_allergens:
                allergens[allergen] += [i_ingredients]
            for ing in i_ingredients:
                ingredients[ing] += 1
    # filter allergens by intersecting their ingredients lists
    allergens_filtered = {}
    for allergen, ing_list in allergens.items():
        filtered = set(ing_list[0])
        for ings in ing_list[1:]:
            filtered.intersection_update(set(ings))
        allergens_filtered[allergen] = filtered
    # safe ingredients are ingredients that cannot have any of the allergens found
    safe_ingredients = set(ingredients)
    for ing in allergens_filtered.values():
        safe_ingredients.difference_update(ing)
    # answer to part1 is the number of times all safe ingredients where found
    part1 = str(sum(ingredients[ing] for ing in safe_ingredients))
    # remove safe ingredients from allergens
    for allergen, ing in allergens_filtered.items():
        ing.difference_update(safe_ingredients)
    # eliminate
    allergens_final = {}  # dict whose key is NOW the ingredient
    while len(allergens := allergens_filtered.keys()) > 0:
        for allergen in allergens:
            allergens_filtered[allergen].difference_update(allergens_final.keys())
            if len(ing := allergens_filtered[allergen]) == 1:
                allergens_final[list(ing)[0]] = allergen
                del allergens_filtered[allergen]
                break
    # answer to part 2 is the canonical dangerous ingredient list sorted alphabetically by their
    # allergen
    part2 = ",".join(
        ing for ing, _ in sorted(allergens_final.items(), key=lambda t: t[1])
    )
    return part1, part2


if __name__ == "__main__":
    print("\n".join(" ".join(z) for z in zip(("part1:", "part2:"), solve("21ex.txt"))))
    print("\n".join(" ".join(z) for z in zip(("part1:", "part2:"), solve("21.txt"))))
