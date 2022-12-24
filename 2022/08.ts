import { part1, part2, range, readLines } from "./aoc.ts";

const map = readLines(false);
const H = map.length;
const W = map[0].length;

enum Direction {
  TOP,
  RIGHT,
  BOTTOM,
  LEFT,
}
const dirs = [Direction.TOP, Direction.RIGHT, Direction.BOTTOM, Direction.LEFT];

function line(x: number, y: number, direction: Direction) {
  switch (direction) {
    case Direction.TOP:
      return range(x, 0)
        .map((xx) => [xx, y])
        .reverse();
    case Direction.BOTTOM:
      return range(H - x - 1, x + 1).map((xx) => [xx, y]);
    case Direction.LEFT:
      return range(y, 0)
        .map((yy) => [x, yy])
        .reverse();
    case Direction.RIGHT:
      return range(W - y - 1, y + 1).map((yy) => [x, yy]);
  }
}

let visible = 2 * W + 2 * (H - 2);
let maxScenicScore = 0;
for (let x = 1; x < W - 1; x++) {
  for (let y = 1; y < H - 1; y++) {
    const tree = parseInt(map[x][y]);
    const lines = dirs.map((dir) =>
      line(x, y, dir).map(([x, y]) => parseInt(map[x][y]))
    );
    if (lines.some((line) => line.every((t) => t < tree))) {
      visible++;
    }
    maxScenicScore = Math.max(
      maxScenicScore,
      lines
        .map((sight) => sight.findIndex((t) => t >= tree) + 1 || sight.length)
        .reduce((a, c) => a * c, 1),
    );
  }
}
part1(visible);
part2(maxScenicScore);
