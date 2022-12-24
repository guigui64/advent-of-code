import { Cube, part1, part2, readLines, setDebug } from "./aoc.ts";

const example = false;
setDebug(example);
const lines = readLines(example);

const cubes = new Set(lines);
let exposed = 0;
let min = Infinity;
let max = -Infinity;
for (const cube of cubes) {
  const c = Cube.parse(cube);
  exposed += c.neighbors().filter((s) => !cubes.has(s.toString())).length;
  min = Math.min(min, c.x, c.y, c.z);
  max = Math.max(max, c.x, c.y, c.z);
}

part1(exposed);

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
  const sides = cube.neighbors();
  exposed += sides.filter((s) => cubes.has(s.toString())).length;
  queue.push(...sides);
}
part2(exposed);
