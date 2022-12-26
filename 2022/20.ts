import { part1, part2, range, readLines, setDebug, sum } from "./aoc.ts";
import { makeDLL } from "./list.ts";

const example = false;
setDebug(example);
const lines = readLines(example);
const L = lines.length;

let Q = makeDLL(lines.map(Number));
let zero = Q.find((n) => n.value === 0)!;
Q.forEach((q) => q.move(q.value, L));
part1(sum(
  [1000, 2000, 3000].map((x) => x % L).map((x) => zero.get(x, L)),
));

const key = 811589153;
Q = makeDLL(lines.map((l) => key * parseInt(l)));
zero = Q.find((n) => n.value === 0)!;
range(10).forEach((_) => Q.forEach((q) => q.move(q.value, L)));
part2(sum(
  [1000, 2000, 3000].map((x) => x % L).map((x) => zero.get(x, L)),
));
