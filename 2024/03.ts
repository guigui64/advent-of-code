import { log, part1, part2, readLines, sum } from "./aoc.ts";

globalThis.example = false;
const lines = readLines();
log(lines);

function compute(instructions: string) {
  return sum(
    [...instructions.matchAll(/mul\((\d{1,3}),(\d{1,3})\)/g)].map(
      ([_, a, b]) => +a * +b,
    ),
  );
}

// part1
part1(compute(lines.join("")));

// part2
const scrapedInstructions = lines
  .join("")
  .replaceAll(/don't\(\).*?do\(\)/g, "");
part2(compute(scrapedInstructions));

// From regex101:
// a*?
// Matches as few characters as possible.
// You can make any quantifier lazy by appending a question mark to it.
