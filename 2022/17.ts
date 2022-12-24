import { part1, part2, range, readLines, setDebug } from "./aoc.ts";

const example = true;
setDebug(example);
const instructions = readLines(example)[0];

// map of rocks coordinates from bottom-left, eg:
//  .#.
//  ###
//  .#.
//  ^
//  \
//   -- origin
// ==> 0,1 1,0 1,1 1,2 2,1
// X
// ^
// |
// +--> Y
const rocks = "-+LIS";
const coords = [
  [[0, 0], [0, 1], [0, 2], [0, 3]],
  [[0, 1], [1, 0], [1, 1], [1, 2], [2, 1]],
  [[0, 0], [0, 1], [0, 2], [1, 2], [2, 2]],
  [[0, 0], [1, 0], [2, 0], [3, 0]],
  [[0, 0], [0, 1], [1, 0], [1, 1]],
];
// collisions are computed on bottom pixels
const bottoms = [
  [0, 1, 2, 3],
  [0, 1, 3],
  [0, 1, 2],
  [0],
  [0, 1],
];
// top pixels
const tops = [
  [0, 1, 2, 3],
  [1, 3, 4],
  [0, 1, 4],
  [3],
  [2, 3],
];

function jet(coords: number[][], dir: string, stopped: number[][]) {
  const dy = dir === ">" ? 1 : -1;
  // check collision with walls or floor
  if (
    Math.max(...coords.map((c) => c[1])) + dy === W ||
    Math.min(...coords.map((c) => c[1])) + dy === -1
  ) {
    return coords;
  }
  const newCoords = coords.map((c) => [c[0], c[1] + dy]);
  if (
    newCoords.some((c) => stopped.some((s) => c[0] === s[0] && c[1] === s[1]))
  ) {
    return coords;
  }
  return newCoords;
}

function hit(stopped: number[][], coords: number[][], bottoms: number[]) {
  return stopped.some((s) =>
    bottoms.some((ci) => {
      const c = coords[ci];
      return c[1] === s[1] && c[0] === s[0] + 1;
    })
  );
}

function fall(coords: number[][]) {
  return coords.map((c) => [c[0] - 1, c[1]]);
}

function print(coords: number[][], stopped: number[][], bottomFloor: number) {
  for (
    let x = Math.max(
      Math.max(...coords.map((c) => c[0])),
      Math.max(...stopped.map((s) => s[0])),
    );
    x >= bottomFloor;
    x--
  ) {
    let s = "|";
    for (let y = 0; y < W; y++) {
      s += coords.some((c) => c[0] === x && c[1] === y) ? "@" : (
        stopped.some((s) => s[0] === x && s[1] === y) ? "#" : "."
      );
    }
    s += "|";
    console.log(s);
  }
  console.log("");
}

const W = 7; // chamber's width
let ir = 0; // rocks
let ii = 0; // instructions
let stopped = [...Array(W).keys()].map((y) => [0, y]); // start at floor level
let height = 0;
let bottomFloor = 0;
const cache: {
  rock: number;
  next4instr: string;
  stopped: string;
  next: string;
}[] = [];

const p1 = 2022;
const p2 = 1000000000000;
for (let turn = 0; turn < p2; turn++) {
  const rock = rocks[ir];
  const dx = 4 + Math.max(...stopped.map((s) => s[0]));
  let c = coords[ir].map((c) => [c[0] + dx, c[1] + 2]);
  // log(rock, c);
  const stoppedSave = JSON.stringify(
    stopped.map((s) => [s[0] - bottomFloor, s[1]]),
  );
  const next4instr = range(4).map((x) =>
    instructions[(ii + x) % instructions.length]
  ).join("");
  // console.log(stoppedSave);
  const fromCache = cache.find((c) =>
    c.rock === ir && c.next4instr === next4instr && c.stopped === stoppedSave
  );
  if (fromCache) {
    console.log(height, rock, "cache hit!!!");
    // print(c, stopped, bottomFloor);
    stopped = JSON.parse(fromCache.next).map((
      s: number[],
    ) => [s[0] + bottomFloor, s[1]]);
    // print(c, stopped, bottomFloor);
  } else {
    while (true) {
      const instr = instructions[ii];
      ii = (ii + 1) % instructions.length;
      c = jet(c, instr, stopped);
      // log(instr, c);
      if (hit(stopped, c, bottoms[ir])) break;
      c = fall(c);
      // log("v", c);
      // print(c, stopped);
    }
    // log(c);
    // print(c, stopped);
    stopped.push(...c);
    stopped = stopped.filter((s) => s[0] >= bottomFloor);
    bottomFloor = Math.min(
      ...range(W).map((y) =>
        Math.max(...stopped.filter((s) => s[1] === y).map((s) => s[0]))
      ),
    );
    cache.push({
      rock: ir,
      next4instr,
      stopped: stoppedSave,
      next: JSON.stringify(stopped.map((s) => [s[0] - bottomFloor, s[1]])),
    });
    // console.log({ bottomFloor, stopped: stopped.length });
    // log(stopped);
  }

  height = Math.max(
    Math.max(...c.map((c) => c[0])),
    Math.max(...stopped.map((s) => s[0])),
  );
  ir = (ir + 1) % rocks.length;
  if (turn === p1 - 1) {
    part1(height);
  }
  if (turn / p2 * 100 % 1 === 0) {
    console.log(turn / p2 * 100, "%");
    console.timeLog("took");
  }
}
part2(height);
