import { combinations } from "./aoc.ts";
import { DefaultDict, log, part1, part2, Point, readLines } from "./aoc.ts";

globalThis.example = false;
const lines = readLines();
log(lines);

const H = lines.length;
const W = lines[0].length;

const antennas: DefaultDict<string, Point[]> = new DefaultDict(() => []);
for (let y = 0; y < H; y++) {
  for (let x = 0; x < W; x++) {
    const c = lines[y][x];
    if (c !== ".") {
      antennas.get(c).push([x, y]);
    }
  }
}

const antinodes = new Set<string>();

function inBounds([x, y]: Point) {
  return x >= 0 && x < W && y >= 0 && y < H;
}

for (const positions of antennas.values()) {
  for (const [[x1, y1], [x2, y2]] of combinations(positions)) {
    const [dx, dy] = [x2 - x1, y2 - y1];
    let [x, y] = [x1 - dx, y1 - dy];
    if (inBounds([x, y])) {
      antinodes.add([x, y].toString());
    }
    [x, y] = [x2 + dx, y2 + dy];
    if (inBounds([x, y])) {
      antinodes.add([x, y].toString());
    }
  }
}

// part1
part1(antinodes.size);

antinodes.clear();

for (const positions of antennas.values()) {
  for (const [[x1, y1], [x2, y2]] of combinations(positions)) {
    const [dx, dy] = [x2 - x1, y2 - y1];
    let [x, y] = [x1, y1];
    while (inBounds([x, y])) {
      antinodes.add([x, y].toString());
      x -= dx;
      y -= dy;
    }
    [x, y] = [x2, y2];
    while (inBounds([x, y])) {
      antinodes.add([x, y].toString());
      x += dx;
      y += dy;
    }
  }
}

// part2
part2(antinodes.size);
