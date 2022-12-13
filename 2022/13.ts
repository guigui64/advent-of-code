import {
  log,
  part1,
  part2,
  printTime,
  read,
  setDebug,
  startTimer,
  sum,
} from "./aoc.ts";

startTimer();
const example = false;
setDebug(example);
const pairs = read(example)
  .split("\n\n")
  .map((pair) => pair.trim().split("\n"));

log(pairs);

type Value = number | Value[];

// return <0 if right order, 0 if same, >0 if wrong order
function compare(left: Value, right: Value): number {
  // log(left, right);
  if (typeof left === "number" && typeof right === "number") {
    return left - right;
  } else if (typeof left !== "number" && typeof right !== "number") {
    let i = 0;
    while (i < left.length && i < right.length) {
      const cmp: number = compare(left[i], right[i]);
      if (cmp !== 0) {
        return cmp;
      }
      i++;
    }
    if (i === left.length && i === right.length) return 0;
    if (i === left.length) return -1;
    if (i === right.length) return 1;
  } else {
    if (typeof left === "number") {
      return compare([left], right);
    } else {
      return compare(left, [right]);
    }
  }
  throw Error("impossible case ???");
}

// part1
part1(
  sum(
    pairs
      .map(([left, right]) => compare(eval(left), eval(right)))
      .map((cmp, i) => (cmp < 0 ? i + 1 : 0)),
  ),
);
printTime();

// part2
const packets = [...pairs.flat(), "[[2]]", "[[6]]"];
packets.sort((left, right) => compare(eval(left), eval(right)));
part2((packets.indexOf("[[2]]") + 1) * (packets.indexOf("[[6]]") + 1));
printTime();
