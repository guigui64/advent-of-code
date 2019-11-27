// Advent of Code 2018 - Day 2 : Inventory Management System

export function part1(input) {
  const uniq = (array) => {
    return array.filter((x, i, self) => self.indexOf(x) === i);
  };
  let count2 = 0, count3 = 0;
  for (let line of input.split(/\n/)) {
    const array = line.split('');
    let has2 = false, has3 = false;
    for (let letter of uniq(array)) {
      has2 |= array.filter(x => x === letter).length === 2;
      has3 |= array.filter(x => x === letter).length === 3;
    }
    if (has2) count2++;
    if (has3) count3++;
  }
  return count2 * count3;
}

export function part2(input) {
  const differingIndexes = (a1, a2) => {
    let indexes = [];
    for (let i = 0; i < a1.length; ++i) {
      if (a1[i] !== a2[i]) indexes.push(i);
    }
    return indexes;
  };
  const lines = input.split(/\n/);
  for (let i = 0; i < lines.length; ++i) {
    for (let j = 0; j < lines.length; ++j) {
      if (i === j) continue;
      const indexes = differingIndexes(lines[i].split(''), lines[j].split(''));
      if (indexes.length === 1) {
        return lines[i].slice(0, indexes[0]).concat(lines[i].slice(indexes[0]+1));
      }
    }
  }
  return 'Not found';
}

export function all(input) {
  return [part1(input), part2(input)];
}
