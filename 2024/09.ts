import { log, part1, part2, range, readLines, sum } from "./aoc.ts";

globalThis.example = false;
const map = readLines()[0].split("").map(Number);
log(map);
if (map.length % 2 !== 0) {
  map.push(0);
}

let id = 0;
const blocks: [number, number][] = [];
let cursor = 0;
const empty: number[] = [];

for (let i = 0; i < map.length; i += 2) {
  for (let x = 0; x < map[i]; x++) {
    blocks.push([cursor++, id]);
  }
  id++;
  for (let x = 0; x < map[i + 1]; x++) {
    empty.push(cursor++);
  }
}
log(blocks, empty);

const C = cursor;
let s = "";
for (let i = 0; i < C; i++) {
  s += blocks.find(([v]) => v === i)?.[1] ?? ".";
}
log(s);

cursor = blocks.length - 1;
while (true) {
  const slot = empty.shift()!;
  const [pos, id] = blocks[cursor];
  if (pos < slot) {
    break;
  }
  blocks[cursor--] = [slot, id];
}
log(blocks, empty);

s = "";
for (let i = 0; i < C; i++) {
  s += blocks.find(([v]) => v === i)?.[1] ?? ".";
}
log(s);

// part1
part1(sum(blocks.map(([i, v]) => i * v)));

// part2
const ranges: [number, number][] = [];
const emptyRanges: [number, number][] = [];
cursor = 0;
for (let i = 0; i < map.length; i += 2) {
  ranges.push([cursor, cursor + map[i] - 1]);
  cursor += map[i];
  if (map[i + 1] > 0) {
    emptyRanges.push([cursor, cursor + map[i + 1] - 1]);
    cursor += map[i + 1];
  }
}

for (let r = ranges.length - 1; r >= 0; r--) {
  const [x, y] = ranges[r];
  const size = y - x + 1;
  for (let e = 0; e < emptyRanges.length; e++) {
    const [ex, ey] = emptyRanges[e];
    const esize = ey - ex + 1;
    if (esize >= size && ex < x) {
      ranges[r] = [ex, ex + size - 1];
      emptyRanges[e] = [ex + size, ey];
      break;
    }
  }
}

part2(
  sum(ranges.map(([x, y], id) => sum(range(y - x + 1, x).map((v) => v * id)))),
);
