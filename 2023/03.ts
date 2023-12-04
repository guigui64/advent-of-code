import { log, part1, part2, product, range, readLines, sum } from "./aoc.ts";

globalThis.example = false;
// globalThis.verbose = true;
const lines = readLines();
log(lines);
const symbols = lines
  .map((line, y) =>
    [...line.matchAll(/[^.\d]/g)].map((match) => ({
      char: match[0],
      x: match.index!,
      y,
    })),
  )
  .flat();
log(symbols);
const parts = lines
  .map((line, y) =>
    [...line.matchAll(/\d+/dg)].map((match) => ({
      id: +match[0],
      xmin: match.indices![0][0],
      xmax: match.indices![0][1],
      y,
    })),
  )
  .flat();
log(parts);

// xmin incl
// xmax excl
function adjacent(xmin: number, xmax: number, y: number) {
  return range(xmax - xmin + 2, xmin - 1)
    .map((x) => range(3).map((dy) => [x, y + dy - 1]))
    .flat();
}

// part1
part1(
  sum(
    parts
      .filter((p) =>
        adjacent(p.xmin, p.xmax, p.y).some(([ax, ay]) =>
          symbols.some(({ x, y }) => x === ax && y === ay),
        ),
      )
      .map((p) => p.id),
  ),
);

// part2
const ratios = symbols
  .filter((s) => s.char === "*")
  .map((s) => {
    const adjParts = parts
      .filter((p) =>
        adjacent(p.xmin, p.xmax, p.y).some(
          ([ax, ay]) => s.x === ax && s.y === ay,
        ),
      )
      .map((p) => p.id);
    if (adjParts.length === 2) {
      return product(adjParts);
    } else {
      return 0;
    }
  });
part2(sum(ratios));
