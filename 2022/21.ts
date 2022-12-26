import { log, part1, part2, readLines, setDebug } from "./aoc.ts";

const example = false;
setDebug(example);
const lines = readLines(example);

const operations: { [key: string]: string } = {};
const numbers: { [key: string]: number } = {};

for (const line of lines) {
  const [monkey, rest] = line.split(": ");
  if ("+-*/".split("").some((s) => rest.includes(s))) {
    operations[monkey] = rest;
  } else {
    numbers[monkey] = parseInt(rest);
  }
}

function comp(op: string, a: number, b: number) {
  switch (op) {
    case "+":
      return a + b;
    case "-":
      return a - b;
    case "*":
      return a * b;
    case "/":
      return a / b;
  }
  throw new Error("aoc lies");
}

while (!numbers["root"]) {
  log(numbers);
  for (const monkey in operations) {
    log(monkey, operations[monkey]);
    let [op, a, b] = ["", "", ""];
    for (const o of "+-*/".split("")) {
      if (operations[monkey].includes(o)) {
        op = o;
        const operands = operations[monkey].split(` ${o} `);
        a = operands[0];
        b = operands[1];
        log(op, a, b);
        break;
      }
    }
    if (numbers[a] !== undefined && numbers[b] !== undefined) {
      numbers[monkey] = comp(op, numbers[a], numbers[b]);
      delete operations[monkey];
      break;
    }
  }
}

part1(numbers["root"]);

// part2
// first, simplify input by computing all constant numbers (monkeys that do not depend on humn)
// then, resolve root's equation
part2("TODO");
