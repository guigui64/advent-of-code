// Advent of Code 2017 - Day 3 : Spiral Memory

export function part1(input) {
  /* Explanation:
   * The bottom right corner of each square form a sequence of odd perfect
   * squares (3*3=9, 5*5=25...).
   * We find the closest corner to the input n.
   * We know that the distance to this corner is n-1.
   * The result is then n-1 minus the distance between the corner and the
   * input.
   */
  let min = input;
  let corner = 0;
  for (let i = 3; i < 1000 ; i+=2) {
    if (i*i < input) continue;
    if (Math.abs(i*i - input) < min) {
      corner = i;
      min = Math.abs(i*i - input);
    } else {
      break;
    }
  }
  let dist = Math.abs(corner - 1 - Math.abs(corner*corner - input));
  return dist;
}

export function part2(input) {
  const oeis=`Solution found here : https://oeis.org/A141481`
  return oeis;
}

export function all(input) {
  return [part1(input), part2(input)];
}
