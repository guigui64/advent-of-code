import { log, part1, part2, readLines, sum } from "./aoc.ts";

globalThis.example = false;
const lines = readLines();
log(lines);
const sequences = lines[0].split(",");

function hash(sequence: string): number {
  return sequence.split("").reduce((a, c) => {
    return ((a + c.charCodeAt(0)) * 17) % 256;
  }, 0);
}

// part1
part1(sum(sequences.map(hash)));

// part2
part2("TODO");
