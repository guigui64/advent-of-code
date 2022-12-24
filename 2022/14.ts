import { log, part1, part2, range, readLines, setDebug } from "./aoc.ts";

const example = false;
setDebug(true);
const lines = readLines(example);

type Point = number[];
const rocks: Point[] = [];
let abyss = 0;
for (const line of lines) {
  const points = line.split(" -> ").map((ps) => ps.split(",").map(Number));
  for (let i = 0; i < points.length - 1; i++) {
    const line = points.slice(i, i + 2);
    const minx = Math.min(...line.map((p) => p[0]));
    const maxx = Math.max(...line.map((p) => p[0]));
    const miny = Math.min(...line.map((p) => p[1]));
    const maxy = Math.max(...line.map((p) => p[1]));
    abyss = Math.max(abyss, maxy);
    if (minx === maxx) {
      rocks.push(...range(maxy - miny + 1, miny).map((y) => [minx, y]));
    } else {
      rocks.push(...range(maxx - minx + 1, minx).map((x) => [x, miny]));
    }
  }
}
// const abyss = Math.max(...rocks.map((r) => r[1])) + 1;
const floor = abyss + 1;
log(abyss, floor);
log(rocks.length);
const rocks2 = rocks.map((r) => r[1] * (floor + 1) + r[0]);

const orig: Point = [500, 0];
const sand: string[] = [];

function occupied(point: Point): boolean {
  // try sand first
  if (sand.includes(point.toString())) {
    return true;
  }
  if (point[1] === floor) {
    return true;
  }
  return rocks2.includes(point[1] * (floor + 1) + point[0]);
}

function next(from: Point): Point {
  const candidates = [
    [0, 1],
    [-1, 1],
    [1, 1],
  ].map(([dx, dy]) => [from[0] + dx, from[1] + dy]);
  return candidates.filter((p) => !occupied(p))[0] || [...from];
}

let curr = [...orig];
let p1 = false;
while (true) {
  const n = next(curr);
  // log(n);
  if (!p1 && n[1] >= abyss) {
    p1 = true;
    part1(sand.length);
  }
  if (n.toString() !== curr.toString()) {
    curr = [...n];
  } else {
    // come to rest
    sand.push(n.toString());
    if (sand.length % 1000 === 0) console.log(sand.length);
    if (n.toString() === orig.toString()) break;
    curr = [...orig];
  }
}
part2(sand.length);
