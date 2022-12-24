import { part1, part2, read, sum } from "./aoc.ts";

const groups = read().split("\n\n");
const sums = groups.map((group) => {
  const calories = group.split("\n").map(Number);
  return sum(calories);
});
sums.sort((a, b) => b - a);

part1(sums[0]);
part2(sum(sums.slice(0, 3)));
