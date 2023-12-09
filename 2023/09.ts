import { log, part1, part2, readLines, sum } from "./aoc.ts";

globalThis.example = false;
const lines = readLines();
log(lines);

const sequences = lines.map((line) => line.split(" ").map(Number));

function findNext(sequence: number[]): number {
  const differences: number[] = [];
  for (let i = 0; i < sequence.length - 1; i++) {
    differences.push(sequence[i + 1] - sequence[i]);
  }
  if (differences.slice(1).every((d) => d === differences[0])) {
    return sequence[sequence.length - 1] + differences[0];
  } else {
    return sequence[sequence.length - 1] + findNext(differences);
  }
}

part1(sum(sequences.map(findNext)));
part2(sum(sequences.map((s) => s.toReversed()).map(findNext)));
