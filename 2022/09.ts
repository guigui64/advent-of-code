import {
  log,
  part1,
  part2,
  printTime,
  range,
  readLines,
  setDebug,
  startTimer,
} from "./aoc.ts";

startTimer();
const lines = readLines(false);
setDebug(false);

type Pos = number[];
type Dir = "U" | "D" | "L" | "R";
const moves = {
  U: [0, -1],
  D: [0, 1],
  R: [1, 0],
  L: [-1, 0],
};

function moveHead(dir: Dir, pos: Pos) {
  return [pos[0] + moves[dir][0], pos[1] + moves[dir][1]];
}

function distances(head: Pos, tail: Pos) {
  return [head[0] - tail[0], head[1] - tail[1]];
}

function moveKnot(target: Pos, knot: Pos) {
  const dist = distances(target, knot);
  if (Math.abs(dist[0]) > 1 && Math.abs(dist[1]) <= 1) {
    knot[0] += dist[0] / Math.abs(dist[0]);
    knot[1] = target[1];
  } else if (Math.abs(dist[0]) <= 1 && Math.abs(dist[1]) > 1) {
    knot[0] = target[0];
    knot[1] += dist[1] / Math.abs(dist[1]);
  } else if (Math.abs(dist[0]) > 1 && Math.abs(dist[1]) > 1) {
    knot[0] += dist[0] / Math.abs(dist[0]);
    knot[1] += dist[1] / Math.abs(dist[1]);
  }
  return knot;
}

let headPos = [0, 0];
const knots = [...Array(9)].map((_) => [0, 0]);
const visited = knots.map((knot) => new Set([knot.toString()]));
for (const line of lines) {
  const dir = line[0] as Dir;
  const steps = parseInt(line.slice(2));
  range(steps).forEach(() => {
    headPos = moveHead(dir, headPos);
    knots.forEach((_, i) => {
      const target = i === 0 ? headPos : knots[i - 1];
      knots[i] = moveKnot(target, knots[i]);
      visited[i].add(knots[i].toString());
    });
  });
}
log(visited);
part1(visited[0].size);
part2(visited[8].size);
printTime();
