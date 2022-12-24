import { part1, part2, readLines, setDebug, sum } from "./aoc.ts";
import DLLEntry from "./list.ts";

const example = false;
setDebug(example);
const lines = readLines(example);
const L = lines.length;

class Node extends DLLEntry<number> {
  move() {
    return super.move(this.value, L);
  }

  get(delta: number) {
    return super.get(delta, L);
  }
}

let Q = [];
for (const line of lines) {
  Q.push(new Node(parseInt(line)));
  if (Q.length > 1) {
    Q[Q.length - 2].next = Q[Q.length - 1];
    Q[Q.length - 1].previous = Q[Q.length - 2];
  }
}
Q[Q.length - 1].next = Q[0];
Q[0].previous = Q[Q.length - 1];
let zero = Q.find((n) => n.value === 0)!;
while (Q.length > 0) {
  Q.shift()!.move();
}
part1(sum(
  [1000, 2000, 3000].map((x) => x % L).map((x) => zero.get(x)),
));

const key = 811589153;
Q = [];
for (const line of lines) {
  Q.push(new Node(key * parseInt(line)));
  if (Q.length > 1) {
    Q[Q.length - 2].next = Q[Q.length - 1];
    Q[Q.length - 1].previous = Q[Q.length - 2];
  }
}
Q[Q.length - 1].next = Q[0];
Q[0].previous = Q[Q.length - 1];
zero = Q.find((n) => n.value === 0)!;
for (let i = 0; i < 10; i++) {
  for (let q = 0; q < Q.length; q++) {
    Q[q].move();
  }
}
part2(sum(
  [1000, 2000, 3000].map((x) => x % L).map((x) => zero.get(x)),
));
