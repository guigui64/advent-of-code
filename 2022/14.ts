import {
  log,
  part1,
  part2,
  printTime,
  readLines,
  setDebug,
  startTimer,
} from "./aoc.ts";

startTimer();
const example = false;
setDebug(example);
const lines = readLines(example);

type Point = number[];
type Line = Point[];
const scan: Line[] = [];
for (const line of lines) {
  const points = line.split(" -> ").map((ps) => ps.split(",").map(Number));
  for (let i = 0; i < points.length - 1; i++) {
    scan.push(points.slice(i, i + 2));
  }
}
log(scan);
const abyss =
  Math.max(...scan.flatMap((line) => line.flatMap((point) => point[1]))) + 1;
const floor = abyss + 1;
log(abyss, floor);

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
  return scan.some((line) => {
    const minx = Math.min(...line.map((p) => p[0]));
    const maxx = Math.max(...line.map((p) => p[0]));
    const miny = Math.min(...line.map((p) => p[1]));
    const maxy = Math.max(...line.map((p) => p[1]));
    return (
      minx <= point[0] &&
      point[0] <= maxx &&
      miny <= point[1] &&
      point[1] <= maxy
    );
  });
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
    printTime();
  }
  if (n.toString() !== curr.toString()) {
    curr = [...n];
  } else {
    // come to rest
    sand.push(n.toString());
    // Deno.stdout.write(new Uint8Array([".".charCodeAt(0)]));
    if (n.toString() === orig.toString()) break;
    curr = [...orig];
  }
}
part2(sand.length);
printTime();
