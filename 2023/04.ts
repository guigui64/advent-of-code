import { Counter, log, part1, part2, range, readLines, sum } from "./aoc.ts";

globalThis.example = false;
const lines = readLines();
log(lines);

type Card = {
  id: number;
  winning: number[];
  numbers: number[];
};

function matchingCount(card: Card) {
  return card.numbers.filter((n) => card.winning.includes(n)).length;
}

function score(card: Card) {
  return range(matchingCount(card)).reduce(
    (score) => (score === 0 ? 1 : score * 2),
    0,
  );
}

const cards = lines
  .map((line) => line.match(/Card +(\d+): (.*) +\| +(.*)/)!)
  .map((match) => ({
    id: +match[1],
    winning: match[2].split(/\s+/).map(Number),
    numbers: match[3].split(/\s+/).map(Number),
  }));

// part1
part1(sum(cards.map(score)));

// part2
const counter = new Counter<number>();
for (const card of cards) {
  counter.inc(card.id);
  for (let i = 1; i <= matchingCount(card); i++) {
    counter.inc(card.id + i, counter.get(card.id));
  }
}
log(counter);
part2(sum([...counter.values()]));
