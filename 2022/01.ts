import { part1, part2, read } from "./aoc.ts";
import { sum } from "https://deno.land/x/sum@v1.1.0/mod.ts";
import { Direction, SortService } from "https://deno.land/x/sort@v1.1.1/mod.ts";

const groups = read().split("\n\n");
let sums = groups.map((group) => {
  const calories = group.split("\n").map(Number);
  return sum(calories);
});
sums = SortService.sort(sums, Direction.DESCENDING);

part1(sums[0]);
part2(sum(sums.slice(0, 3)));
