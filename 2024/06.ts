import { log, part1, part2, Point, readLines } from "./aoc.ts";

globalThis.example = true;
const lines = readLines();
log(lines);

const H = lines.length;
const W = lines[0].length;

const DIRS = "URDL";
let dir = "U";

function turn(current: string) {
  const i = DIRS.indexOf(current);
  return DIRS[(i + 1) % DIRS.length];
}

function nextPos(current: Point, dir: string) {
  switch (dir) {
    case "U":
      return [current[0], current[1] - 1];
    case "D":
      return [current[0], current[1] + 1];
    case "L":
      return [current[0] - 1, current[1]];
    case "R":
      return [current[0] + 1, current[1]];
    default:
      throw new Error(`Unknown direction: ${dir}`);
  }
}

let pos: Point = [];
const obstacles: string[] = [];

for (let y = 0; y < H; y++) {
  for (let x = 0; x < W; x++) {
    const c = lines[y][x];
    if (c === "^") {
      pos = [x, y];
    } else if (c === "#") {
      obstacles.push([x, y].toString());
    }
  }
}

const visited = new Set<string>();
const directions = new Map<string, string>();
//const possibleSpots = new Set<string>();
let spots = 0;

function outOfBounds([x, y]: Point) {
  return x < 0 || x >= W || y < 0 || y >= H;
}

while (!outOfBounds(pos)) {
  if (visited.has(pos.toString())) {
    if (turn(dir) === directions.get(pos.toString())) {
      spots++;
    }
  }
  visited.add(pos.toString());
  directions.set(pos.toString(), dir);
  const next = nextPos(pos, dir);
  if (obstacles.includes(next.toString())) {
    dir = turn(dir);
    continue;
  }
  pos = next;
}

// part1
part1(visited.size);

// part2
part2(spots);
