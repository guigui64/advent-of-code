import { log, part1, part2, range, readLines, setDebug } from "./aoc.ts";

class Monkey {
  id: number;
  items: number[];
  operation: string;
  diviser: number;
  throwTrue: number;
  throwFalse: number;
  counter = 0;

  constructor(input: string[]) {
    this.id = parseInt(input[0].slice(7));
    this.items = input[1].split(": ")[1].split(", ").map(Number);
    this.operation = input[2].split("new = ")[1];
    this.diviser = parseInt(input[3].split("by ")[1]);
    this.throwTrue = parseInt(input[4].split("monkey ")[1]);
    this.throwFalse = parseInt(input[5].split("monkey ")[1]);
  }
}

const example = false;
setDebug(example);
const lines = readLines(example);
lines.push("");

const nbMonkeys = lines.length / 7;
for (const part of [1, 2]) {
  const monkeys = [];
  for (let i = 0; i < nbMonkeys; i++) {
    monkeys.push(new Monkey(lines.slice(i * 7, i * 7 + 6)));
  }

  const allModulos = monkeys.map((m) => m.diviser).reduce((a, c) => a * c, 1);
  for (const round of range(part === 1 ? 20 : 10000)) {
    for (const monkey of monkeys) {
      while (monkey.items.length > 0) {
        const item = monkey.items.shift()!;
        const oper = monkey.operation.replaceAll("old", item.toString());
        let worryLvl: number = eval(oper);
        if (part === 1) {
          worryLvl = Math.floor(worryLvl / 3);
        } else {
          worryLvl %= allModulos;
        }
        const monkeyDst = monkeys[
          (worryLvl % monkey.diviser === 0)
            ? monkey.throwTrue
            : monkey.throwFalse
        ];
        monkeyDst.items.push(worryLvl);
        monkey.counter++;
      }
    }
    if (round + 1 === 1 || round + 1 === 20 || (round + 1) % 1000 === 0) {
      log(round + 1, monkeys.map((m) => m.counter));
    }
  }
  const amounts = monkeys.map((m) => m.counter);
  log(amounts);
  amounts.sort((a, b) => b - a);
  if (part === 1) {
    part1(amounts[0] * amounts[1]);
  } else {
    part2(amounts[0] * amounts[1]);
  }
}
