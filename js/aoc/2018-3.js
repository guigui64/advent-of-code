// Advent of Code 2018 - Day 3 : No Matter How You Slice It

function all(input) {
  // Example input line : #12 @ 429,177: 12x27
  const regex = /#(\d+) @ (\d+),(\d+): (\d+)x(\d+)/;
  let map = {};
  for (let line of input.split(/\n/)) {
    line = line.trim();
    if (line == "") continue;
    const [id, x, y, dx, dy] = line.match(regex).slice(1).map(x => Number(x));
    for (let i = x; i < x + dx; ++i) {
      for (let j = y; j < y + dy; ++j) {
        let inch = i + ',' + j;
        if (map[inch] === undefined) map[inch] = [];
        map[inch].push(id);
      }
    }
  }
  const overlappingInches = Object.keys(map).filter(x => map[x].length > 1);
  let overlappingClaims = [];
  overlappingInches.forEach(x => map[x].forEach(
    y => overlappingClaims.includes(y) || overlappingClaims.push(y)));
  const onlyClaim = map[Object.keys(map).find(
    x => map[x].length == 1 && !overlappingClaims.includes(map[x][0]))][0];
  return [ overlappingInches.length, onlyClaim ];
}

module.exports = { all };
