// Advent of Code 2018 - Day 11 : Chronal Charge

function compute(x, y, serial) {
  let rackId = x + 10;
  let power = rackId * y;
  power += serial;
  power *= rackId;
  power = (Math.floor(power / 100) - (Math.floor(power / 1000) * 10));
  power -= 5;
  return power;
}

function createGrid(serial) {
  let grid = [];
  for (let x = 1; x <= 300; ++x) {
    grid[x] = [];
    for (let y = 1; y <= 300; ++y) {
      grid[x][y] = compute(x, y, serial);
    }
  }
  return grid;
}

function solve(grid, size) {
  let maxPower = 0, X = 0, Y = 0;
  for (let x = 1; x <= 300 - size; ++x) {
    for (let y = 1; y <= 300 - size; ++y) {
      let totalPower = 0;
      for (let i = x; i < x + size; ++i) {
        for (let j = y; j < y + size; ++j) {
          totalPower += grid[i][j];
        }
      }
      if (totalPower > maxPower) {
        maxPower = totalPower;
        [X, Y] = [x, y];
      }
    }
  }
  return [maxPower, X, Y];
}

function all(input) {
  const serial = Number(input.trim());
  const grid = createGrid(serial);
  const [_, X1, Y1] = solve(grid, 3);
  let part1 = `${X1},${Y1}`;
  // console.log('Part 1 : ' + part1);
  let [ maxPower, X2, Y2, S2 ] = [ 0, 0, 0, 0 ];
  for (let size = 1; size <= 300; ++size) {
    [ power, x, y ] = solve(grid, size);
    if (power == 0) break;
    // console.log('For size ' + size + ' => power = ' + power + ' for x,y = ' + x + ',' + y);
    if (power > maxPower) {
      maxPower = power;
      X2 = x;
      Y2 = y;
      S2 = size;
    }
  }
  let part2 = `${X2},${Y2},${S2}`;
  return [ part1, part2 ];
}

module.exports = { all };
