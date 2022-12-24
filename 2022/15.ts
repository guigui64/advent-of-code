import { part1, part2, Point, readLines, setDebug, sum } from "./aoc.ts";

const example = false;
setDebug(example);
const lines = readLines(example);

const y = example ? 10 : 2000000;

function manhattanDistance(p1: Point, p2: Point): number {
  return Math.abs(p2[0] - p1[0]) + Math.abs(p2[1] - p1[1]);
}

class Sensor {
  position: Point;
  beacon: Point;
  distanceToBeacon: number;

  constructor(line: string) {
    const m = line.match(
      /Sensor at x=(-?\d+), y=(-?\d+): closest beacon is at x=(-?\d+), y=(-?\d+)/,
    )!;
    this.position = [m[1], m[2]].map(Number);
    this.beacon = [m[3], m[4]].map(Number);
    this.distanceToBeacon = manhattanDistance(this.beacon, this.position);
  }

  touches(row: number) {
    return Math.abs(row - this.position[1]) <= this.distanceToBeacon;
  }

  range(row: number): Range {
    const rowDist = Math.abs(row - this.position[1]);
    if (rowDist > this.distanceToBeacon) {
      throw new Error("sensor does not touch this row");
    }
    return new Range(
      this.position[0] - (this.distanceToBeacon - rowDist),
      this.position[0] + (this.distanceToBeacon - rowDist),
    );
  }
}

class Range {
  min: number;
  max: number;

  constructor(min: number, max: number) {
    this.min = min;
    this.max = max;
  }

  size() {
    return this.max - this.min + 1;
  }
}

function merge(...ranges: Range[]): Range[] {
  // first, sort ranges per ascending mins
  ranges.sort((left, right) => left.min - right.min);
  // then, compare bounds
  let previous = ranges[0];
  const merged: Range[] = [];
  ranges.slice(1).forEach((curr) => {
    if (previous.max >= curr.min - 1) {
      previous = new Range(previous.min, Math.max(previous.max, curr.max));
    } else {
      merged.push(previous);
      previous = curr;
    }
  });
  merged.push(previous);
  return merged;
}

function ranges(row: number) {
  return merge(
    ...sensors
      .filter((sensor) => sensor.touches(row))
      .map((sensor) => sensor.range(row)),
  );
}

function beacons(row: number) {
  return sensors
    .map((sensor) => sensor.beacon)
    .filter((pos) => pos[1] === row)
    .map((pos) => pos[0])
    .reduce((a, c) => (a.includes(c) ? a : [...a, c]), [] as number[]);
}

const sensors = lines.map((l) => new Sensor(l));
part1(sum(ranges(y).map((r) => r.size())) - beacons(y).length);

const size = example ? 20 : 4_000_000;

// start with last row because I bet the free spot is closer to the end ^^
for (let row = size - 1; row > -1; row--) {
  const r = ranges(row);
  if (r.length > 1) {
    const x = r[1].min - 1;
    part2(x * 4_000_000 + row);
    break;
  }
}
