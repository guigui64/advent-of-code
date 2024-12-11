import { log, part1, part2, readLines, sum } from "./aoc.ts";
import { findAllPaths, findAllTargets, Node } from "./bfs.ts";

globalThis.example = false;
const lines = readLines();
log(lines);

const M = lines.map((l) =>
  l.split("").map((v) => ({ value: +v, adjacent: [] }) as Node<number>),
);
const H = lines.length;
const W = lines[0].length;

const heads: Node<number>[] = [];
for (let y = 0; y < H; y++) {
  for (let x = 0; x < W; x++) {
    if (M[y][x].value === 0) {
      heads.push(M[y][x]);
    }
    M[y][x].adjacent.push(
      ...(
        [M[y - 1]?.[x], M[y + 1]?.[x], M[y]?.[x - 1], M[y]?.[x + 1]].filter(
          (v) => v !== undefined,
        ) as Node<number>[]
      ).filter((v) => v.value - M[y][x].value === 1),
    );
  }
}

// part1
part1(sum(heads.map((h) => findAllTargets(h, 9).size)));

// part2
part2(sum(heads.map((h) => findAllPaths(h, 9).length)));
