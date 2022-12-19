import {
  part1,
  part2,
  printTime,
  readLines,
  setDebug,
  startTimer,
} from "./aoc.ts";

startTimer();
const example = false;
setDebug(example);
const lines = readLines(example);

class Cube {
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

  sides(): Cube[] {
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

const cubes = new Set(lines);
let exposed = 0;
let min = Infinity;
let max = -Infinity;
for (const cube of cubes) {
  const c = Cube.parse(cube);
  exposed += c.sides().filter((s) => !cubes.has(s.toString())).length;
  min = Math.min(min, c.x, c.y, c.z);
  max = Math.max(max, c.x, c.y, c.z);
}

part1(exposed);
printTime();

exposed = 0;
// BFS to simulate steam propagation
const visited = new Set<string>();
const queue = [new Cube(min - 1, min - 1, min - 1)];
while (queue.length > 0) {
  const cube = queue.shift()!;
  if (visited.has(cube.toString())) continue;
  if (cubes.has(cube.toString())) continue; // steam cannot reach droplets
  // check not out of bounds
  if (
    cube.x < min - 1 || cube.y < min - 1 || cube.z < min - 1 ||
    cube.x > max + 1 || cube.y > max + 1 || cube.z > max + 1
  ) continue;
  visited.add(cube.toString());
  const sides = cube.sides();
  exposed += sides.filter((s) => cubes.has(s.toString())).length;
  queue.push(...sides);
}
part2(exposed);
printTime();
