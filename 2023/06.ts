import { log, part1, part2, product } from "./aoc.ts";

globalThis.verbose = true;
// const lines = readLines();
// log(lines);
console.time("took");

const inEx = [
  [7, 15, 30],
  [9, 40, 200],
];
const in1 = [
  [56, 71, 79, 99],
  [334, 1135, 1350, 2430],
];
const in2 = [[56717999], [334113513502430]];

function solve(input: number[][]) {
  const possibilities: number[] = [];
  for (let i = 0; i < input[0].length; i++) {
    const time = input[0][i];
    const distance = input[1][i];
    let count = 0;
    let held = 0;
    while (held++ < time) {
      const speed = held;
      const remaining = time - held;
      const travelled = speed * remaining;
      if (travelled > distance) {
        count++;
      }
    }
    possibilities.push(count);
  }
  return product(possibilities);
}

log(solve(inEx));

// part1
part1(solve(in1));

// part2
part2(solve(in2));
