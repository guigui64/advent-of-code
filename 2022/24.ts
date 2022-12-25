import { log, part1, part2, Point, readLines, setDebug } from "./aoc.ts";

const example = false;
setDebug(example);
const lines = readLines(example);

type Direction = ">" | "<" | "^" | "v";

type Blizzard = {
  pos: Point;
  dir: Direction;
};

const H = lines.length;
const W = lines[0].length;

function move(b: Blizzard) {
  switch (b.dir) {
    case ">":
      b.pos[0]++;
      if (b.pos[0] === W - 1) {
        b.pos[0] = 1;
      }
      break;
    case "<":
      b.pos[0]--;
      if (b.pos[0] === 0) {
        b.pos[0] = W - 2;
      }
      break;
    case "^":
      b.pos[1]--;
      if (b.pos[1] === 0) {
        b.pos[1] = H - 2;
      }
      break;
    case "v":
      b.pos[1]++;
      if (b.pos[1] === H - 1) {
        b.pos[1] = 1;
      }
      break;
  }
}

function neighbors(pos: Point) {
  const [x, y] = pos;
  return [[1, 0], [-1, 0], [0, 1], [0, -1]].map(([dx, dy]) => [
    x + dx,
    y + dy,
  ]).filter(([x, y]) => (0 < x && x < W - 1 && 0 < y && y < H - 1));
}

const blizzards: Blizzard[] = [];

lines.forEach((line, y) => {
  line.split("").forEach((c, x) => {
    if (c !== "." && c !== "#") {
      blizzards.push({
        pos: [x, y],
        dir: c as Direction,
      });
    }
  });
});

const initial = [1, 0];
const goal = [W - 2, H - 1];

// A* where heuristic is distance
function distance(from: Point, to: Point) {
  return Math.abs(from[0] - to[0]) + Math.abs(from[1] - to[1]);
}
const openSet = new Set<string>([initial.toString()]);
const cameFrom: { [key: string]: string } = {};
const gScore = { [initial.toString()]: 0 };
const fScore = { [initial.toString()]: distance(initial, goal) };
let time = 0;
while (openSet.size > 0) {
  time++;
  blizzards.forEach((b) => move(b));
  let current = "";
  let minFScore = Infinity;
  Object.entries(fScore).forEach(([p, s]) => {
    if (s < minFScore) {
      minFScore = s;
      current = p;
    }
  });
  const pCurrent = current.split(",").map(Number);
  if (distance(pCurrent, goal) === 1) {
    let path = [current];
    while (Object.hasOwn(cameFrom, current)) {
      current = cameFrom[current];
      path = [current, ...path];
    }
    log({ path, time });
    part1(time + 1);
    break;
  }
  openSet.delete(current);
  for (const pN of [...neighbors(pCurrent), pCurrent]) {
    const n = pN.toString();
    log({ current, n });
    if (blizzards.some((b) => b.pos.toString() === n)) {
      continue;
    }
    const tentativeGScore = gScore[current] === undefined
      ? Infinity
      : gScore[current];
    if (tentativeGScore < (gScore[n] === undefined ? Infinity : gScore[n])) {
      cameFrom[n] = current;
      gScore[n] = tentativeGScore;
      fScore[n] = tentativeGScore + distance(goal, pN);
      if (!openSet.has(n)) {
        openSet.add(n);
      }
    } else if (current === n) {
      openSet.add(current);
    }
  }
}

// part2
part2("TODO");
