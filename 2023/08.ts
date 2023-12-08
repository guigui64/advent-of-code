import { log, part1, part2, readLines } from "./aoc.ts";
import { lcm } from "./math.ts";

globalThis.example = false;
const lines = readLines();
log(lines);

const directions = lines[0].split("");
const network = new Map(
  lines.slice(2).map((line) => {
    const m = /(.*) = \((.*), (.*)\)/.exec(line);
    return [m![1], [m![2], m![3]]];
  }),
);
log(network);

function solve(start?: string): number {
  let current = start ? start + "A" : "AAA";
  let idx = 0;
  const endCondition = (c: string) => (start ? c.endsWith("Z") : c === "ZZZ");
  while (!endCondition(current)) {
    const [l, r] = network.get(current)!;
    const dir = directions[idx % directions.length];
    if (dir === "R") {
      current = r;
    } else {
      current = l;
    }
    idx++;
  }
  return idx;
}

// part1
part1(solve());

// part2
const solutions = [...network.keys()]
  .filter((k) => k.endsWith("A"))
  .map((s) => solve(s.slice(0, -1)));
log(solutions);
part2(solutions.reduce(lcm));
