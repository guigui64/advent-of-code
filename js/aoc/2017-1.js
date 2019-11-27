// Advent of Code 2017 - Day 1 : Inverse Captcha

export function part1(input) {
  let sum = 0;
  for (let i = 0; i < input.length; i++) {
    if (input[i] == input[(i + 1) % input.length]) {
      sum += eval(input[i]);
    }
  }
  return sum;
}

export function part2(input) {
  let sum = 0;
  for (let i = 0; i < input.length; i++) {
    if (input[i] == input[(i + input.length/2) % input.length]) {
      sum += eval(input[i]);
    }
  }
  return sum;
}

export function all(input) {
  return [part1(input), part2(input)];
}
