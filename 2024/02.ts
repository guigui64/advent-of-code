import { log, part1, part2, readLines } from "./aoc.ts";

globalThis.example = false;
globalThis.verbose = false;
const lines = readLines();
log(lines);

const report = lines.map((line) => line.split(/\s+/).map(Number));

function isSafe(levels: number[]) {
  const dir = levels[0] < levels[1] ? 1 : -1;
  for (let i = 0; i < levels.length - 1; i++) {
    const dist = (levels[i + 1] - levels[i]) * dir;
    if (dist < 1 || dist > 3) return false;
  }
  return true;
}

part1(report.filter(isSafe).length);

function isSafe2(levels: number[]) {
  if (isSafe(levels)) {
    return true;
  }
  for (let i = 0; i < levels.length; i++) {
    if (isSafe([...levels.slice(0, i), ...levels.slice(i + 1)])) {
      return true;
    }
  }
  return false;
}

part2(report.filter(isSafe2).length);
