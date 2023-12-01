import { log, part1, part2, readLines, sum } from "./aoc.ts";

globalThis.example = false;
const lines = readLines();
log(lines);

// part1
part1(
  sum(
    lines
      .map((line) => line.match(/\d/g))
      .filter((it) => it) // match could return null on lines without digits
      .map((it) => Array.from(it!))
      .map((a) => a[0] + a[a.length - 1])
      .map(Number),
  ),
);

// part2
const digits = [
  "one",
  "two",
  "three",
  "four",
  "five",
  "six",
  "seven",
  "eight",
  "nine",
];
part2(
  sum(
    lines
      .map(
        (line) =>
          line.matchAll(
            /(?=(one|two|three|four|five|six|seven|eight|nine|\d))/g,
          ),
        // using the positive lookahead group catpture (?=...) so that characters are not consumed
        // for string 'oneight', (?=(one|eight)) will match 'one' and 'eight' whereas (one|eight) will only match 'one'
      )
      .map((it) => Array.from(it!).map((match) => match[1]))
      .map(
        (a) =>
          [a[0], a[a.length - 1]]
            .map((d) => digits.indexOf(d) + 1 || d)
            .join(""), // using a trick here: if not found, index is -1, -1 + 1 = 0 = false :p
      )
      .map(Number),
  ),
);
