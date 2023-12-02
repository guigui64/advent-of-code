import { log, part1, part2, product, readLines, sum } from "./aoc.ts";

globalThis.example = false;
const lines = readLines();
log(lines);

const games = lines
  .map((line) => line.match(/Game (\d+): (.*)/))
  .map((match) => ({
    game: Number(match![1]),
    subsets: match![2]
      .split("; ")
      .map((subset) =>
        subset
          .split(", ")
          .map((s) => s.split(" ").toReversed())
          .map(([color, n]) => [color, Number(n)] as [string, number]),
      )
      .map((s) => new Map(s)),
  }));
log(games);

const colors = ["red", "green", "blue"] as const;
const req = new Map([
  ["red", 12],
  ["green", 13],
  ["blue", 14],
]);

// part1
part1(
  sum(
    games
      .filter((game) =>
        colors.every((color) =>
          game.subsets.every(
            (subset) => req.get(color)! >= (subset.get(color) ?? 0),
          ),
        ),
      )
      .map((game) => game.game),
  ),
);

// part2
part2(
  sum(
    games.map((game) =>
      product(
        colors.map((color) =>
          Math.max(...game.subsets.map((s) => s.get(color) ?? 0)),
        ),
      ),
    ),
  ),
);
