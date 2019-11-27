// Advent of Code 2018 - Day 5 : Alchemical Reduction

const DIFF = Math.abs('a'.charCodeAt(0) - 'A'.charCodeAt(0));
function removeAllUnits(s) {
  let finished = true;
  let i = 0;
  while (i < s.length - 1) {
    if (Math.abs(s.charCodeAt(i) - s.charCodeAt(i+1)) == DIFF) {
      finished = false;
      s = s.slice(0, i).concat(s.slice(i+2));
      continue;
    }
    i++;
  }
  if (!finished) {
    return removeAllUnits(s);
  }
  return s;
}

function filter(s, u) {
  let i = 0;
  while (i < s.length) {
    if (s.charCodeAt(i) === u || s.charCodeAt(i) === u + DIFF) {
      s = s.slice(0, i).concat(s.slice(i+1));
      continue;
    }
    i++;
  }
  return s;
}

function all(input) {
  let part1 = removeAllUnits(input).length;
  let min = input.length;
  for (let unit = 'A'.charCodeAt(0); unit <= 'Z'.charCodeAt(0); ++unit) {
    let filtered = filter(input, unit);
    let len = removeAllUnits(filtered).length;
    if (len < min) {
      min = len;
    }
  }
  let part2 = min;
  return [ part1, part2 ];
}

module.exports = { all };
