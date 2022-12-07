import { part1, part2, printTime, readLines, startTimer } from "./aoc.ts";

const example = false;
const lines = readLines(example);

// returns [index of counts line, count]
function countStacks(lines: string[]) {
  let i = 0;
  while (lines[i].includes("[")) {
    i++;
  }
  return [i, Math.max(...lines[i].trim().split(/\s+/).map(Number))];
}
startTimer();
const [border, count] = countStacks(lines);
// build stacks
const stacks: string[][] = [];
const stacks2: string[][] = [];
for (let stackNb = 0; stackNb < count; stackNb++) {
  stacks[stackNb] = [];
  for (let i = border - 1; i >= 0; i--) {
    const crate = lines[i].charAt(1 + stackNb * 4);
    if (crate !== " ") {
      stacks[stackNb].push(crate);
    }
  }
  stacks2[stackNb] = [...stacks[stackNb]];
}
// move crates
for (const instruction of lines.slice(border + 2)) {
  let [qty, src, dst] = instruction
    .match(/move (\d+) from (\d+) to (\d+)/)!
    .slice(1)
    .map(Number);
  src--;
  dst--;
  // CrateMover 9000 moves crates one at a time
  for (const _ of Array(qty)) {
    stacks[dst].push(stacks[src].pop()!);
  }
  // CrateMover 9001 moves crates multiple crates at once!!!
  stacks2[dst].push(...stacks2[src].splice(-qty, qty));
}
part1(stacks.map((s) => s.pop()).join(""));
part2(stacks2.map((s) => s.pop()).join(""));
printTime();
