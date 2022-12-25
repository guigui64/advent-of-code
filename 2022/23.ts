import { log, part1, part2, Point, range, readLines, setDebug } from "./aoc.ts";
import { makeDLL } from "./list.ts";

const example = false;
setDebug(example);
const lines = readLines(example);

const North = [[0, -1], [1, -1], [-1, -1]];
const South = [[0, 1], [1, 1], [-1, 1]];
const West = [[-1, 0], [-1, -1], [-1, 1]];
const East = [[1, 0], [1, -1], [1, 1]];

const elves: Point[] = [];
lines.forEach((line, y) => {
  line.split("").forEach((c, x) => {
    if (c === "#") {
      elves.push([x, y]);
    }
  });
});

function print() {
  if (!example) return;
  const minx = Math.min(...elves.map(([x, _]) => x));
  const maxx = Math.max(...elves.map(([x, _]) => x));
  const miny = Math.min(...elves.map(([_, y]) => y));
  const maxy = Math.max(...elves.map(([_, y]) => y));
  for (let y = miny; y <= maxy; y++) {
    let s = "";
    for (let x = minx; x <= maxx; x++) {
      s += elves.find(([xx, yy]) => xx === x && yy === y) === undefined
        ? "."
        : "#";
    }
    console.log(s);
  }
}
// print();

function count() {
  let n = 0;
  const minx = Math.min(...elves.map(([x, _]) => x));
  const maxx = Math.max(...elves.map(([x, _]) => x));
  const miny = Math.min(...elves.map(([_, y]) => y));
  const maxy = Math.max(...elves.map(([_, y]) => y));
  for (let y = miny; y <= maxy; y++) {
    for (let x = minx; x <= maxx; x++) {
      if (elves.find(([xx, yy]) => xx === x && yy === y) === undefined) {
        n++;
      }
    }
  }
  return n;
}

function alone(p: Point) {
  const [x, y] = p;
  return [North, South, West, East].every((dir) =>
    dir.every(([dx, dy]) =>
      !elves.some((e) => e.toString() === [x + dx, y + dy].toString())
    )
  );
}

let roundDir = makeDLL([North, South, West, East])[0];
let round = 0;
while (true) {
  round++;
  console.log("Round", round);
  const propositions: Point[] = [];
  let noMove = true;
  for (let i = 0; i < elves.length; i++) {
    let elfDir = roundDir;
    const elf = elves[i];
    const otherElves = elves.filter((_, j) => j !== i).map((e) => e.toString());
    let found = false;
    if (alone(elf)) {
      propositions.push(elf);
      continue;
    }
    noMove = false;
    for (const _ of range(4)) {
      if (
        elfDir.value.every(([dx, dy]) =>
          !otherElves.includes([elf[0] + dx, elf[1] + dy].toString())
        )
      ) {
        propositions.push([
          elf[0] + elfDir.value[0][0],
          elf[1] + elfDir.value[0][1],
        ]);
        found = true;
        break;
      }
      elfDir = elfDir.next!;
    }
    if (!found) {
      propositions.push(elf);
    }
  }
  if (noMove) {
    part2(round);
    break;
  }
  roundDir = roundDir.next!;
  for (let i = 0; i < elves.length; i++) {
    const proposition = propositions[i];
    const otherPropositions = propositions.filter((_, j) => i !== j).map((p) =>
      p.toString()
    );
    if (!otherPropositions.includes(proposition.toString())) {
      elves[i] = proposition;
    }
  }
  // print();
  if (round === 10) {
    part1(count());
  }
}
