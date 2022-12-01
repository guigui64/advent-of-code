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

function partX(i: 1 | 2) {
  // deno-lint-ignore no-explicit-any
  return (...data: any[]) => console.log(`Part${i}:`, ...data);
}

export const part1 = partX(1);
export const part2 = partX(2);

export function sum(a: number[]) {
  return a.reduce((a, c) => a + c);
}
