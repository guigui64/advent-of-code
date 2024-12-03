import { log, part1, part2, readLines } from "./aoc.ts";

globalThis.example = false;
const lines = readLines();
log(lines);

const map = lines.map((l) => l.split(""));
const startCoords = map
  .map((row, y) => [row, y] as const)
  .filter(([row, y]) => row.includes("S"))
  .map(([row, y]) => [row.indexOf("S"), y])[0];
log(startCoords);
// TODO: find start pipe programmatically
const startPipe = globalThis.example ? "F" : "|";
map[startCoords[1]][startCoords[0]] = startPipe;

function has(path: number[][], coords: number[]) {
  return path.some((c) => c[0] === coords[0] && c[1] === coords[1]);
}

function travel(path: number[][], depth: number) {
  const len = path.length;
  console.log(len, depth);
  for (const coords of path.slice(-2)) {
    const [x, y] = coords;
    switch (map[y][x]) {
      case "|":
        if (!has(path, [x, y + 1])) {
          path.push([x, y + 1]);
        }
        if (!has(path, [x, y - 1])) {
          path.push([x, y - 1]);
        }
        break;
      case "-":
        if (!has(path, [x + 1, y])) {
          path.push([x + 1, y]);
        }
        if (!has(path, [x - 1, y])) {
          path.push([x - 1, y]);
        }
        break;
      case "F":
        if (!has(path, [x + 1, y])) {
          path.push([x + 1, y]);
        }
        if (!has(path, [x, y + 1])) {
          path.push([x, y + 1]);
        }
        break;
      case "7":
        if (!has(path, [x - 1, y])) {
          path.push([x - 1, y]);
        }
        if (!has(path, [x, y + 1])) {
          path.push([x, y + 1]);
        }
        break;
      case "J":
        if (!has(path, [x, y - 1])) {
          path.push([x, y - 1]);
        }
        if (!has(path, [x - 1, y])) {
          path.push([x - 1, y]);
        }
        break;
      case "L":
        if (!has(path, [x + 1, y])) {
          path.push([x + 1, y]);
        }
        if (!has(path, [x, y - 1])) {
          path.push([x, y - 1]);
        }
        break;
    }
  }
  if (path.length === len) {
    return depth;
  }
  return travel(path, depth + 1);
}

// part1
part1(travel([startCoords], 0));

// part2
part2("TODO");
