// Advent of Code 2017 - Day 2 : Corruption Checksum

export function part1(input) {
  let res = 0;
  input.split('\n').forEach((line) => {
    let min = Number.MAX_VALUE, max = 0;
    line.split(/\s+/).forEach((num) => {
      if (num < min) {
        min = Number.parseInt(num);
      }
      if (num > max) {
        max = Number.parseInt(num);
      }
    });
    res += max - min;
  });
  return res;
}

export function part2(input) {
  let res = 0;
  input.split('\n').forEach((line) => {
    const nums = line.split(/\s+/).map(x => Number.parseInt(x));
    outter : for (let i = 0; i < nums.length; ++i) {
      for (let j = 0; j < nums.length; ++j) {
        if (i != j && (nums[i] % nums[j]) == 0) {
          res += nums[i]/nums[j];
          break outter;
        }
      }
    }
  });
  return res;
}

export function all(input) {
  return [part1(input), part2(input)];
}
