import { Point, log, part1, part2, readLines } from "./aoc.ts";

globalThis.example = false;
const lines = readLines();
log(lines);

function mod(n: number, m: number) {
  return ((n % m) + m) % m;
}

const MAP = lines.map((l) => l.split(""));

const down = [0, 1];
const up = [0, -1];
const left = [-1, 0];
const right = [1, 0];
const dirs = [up, right, down, left] as const;
type Dir = (typeof dirs)[number];

function next(pos: Point, dir: Dir): [Point, Dir][] {
  const [x, y] = pos;
  const [dx, dy] = dir;
  switch (MAP[y][x]) {
    case ".":
      return [[[x + dx, y + dy], dir]];
    case "-":
      switch (dir) {
        case left:
        case right:
          return [[[x + dx, y + dy], dir]];
        case up:
        case down:
          return [
            [[x + 1, y], right],
            [[x - 1, y], left],
          ];
      }
    case "|":
      switch (dir) {
        case left:
        case right:
          return [
            [[x, y + 1], down],
            [[x, y - 1], up],
          ];
        case up:
        case down:
          return [[[x + dx, y + dy], dir]];
      }
    case "/": {
      dir =
        dir === right ? up : dir === up ? right : dir === left ? down : left;
      const [dx, dy] = dir;
      return [[[x + dx, y + dy], dir]];
    }
    case "\\": {
      dir =
        dir === left ? up : dir === up ? left : dir === right ? down : right;
      const [dx, dy] = dir;
      return [[[x + dx, y + dy], dir]];
    }
  }
  throw Error("wtf");
}

function isOutOfMap(pos: Point): boolean {
  const [x, y] = pos;
  return x < 0 || y < 0 || x >= MAP[0].length || y >= MAP.length;
}

const start = [0, 0];
const startDir = right;
const history = new Set<string>();
const energized = new Set<string>();

function travel(pos: Point, dir: Dir) {
  const key = pos.toString() + dir.toString();
  if (isOutOfMap(pos) || history.has(key)) {
    return;
  }
  log(pos);
  history.add(key);
  energized.add(pos.toString());
  next(pos, dir).forEach(([nextPos, nextDir]) => {
    travel(nextPos, nextDir);
  });
}

travel(start, startDir);

// part1
part1(energized.size);

// part2
part2("TODO");
