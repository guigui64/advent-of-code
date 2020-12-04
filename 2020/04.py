#!/usr/bin/env python

import re

if __name__ == "__main__":
    passports = [
        {k: v for (k, v) in [x.split(":") for x in p]}
        for p in [e.split() for e in open("04.txt").read().split("\n\n")]
    ]
    valid1 = 0
    valid2 = 0
    required_keys = (
        "byr",
        "iyr",
        "eyr",
        "hgt",
        "hcl",
        "ecl",
        "pid",
    )  # "cid" is optional
    year = re.compile(r"\d{4}")
    patterns = {
        "byr": year,
        "iyr": year,
        "eyr": year,
        "hgt": re.compile(r"(\d+)(cm|in)"),
        "hcl": re.compile(r"#[0-9a-f]{6}"),
        "ecl": re.compile(r"(amb|blu|brn|gry|grn|hzl|oth)"),
        "pid": re.compile(r"\d{9}"),
    }
    bounds = {
        "byr": (1920, 2002),
        "iyr": (2010, 2020),
        "eyr": (2020, 2030),
        "hgt": {
            "cm": (150, 193),
            "in": (59, 76),
        },
    }
    for p in passports:
        if 7 <= len(p.keys()) <= 8 and all(k in p.keys() for k in required_keys):
            valid1 += 1
            valid = True
            for key in required_keys:
                m = patterns[key].fullmatch(p[key])
                if m is None:
                    valid = False
                    break
                if key in bounds.keys():
                    if key == "hgt":
                        unit = m.group(2)
                        value = int(m.group(1))
                        min, max = bounds["hgt"][unit]
                    else:
                        min, max = bounds[key]
                        value = int(m.group(0))
                    if not (min <= value <= max):
                        valid = False
                        break
            if valid:
                valid2 += 1
    print(valid1, "passports are valid for part 1")
    print(valid2, "passports are valid for part 2")
