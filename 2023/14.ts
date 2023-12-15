import { log, part1, part2, readLines, sum } from "./aoc.ts";

globalThis.example = false;
const lines = readLines();
log(lines);

function north(map: string[][]) {
  for (let x = 0; x < map[0].length; x++) {
    for (let y = 1; y < map.length; y++) {
      if (map[y][x] === "O") {
        let yy = y;
        while (yy > 0 && map[yy - 1][x] === ".") {
          yy--;
        }
        if (map[yy][x] === ".") {
          map[yy][x] = "O";
          map[y][x] = ".";
        }
      }
    }
  }
}

function south(map: string[][]) {
  for (let x = 0; x < map[0].length; x++) {
    for (let y = map.length - 2; y >= 0; y--) {
      if (map[y][x] === "O") {
        let yy = y;
        while (yy < map.length - 1 && map[yy + 1][x] === ".") {
          yy++;
        }
        if (map[yy][x] === ".") {
          map[yy][x] = "O";
          map[y][x] = ".";
        }
      }
    }
  }
}

function east(map: string[][]) {
  for (let y = 0; y < map.length; y++) {
    for (let x = map[0].length - 2; x >= 0; x--) {
      if (map[y][x] === "O") {
        let xx = x;
        while (xx < map[0].length - 1 && map[y][xx + 1] === ".") {
          xx++;
        }
        if (map[y][xx] === ".") {
          map[y][xx] = "O";
          map[y][x] = ".";
        }
      }
    }
  }
}

function west(map: string[][]) {
  for (let y = 0; y < map.length; y++) {
    for (let x = 1; x < map[0].length; x++) {
      if (map[y][x] === "O") {
        let xx = x;
        while (xx > 0 && map[y][xx - 1] === ".") {
          xx--;
        }
        if (map[y][xx] === ".") {
          map[y][xx] = "O";
          map[y][x] = ".";
        }
      }
    }
  }
}

function load(map: string[][]) {
  return sum(
    map.map((row, i) => row.filter((c) => c === "O").length * (map.length - i)),
  );
}

// part1
let map = lines.map((line) => line.split(""));
north(map);
part1(load(map));

function cycle(map: string[][]) {
  north(map);
  west(map);
  south(map);
  east(map);
}

function toString(map: string[][]) {
  return map.map((row) => row.join("")).join("");
}

// part2
map = lines.map((line) => line.split(""));
const cache = [toString(map)];
let iter = 0;
const target = 1_000_000_000;
while (iter < target) {
  iter++;
  cycle(map);
  const idx = cache.indexOf(toString(map));
  if (idx !== -1) {
    const period = iter - idx;
    const amt = Math.floor((target - iter) / period);
    iter += amt * period;
    continue;
  }
  cache.push(toString(map));
}
part2(load(map));
