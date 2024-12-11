import { log, part1, part2, readLines, sum } from "./aoc.ts";

globalThis.example = true;
const lines = readLines();
log(lines);

const entries = lines
  .map((line) => line.split(": "))
  .map(([res, equation]) => ({ result: +res, equation }));

function works(equation: string, result: number, withConcat = false): boolean {
  if (!equation.includes(" ")) {
    return eval(equation) === result;
  }
  return (
    works(
      equation.replace(/(\d+) (\d+)/, (_, p1, p2) => eval(`${p1}+${p2}`)),
      result,
      withConcat,
    ) ||
    works(
      equation.replace(/(\d+) (\d+)/, (_, p1, p2) => eval(`${p1}*${p2}`)),
      result,
      withConcat,
    ) ||
    (withConcat &&
      works(equation.replace(/(\d+) (\d+)/, `$1$2`), result, withConcat))
  );
}

// part1
part1(
  sum(
    entries
      .filter(({ equation, result }) => works(equation, result))
      .map(({ result }) => result),
  ),
);

// part2
part2(
  sum(
    entries
      .filter(({ equation, result }) => works(equation, result, true))
      .map(({ result }) => result),
  ),
);
