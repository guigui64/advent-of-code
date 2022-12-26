// https://www.reddit.com/r/adventofcode/comments/zv4ixy/my_daughter_made_me_my_own_advent_of_code/

import { part1, part2, readLines } from "./aoc.ts";

const example = false;
const lines = readLines(example);
const letters: string[] = [];
const numbers: string[] = [];
lines[0]
  .slice(0, -1)
  .split("")
  .forEach((c, i) => {
    if (/[A-Z-]/.test(c) && lines[0][i + 1] === c) {
      letters.push(c);
    }
    if (/[0-9]/.test(c) && lines[0][i + 1] === c) {
      numbers.push(c);
    }
  });

// part1
part1(letters.join(""));

// part2
part2(numbers.join(""));
