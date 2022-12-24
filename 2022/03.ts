import { part1, part2, readLines } from "./aoc.ts";

const lines = readLines(false);

function priority(letter: string) {
  return "0abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ".indexOf(
    letter,
  );
}

let p1 = 0;
for (const line of lines) {
  const first = line.slice(0, line.length / 2);
  for (const l of first) {
    if (line.includes(l, line.length / 2)) {
      p1 += priority(l);
      break;
    }
  }
}
part1(p1);

let p2 = 0;
for (let i = 0; i < lines.length - 2; i += 3) {
  for (const l of lines[i]) {
    if (lines[i + 1].includes(l) && lines[i + 2].includes(l)) {
      p2 += priority(l);
      break;
    }
  }
}
part2(p2);
