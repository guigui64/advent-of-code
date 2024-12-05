import { directions, equal, log, part1, part2, readLines } from "./aoc.ts";

globalThis.example = false;
const grid = readLines();
log(grid);

let count = 0;

function findXMAS(x: number, y: number) {
  const MAS = ["M", "A", "S"];
  return directions().filter(([dx, dy]) => {
    return equal(
      [
        grid[y + dy]?.[x + dx],
        grid[y + dy * 2]?.[x + dx * 2],
        grid[y + dy * 3]?.[x + dx * 3],
      ],
      MAS,
    );
  }).length;
}

for (let y = 0; y < grid.length; y++) {
  for (let x = 0; x < grid[y].length; x++) {
    if (grid[y][x] === "X") {
      count += findXMAS(x, y);
    }
  }
}

part1(count);

count = 0;

function findX_MAS(x: number, y: number) {
  const MS = ["M", "S"];
  if (
    equal([grid[y - 1]?.[x - 1], grid[y + 1]?.[x + 1]].toSorted(), MS) &&
    equal([grid[y - 1]?.[x + 1], grid[y + 1]?.[x - 1]].toSorted(), MS)
  ) {
    return 1;
  }
  return 0;
}

for (let y = 0; y < grid.length; y++) {
  for (let x = 0; x < grid[y].length; x++) {
    if (grid[y][x] === "A") {
      count += findX_MAS(x, y);
    }
  }
}

part2(count);
