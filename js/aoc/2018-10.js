// Advent of Code 2018 - Day 10 : The Stars Align

function all(input, rounds = 20000, margin = 100) {
  let res = '';
  const re = /<(.*), (.*)>.*<(.*), (.*)>/;
  let points = [];
  for (let line of input.split(/\n/)) {
    const [px, py, vx, vy] = re.exec(line).slice(1).map(x => Number(x.trim()));
    let point = {
      pos : [px, py],
      vel : [vx, vy],
    }
    points.push(point);
  }
  for (let r = 0; r < rounds; r++) {
    let maxX = Math.max(...points.map(p => p.pos[0]));
    let maxY = Math.max(...points.map(p => p.pos[1]));
    let minX = Math.min(...points.map(p => p.pos[0]));
    let minY = Math.min(...points.map(p => p.pos[1]));
    if (minX + margin >= maxX && minY + margin >= maxY) {
      res += r + '\n';
      let s = '';
      for (let y = minY; y <= maxY; ++y) {
        for (let x = minX; x <= maxX; ++x) {
          if (points.some(p => p.pos[0] == x && p.pos[1] == y)) {
            s += '#';
          } else {
            s += '.';
          }
        }
        s += '\n';
      }
      res += s;
    }
    for (let p of points) {
      p.pos[0] += p.vel[0];
      p.pos[1] += p.vel[1];
    }
  }
  return res;
}

module.exports = { all };
