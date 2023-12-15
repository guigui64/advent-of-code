import { log, part1, part2, readLines, sum } from "./aoc.ts";

globalThis.example = true;
const lines = readLines();
log(lines);

const records = lines.map((line) => {
  const [a, b] = line.split(" ");
  return [a, b.split(",").map(Number)] as const;
});
log(records);

function satisfies(seq: string, spec: number[]) {
  const val = seq
    .split(".")
    .filter((s) => s)
    .map((s) => s.length);
  return spec.length === val.length && spec.every((s, i) => s === val[i]);
}

function possibilities(pat: string): string[] {
  if (!pat.includes("?")) {
    return [pat];
  } else {
    return [
      ...possibilities(pat.replace("?", ".")),
      ...possibilities(pat.replace("?", "#")),
    ];
  }
}

// part1
part1(
  sum(
    records.map(([sequence, numbers]) => {
      return possibilities(sequence).filter((s) => satisfies(s, numbers))
        .length;
    }),
  ),
);

// part2
// const records2 = records.map(
//   ([sequence, numbers]) =>
//     [
//       (sequence + "?").repeat(5).slice(0, -1),
//       Array(5).fill(numbers).flat(),
//     ] as const,
// );
// log(records2);
//
// part2(
//   sum(
//     records2.map(([sequence, numbers]) => {
//       return possibilities(sequence).filter((s) => satisfies(s, numbers))
//         .length;
//     }),
//   ),
// );
part2("out of memory...");
