import { Counter, count, log, part1, part2, readLines } from "./aoc.ts";

globalThis.example = false;
globalThis.verbose = true;
const lines = readLines();
log(lines);

const instructions = lines
  .map((line) => /([RLUD]) (\d+) \((#\w{6})\)/.exec(line))
  .map((match) => ({
    dir: match![1],
    steps: Number(match![2]),
    color: match![3],
  }));
log(instructions);

const start = [0, 0];
const trench = [start];
instructions.forEach((instruction) => {
  let [x, y] = trench[trench.length - 1];
  let [dx, dy] = [0, 0];
  switch (instruction.dir) {
    case "R":
      dx = 1;
      break;
    case "L":
      dx = -1;
      break;
    case "U":
      dy = -1;
      break;
    case "D":
      dy = 1;
      break;
  }
  for (let i = 0; i < instruction.steps; i++) {
    x += dx;
    y += dy;
    trench.push([x, y]);
  }
});

const minY = Math.min(...trench.map(([_, y]) => y));
const maxY = Math.max(...trench.map(([_, y]) => y));
const minX = Math.min(...trench.map(([x, _]) => x));
const maxX = Math.max(...trench.map(([x, _]) => x));

let map = "";
let map2 = "";
let res = 0;
for (let y = minY; y <= maxY; y++) {
  let line = "";
  for (let x = minX; x <= maxX; x++) {
    if (trench.find(([X, Y]) => x === X && y === Y)) {
      line += "#";
    } else {
      line += ".";
    }
  }
  map += line + "\n";
  const line2 = line.replaceAll(/#\.+#/g, (match) => "#".repeat(match.length));
  map2 += line2 + "\n";
  res += count(line2.split("")).get("#");
}
log(map);
log(map2);

// part1
part1(res);

// part2
part2("TODO");
