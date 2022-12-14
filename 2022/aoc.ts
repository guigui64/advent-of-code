import { basename, extname } from "https://deno.land/std@0.166.0/path/posix.ts";

export function read(ex = false) {
  const tsName = basename(Deno.mainModule);
  const filename = tsName.replace(extname(tsName), (ex ? "ex" : "") + ".txt");
  return Deno.readTextFileSync(filename);
}

export function readLines(ex = false) {
  const lines = read(ex).split("\n");
  return lines.slice(0, -1); // remove trailing newline
}

export function range(size: number, startAt = 0) {
  return [...Array(size).keys()].map((i) => i + startAt);
}

let time: number | null = null;
export function startTimer() {
  time = Date.now();
  console.log("🎬");
}

function delta(to: number) {
  let d = to - time!;
  let s = "";
  if (d > 1000) {
    const seconds = Math.abs(d / 1000);
    d -= 1000 * seconds;
    s += seconds + "s";
  }
  s += d + "ms";
  return s;
}

export function printTime() {
  console.log(`🏁 ${delta(Date.now())}`);
}

function partX(i: 1 | 2) {
  // deno-lint-ignore no-explicit-any
  return (...data: any[]) => console.log(`Part${i}:`, ...data);
}

export const part1 = partX(1);
export const part2 = partX(2);

export function sum(a: number[]) {
  return a.reduce((a, c) => a + c);
}

export function combinations<T>(array1: T[], array2?: T[]) {
  if (array2) {
    return array2.flatMap((x2) => array1.map((x1) => [x1, x2]));
  }
  return array1.flatMap((v, i) => array1.slice(i + 1).map((w) => [w, v]));
}

let debug = false;
export function setDebug(d: boolean) {
  debug = d;
}
// deno-lint-ignore no-explicit-any
export function log(...a: any[]) {
  if (debug) {
    console.log(...a);
  }
}

export function BFS<T>(
  neighbors: (node: T) => T[],
  root: T,
  goal: (node: T) => boolean,
  key: (node: T) => string,
): { Q: T[]; explored: string[] } {
  const Q: T[] = [];
  const explored: string[] = [key(root)];
  Q.push(root);
  while (Q.length > 0) {
    const v = Q.pop()!;
    if (goal(v)) {
      break;
    }
    for (const n of neighbors(v)) {
      if (!explored.includes(key(n))) {
        explored.push(key(n));
        Q.push(n);
      }
    }
  }
  return { Q, explored };
}
