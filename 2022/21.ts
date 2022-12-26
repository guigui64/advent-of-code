import { log, part1, part2, readLines, setDebug } from "./aoc.ts";

const example = true;
setDebug(example);
const lines = readLines(example);

let operations: { [key: string]: string } = {};
let numbers: { [key: string]: number } = {};

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
  for (const monkey in operations) {
    let [op, a, b] = ["", "", ""];
    for (const o of "+-*/".split("")) {
      if (operations[monkey].includes(o)) {
        op = o;
        const operands = operations[monkey].split(` ${o} `);
        a = operands[0];
        b = operands[1];
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

operations = {};
numbers = {};

for (const line of lines) {
  const [monkey, rest] = line.split(": ");
  if (monkey === "humn") continue;
  if (monkey === "root") {
    operations[monkey] = rest.replace("+", "=");
    continue;
  }
  if ("+-*/".split("").some((s) => rest.includes(s))) {
    operations[monkey] = rest;
  } else {
    numbers[monkey] = parseInt(rest);
  }
}
while (true) {
  let stuck = true;
  for (const monkey in operations) {
    if (monkey === "root") continue;
    let [op, a, b] = ["", "", ""];
    for (const o of "+-*/".split("")) {
      if (operations[monkey].includes(o)) {
        op = o;
        const operands = operations[monkey].split(` ${o} `);
        a = operands[0];
        b = operands[1];
        break;
      }
    }
    if (numbers[a] !== undefined && numbers[b] !== undefined) {
      numbers[monkey] = comp(op, numbers[a], numbers[b]);
      delete operations[monkey];
      stuck = false;
    }
  }
  if (stuck) break;
}
Object.keys(operations).forEach((m1) => {
  Object.keys(numbers).forEach((m2) => {
    operations[m1] = operations[m1].replace(m2, "" + numbers[m2]);
  });
});
while (true) {
  const prev = operations["root"];
  Object.keys(operations)
    .filter((m) => m !== "root")
    .forEach(
      (m) => (operations["root"] = operations["root"].replace(
        m,
        `(${operations[m]})`,
      )),
    );
  if (operations["root"] === prev) break;
}

part2(operations["root"]);
