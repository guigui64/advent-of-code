import { DefaultDict, log, part1, part2, readLines, sum } from "./aoc.ts";

globalThis.example = false;
const lines = readLines();
log(lines);

type Page = {
  N: number;
  before: Set<number>;
  after: Set<number>;
};

function isValid(update: number[]) {
  // all pages before each must not be in its after set
  for (let i = 1; i < update.length; i++) {
    const current = update[i];
    if (
      update
        .slice(0, i)
        .some((previous) => rules.get(current).after.has(previous))
    ) {
      return false;
    }
  }
  return true;
}

function fixInvalidUpdate(update: number[]) {
  // sort each pair according to its rules until the whole sequence is valid
  do {
    update.sort((before, after) =>
      rules.get(before).after.has(after) ? -1 : 1,
    );
  } while (!isValid(update));
  return update;
}

function middlePage(update: number[]) {
  return update[Math.floor(update.length / 2)];
}

const rules = new DefaultDict<number, Page>((N) => ({
  N,
  before: new Set(),
  after: new Set(),
}));

const validUpdates: number[][] = [];
const fixedUpdates: number[][] = [];

let inRule = true;
for (const line of lines) {
  if (line === "") {
    inRule = false;
    continue;
  }
  if (inRule) {
    const [before, after] = line.split("|").map(Number);
    rules.get(before).after.add(after);
    rules.get(after).before.add(before);
  } else {
    const update = line.split(",").map(Number);
    if (isValid(update)) {
      validUpdates.push(update);
    } else {
      fixedUpdates.push(fixInvalidUpdate(update));
    }
  }
}

part1(sum(validUpdates.map(middlePage)));
part2(sum(fixedUpdates.map(middlePage)));
