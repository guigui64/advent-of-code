import {
  part1,
  part2,
  printTime,
  range,
  readLines,
  setDebug,
  startTimer,
  sum,
} from "./aoc.ts";

startTimer();
const example = false;
setDebug(example);
const lines = readLines(example);
const L = lines.length;

class Node {
  value: number;
  next?: Node;
  previous?: Node;

  constructor(value: number) {
    this.value = value;
  }

  toString() {
    return `${this.previous?.value} -> [${this.value}] -> ${this.next?.value}`;
  }

  move() {
    if (this.value === 0) return;
    const move = Math.abs(this.value) % (L - 1);
    // remove this from neighbors
    this.previous!.next = this.next;
    this.next!.previous = this.previous;
    // find new position
    for (let i = 0; i < move; i++) {
      if (this.value > 0) {
        this.next = this.next!.next;
        this.previous = this.previous!.next;
      } else {
        this.next = this.previous;
        this.previous = this.previous!.previous;
      }
    }
    // insert this
    this.previous!.next = this;
    this.next!.previous = this;
  }

  get(delta: number) {
    // deno-lint-ignore no-this-alias
    let n: Node = this;
    range(delta % L).forEach(() => n = n.next!);
    return n.value;
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
printTime();

startTimer();
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
printTime();
