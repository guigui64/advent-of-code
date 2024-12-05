import { basename, extname } from "https://deno.land/std@0.166.0/path/posix.ts";

export type Point = number[];

export function manhattan(a: Point, b: Point) {
  return Math.abs(a[0] - b[0]) + Math.abs(a[1] - b[1]);
}

export function read() {
  const tsName = basename(Deno.mainModule);
  const filename = tsName.replace(
    extname(tsName),
    (globalThis.example ? "ex" : "") + ".txt",
  );
  console.time("took");
  try {
    return Deno.readTextFileSync(filename);
  } catch {
    console.error("Could not read file", filename);
    return "";
  }
}

export function readLines() {
  const lines = read().split("\n");
  return lines.slice(0, -1); // remove trailing newline
}

export function range(size: number, startAt = 0) {
  return [...Array(size).keys()].map((i) => i + startAt);
}

function partX(i: 1 | 2) {
  return (...data: unknown[]) => {
    console.log(`Part${i}:`, ...data);
    console.timeLog("took");
  };
}

export const part1 = partX(1);
export const part2 = partX(2);

export function sum(a: number[]) {
  return a.reduce((a, c) => a + c, 0);
}
export function product(a: number[]) {
  return a.reduce((a, c) => a * c, 1);
}

export function combinations<T>(array1: T[], array2?: T[]) {
  if (array2) {
    return array2.flatMap((x2) => array1.map((x1) => [x1, x2]));
  }
  return array1.flatMap((v, i) => array1.slice(i + 1).map((w) => [w, v]));
}

export function directions(diagonalAllowed = true) {
  return diagonalAllowed
    ? combinations([-1, 0, 1], [-1, 0, 1]).filter(
        ([dx, dy]) => dx !== 0 || dy !== 0,
      )
    : [
        [-1, 0],
        [0, -1],
        [0, 1],
        [1, 0],
      ];
}

export function surrounding(x: number, y: number) {
  return directions().map(([dx, dy]) => [x + dx, y + dy]);
}

export function log(...a: unknown[]) {
  if (globalThis.example || globalThis.verbose) {
    console.log(...a);
  }
}

export function equal<T>(a: T[], b: T[]) {
  if (a.length !== b.length) {
    return false;
  }
  return a.every((v, i) => v === b[i]);
}

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

export class DefaultDict<K, V> extends Map<K, V> {
  constructor(private defaultFunc: (key: K) => V) {
    super();
  }
  override get(key: K) {
    if (!this.has(key)) {
      this.set(key, this.defaultFunc(key));
    }
    return super.get(key)!;
  }
}

export class Counter<K> extends DefaultDict<K, number> {
  constructor() {
    super(Number);
  }
  inc(key: K, by?: number) {
    this.set(key, this.get(key) + (by ?? 1));
  }
  dec(key: K, by?: number) {
    this.set(key, this.get(key) - (by ?? 1));
  }
}

export function count<T>(a: T[]): Counter<T> {
  const c = new Counter<T>();
  a.forEach((x) => c.inc(x));
  return c;
}
