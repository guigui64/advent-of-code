// Advent of Code 2018 - Day 1 : Chronal Calibration

export function part1(input) {
  return eval(input.split(/\n/).join(''));
}

export function part2(input) {
  let frequencies = input.split(/\n/).map(eval);
  let index = 0;
  let currentF = frequencies[index++];
  let passedF = [currentF];
  while (true) {
    currentF += frequencies[index++];
    if (passedF.includes(currentF)) {
      return currentF;
    }
    passedF.push(currentF);
    if (index === frequencies.length) {
      index = 0;
    }
  }
}

export function all(input) {
  return [part1(input), part2(input)];
}
