import { count, log, part1, part2, readLines, sum } from "./aoc.ts";

globalThis.example = false;
globalThis.verbose = false;
const lines = readLines();
log(lines);

// part1
const [left, right] = lines
  .map((line) => line.split(/\s+/))
  .reduce(
    ([left, right], [a, b]) =>
      [
        [...left, +a],
        [...right, +b],
      ] as [number[], number[]],
    [[], []] as [number[], number[]],
  )
  .map((s) => s.toSorted());
part1(sum(left.map((_, i) => Math.abs(left[i] - right[i]))));

// part2
const counter = count(right);
part2(sum(left.map((l) => l * counter.get(l))));
