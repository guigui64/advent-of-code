import dijkstra from "https://deno.land/x/dijkstra@1.0.2/mod.ts";
import {
  combinations,
  log,
  part1,
  part2,
  printTime,
  range,
  readLines,
  setDebug,
  startTimer,
} from "./aoc.ts";

type Point = number[];

startTimer();
const example = false;
setDebug(example);
const lines = readLines(example);

const H = lines.length;
const W = lines[0].length;

let start: Point = [];
let end: Point = [];

lines.forEach((line, y) => {
  let x = line.indexOf("S");
  if (x !== -1) {
    start = [x, y];
    lines[y] = lines[y].replace("S", "a");
  }
  x = line.indexOf("E");
  if (x !== -1) {
    end = [x, y];
    lines[y] = lines[y].replace("E", "z");
  }
});

function neighbors(p: Point) {
  const [x, y] = p;
  return [
    [0, 1],
    [0, -1],
    [1, 0],
    [-1, 0],
  ]
    .map(([dx, dy]) => [x + dx, y + dy])
    .filter(([x, y]) => x >= 0 && x < W && y >= 0 && y < H);
}

function key(p: Point) {
  return p.toString();
}

function elevation(p: Point) {
  return lines[p[1]][p[0]].charCodeAt(0);
}

const graph = Object.fromEntries(
  combinations(range(W), range(H)).map((node) => [
    key(node),
    Object.fromEntries(
      neighbors(node)
        .filter((neighbor) => elevation(neighbor) <= elevation(node) + 1)
        .map((neighbor) => [key(neighbor), 1]),
    ),
  ]),
);

log(graph);
const path = dijkstra.find_path(graph, key(start), key(end));
log(path);

part1(path.length - 1);
printTime();

const paths = combinations(range(W), range(H))
  .filter(([x, y]) => lines[y][x] === "a")
  .map((node) => {
    try {
      return dijkstra.find_path(graph, key(node), key(end));
    } catch (_err) {
      return "no path";
    }
  })
  .filter((path) => path !== "no path");

paths.sort((p1, p2) => p1.length - p2.length);

log(paths[0]);
part2(Math.min(...paths.map((p) => p.length - 1)));
printTime();
