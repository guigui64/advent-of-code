import { basename, extname } from "https://deno.land/std@0.166.0/path/posix.ts";

export type Point = number[];

export function read() {
  const tsName = basename(Deno.mainModule);
  const filename = tsName.replace(
    extname(tsName),
    (globalThis.example ? "ex2" : "") + ".txt",
  );
  console.time("took");
  return Deno.readTextFileSync(filename);
}

export function readLines() {
  const lines = read().split("\n");
  return lines.slice(0, -1); // remove trailing newline
}

export function range(size: number, startAt = 0) {
  return [...Array(size).keys()].map((i) => i + startAt);
}

function partX(i: 1 | 2) {
  // deno-lint-ignore no-explicit-any
  return (...data: any[]) => {
    console.log(`Part${i}:`, ...data);
    console.timeLog("took");
  };
}

export const part1 = partX(1);
export const part2 = partX(2);

export function sum(a: number[]) {
  return a.reduce((a, c) => a + c, 0);
}

export function combinations<T>(array1: T[], array2?: T[]) {
  if (array2) {
    return array2.flatMap((x2) => array1.map((x1) => [x1, x2]));
  }
  return array1.flatMap((v, i) => array1.slice(i + 1).map((w) => [w, v]));
}

// deno-lint-ignore no-explicit-any
export function log(...a: any[]) {
  if (globalThis.example || globalThis.verbose) {
    console.log(...a);
  }
}

/* export function BFS<T>({ neighbors, root, key, ignore, goal }: {
  neighbors: (node: T) => T[];
  root: T;
  key: (node: T) => string;
  ignore?: (node: T) => boolean;
  goal?: (node: T) => boolean;
}): { Q: T[]; explored: Set<string> } {
  const Q = [root];
  const explored = new Set<string>([key(root)]);
  while (Q.length > 0) {
    const v = Q.shift()!;
    // if (explored.has(key(v))) continue;
    if (goal && goal(v)) break;
    if (ignore && ignore(v)) continue;
    // explored.add(key(v));
    neighbors(v).filter((n) => !explored.has(key(n))).forEach((n) => {
      explored.add(key(n));
      Q.push(n);
    });
    // Q.push(...neighbors(v));
  }
  return { Q, explored };
} */

export class Cube {
  x: number;
  y: number;
  z: number;

  constructor(x: number, y: number, z: number) {
    this.x = x;
    this.y = y;
    this.z = z;
  }

  static parse(line: string) {
    const [x, y, z] = line.split(",").map(Number);
    return new Cube(x, y, z);
  }

  toString() {
    return [this.x, this.y, this.z].join(",");
  }

  neighbors(): Cube[] {
    return [
      [1, 0, 0],
      [-1, 0, 0],
      [0, 1, 0],
      [0, -1, 0],
      [0, 0, 1],
      [0, 0, -1],
    ].map(([dx, dy, dz]) => new Cube(this.x + dx, this.y + dy, this.z + dz));
  }
}
