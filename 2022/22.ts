import { log, part1, part2, Point, range, readLines, setDebug } from "./aoc.ts";
import { makeDLL } from "./list.ts";

const example = true;
setDebug(example);
const lines = readLines(example);

const sep = lines.findIndex((l) => l === "");
const map = lines.slice(0, sep);
const instructions = lines[sep + 1];
log(instructions);

function tile(pos: Point) {
  const [x, y] = pos;
  return map[y]?.[x] || " ";
}

type Direction = "right" | "left" | "up" | "down";
const moves = {
  "right": [1, 0],
  "left": [-1, 0],
  "up": [0, -1],
  "down": [0, 1],
};
function next(pos: Point, dir: Direction) {
  let n = pos.map((p, i) => p + moves[dir][i]);
  const t = tile(n);
  if (t === " ") {
    // wrap
    const [x, y] = pos;
    if (dir === "right") {
      n = [
        Math.min(map[y].indexOf("."), map[y].indexOf("#")),
        y,
      ];
    } else if (dir === "left") {
      n = [
        Math.max(map[y].lastIndexOf("."), map[y].lastIndexOf("#")),
        y,
      ];
    } else if (dir === "down") {
      n = [
        x,
        map.findIndex((l) => l[x] !== " "),
      ];
    } else if (dir === "up") {
      n = [
        x,
        map.findLastIndex((l) => l[x] !== " "),
      ];
    }
  }
  if (t === "#") return pos;
  return n;
}

let pos = [
  Math.min(map[0].indexOf("."), map[0].indexOf("#")),
  0,
];
console.log(pos);
const dirs: Direction[] = ["right", "down", "left", "up"];
let facing = makeDLL<Direction>(dirs)[0];

const distances = instructions.split(/[RL]/).map(Number);
const rotations = instructions.split(/[0-9]/).filter((e) => e !== "");
if (distances.length !== rotations.length + 1) throw Error("aoc lies");

while (distances.length > 0) {
  const dist = distances.shift()!;
  range(dist).forEach((_) => pos = next(pos, facing.value));
  if (rotations.length > 0) {
    const rot = rotations.shift();
    if (rot === "R") facing = facing.next!;
    else facing = facing.prev!;
  }
}
// part1
console.log(pos);
part1(1000 * (pos[1] + 1) + 4 * (pos[0] + 1) + dirs.indexOf(facing.value));

log(next([5, 4], "up"));

// part2
part2("TODO");
