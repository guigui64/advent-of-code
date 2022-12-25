import { log, part1, readLines, setDebug, sum } from "./aoc.ts";

const example = false;
setDebug(example);
const lines = readLines(example);

function snafuToDecimal(snafu: string) {
  const parts = snafu.split("").toReversed();
  let d = 0;
  parts.forEach((p, i) => {
    let dp = parseInt(p);
    if (isNaN(dp)) {
      if (p === "-") {
        dp = -1;
      } else {
        dp = -2;
      }
    }
    d += dp * (5 ** i);
  });
  return d;
}

function decimalToSnafu(decimal: number) {
  const parts = [];
  let i = 0;
  while (decimal > 2 * (5 ** i)) {
    i++;
  }
  let remaining = decimal;
  while (i >= 0) {
    const p = Math.round(remaining / (5 ** i));
    parts.push(p);
    remaining -= p * (5 ** i);
    i--;
  }
  let s = "";
  for (const part of parts) {
    if (part === -2) {
      s += "=";
    } else if (part === -1) {
      s += "-";
    } else {
      s += "" + part;
    }
  }
  return s;
}

const sumDecimal = sum(lines.map((l) => snafuToDecimal(l)));
log(sumDecimal);
part1(decimalToSnafu(sumDecimal));
