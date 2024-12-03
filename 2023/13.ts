import { log, part1, part2, read, sum } from "./aoc.ts";

globalThis.example = false;
const patterns = read()
  .slice(0, -1)
  .split("\n\n")
  .map((s) => s.split("\n"));
log(patterns);

function findHorizontalReflection(pattern: string[]) {
  for (let y = 1; y < pattern.length - 1; y++) {
    let reflects = true;
    for (let dy = 1; y + dy < pattern.length && y - dy + 1 >= 0; dy++) {
      if (pattern[y + dy] !== pattern[y - dy + 1]) {
        reflects = false;
        break;
      }
    }
    if (reflects) {
      return y + 1;
    }
  }
  return 0;
}

function findVerticalReflection(pattern: string[]) {
  const rotatedPattern: string[] = [];
  for (let x = 0; x < pattern[0].length; x++) {
    rotatedPattern[x] = "";
    for (let y = 0; y < pattern.length; y++) {
      rotatedPattern[x] += pattern[y][x];
    }
  }
  return findHorizontalReflection(rotatedPattern);
}

// part1
part1(
  sum(patterns.map((pattern) => findVerticalReflection(pattern))) +
    100 * sum(patterns.map((pattern) => findHorizontalReflection(pattern))),
);

// part2
part2("TODO");
