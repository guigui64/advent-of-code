import { part1, part2, readLines } from "./aoc.ts";

const lines = readLines(false);

function len(section: number[]) {
  return section[1] - section[0];
}

function contained(big: number[], small: number[]) {
  return small[0] >= big[0] && small[1] <= big[1];
}

function overlap(big: number[], small: number[]) {
  const [s0, s1, b0, b1] = [small[0], small[1], big[0], big[1]];
  return (b0 <= s0 && s0 <= b1) || (b0 <= s1 && s1 <= b1);
}

let cntContained = 0;
let cntOverlap = 0;
for (const pair of lines) {
  const [sections1, sections2] = pair
    .split(",")
    .map((s) => s.split("-").map(Number));
  const [biggest, smallest] = len(sections1) > len(sections2)
    ? [sections1, sections2]
    : [sections2, sections1];
  if (contained(biggest, smallest)) {
    cntContained++;
  }
  if (overlap(biggest, smallest)) {
    cntOverlap++;
  }
  // console.log(pair, cntContained, cntOverlap);
}
part1(cntContained);
part2(cntOverlap);
