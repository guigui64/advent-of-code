import { log, part1, part2, readLines, setDebug, sum } from "./aoc.ts";

const example = true;
setDebug(example);
const lines = readLines(example);

let X = 1;
const history: number[] = [X];
for (const line of lines) {
  log(line);
  if (line === "noop") {
    history.push(X);
    log(X);
  } else {
    history.push(X);
    log(X);
    history.push(X);
    log(X);
    X += parseInt(line.slice(5));
  }
}
const indices = [20, 60, 100, 140, 180, 220];
indices.forEach((i) => log(i, history[i]));
part1(
  sum(indices.map((x) => x * history[x])),
);

let screen = "\n";
for (let y = 0; y < 6; y++) {
  log("y", y);
  for (let x = 0; x < 40; x++) {
    log("x + 1", x + 1);
    const X = history[40 * y + x];
    log("X", X);
    if (Math.abs(X - x + 1) < 2) {
      screen += "#";
    } else {
      screen += ".";
    }
    log(screen[screen.length - 1]);
  }
  screen += "\n";
}

part2(screen);
