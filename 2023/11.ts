import {
  combinations,
  log,
  manhattan,
  part1,
  part2,
  readLines,
  sum,
} from "./aoc.ts";

globalThis.example = false;
// globalThis.verbose = true;
const lines = readLines();
log(lines);

const universe = lines.map((line) => line.split(""));
const expandedRows = universe
  .map((row, i) => [row, i] as const)
  .filter(([row, _]) => !row.includes("#"))
  .map(([_, i]) => i);
const expandedCols: number[] = [];
for (let i = 0; i < universe[0].length; i++) {
  if (universe.every((row) => row[i] === ".")) {
    expandedCols.push(i);
  }
}

const galaxiesCoords = (incBy = 1) =>
  universe
    .map(
      (row, y) =>
        row
          .map((cell, x) => (cell === "#" ? [x, y] : null))
          .filter((coord) => coord !== null) as number[][],
    )
    .flat()
    .map(([x, y]) => {
      y += incBy * expandedRows.filter((ey) => ey < y).length;
      x += incBy * expandedCols.filter((ex) => ex < x).length;
      return [x, y];
    });

// part1
part1(sum(combinations(galaxiesCoords()).map(([g1, g2]) => manhattan(g1, g2))));

// part2
part2(
  sum(
    combinations(galaxiesCoords(1_000_000 - 1)).map(([g1, g2]) =>
      manhattan(g1, g2),
    ),
  ),
);
