// Advent of Code 2018 - Day 6 : Chronal Coordinates

function distance(a, b) {
  return Math.abs(a[0] - b[0]) + Math.abs(a[1] - b[1]);
}

function all(input, safeRadius = 10000) {
  const re = /(\d+), (\d+)/;
  let coords = [];
  let maxX = 0, maxY = 0;
  input.split(/\n/).forEach(line => {
    line = line.trim();
    if (line != '') {
      const [x, y] = re.exec(line).slice(1, 3).map(Number);
      if (x > maxX) maxX = x;
      if (y > maxY) maxY = y;
      coords.push([x, y]);
    }
  });
  /*let strMap = '';
  for (let x = 0; x < maxX + 1; ++x) {
    for (let y = 0; y < maxY + 1; ++y) {
      if (coords.some(([a, b]) => a == x && b == y)) strMap += '#';
      else strMap += '.';
    }
    strMap += '\n';
  }
  console.log(strMap);*/
  let area = {};
  let infinite = new Set();
  let safe = [];
  // For each point of the map, find the closest available coord
  for (let x = 0; x <= maxX; ++x) {
    for (let y = 0; y <= maxY; ++y) {
      let bestDist = maxX + maxY, closestCoordIdx = -1, totalDist = 0;
      for (let idx in coords) {
        const dist = distance([x,y], coords[idx]);
        totalDist += dist;
        if (dist < bestDist) {
          bestDist = dist;
          closestCoordIdx = idx;
        } else if (dist == bestDist) { // x,y is equidistant to two or more points, don't count it
          closestCoordIdx = -1;
        }
      }
      if (area[closestCoordIdx] === undefined) {
        area[closestCoordIdx] = 1;
      } else {
        area[closestCoordIdx]++;
      }
      if (x == 0 || x == maxX || y == 0 || y == maxY) {
        // This point belongs to an infinite area because we are on the 'border'
        infinite.add(closestCoordIdx);
      }
      // part2
      if (totalDist < safeRadius) {
        safe.push([x,y]);
      }
    }
  }
  let max = 0;
  for (let idx in area) {
    if (!infinite.has(idx) && area[idx] > max) {
      max = area[idx];
    }
  }
  let part1 = max;
  let part2 = safe.length;
  return [ part1, part2 ];
}

module.exports = { all };
