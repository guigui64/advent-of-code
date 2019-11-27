// Advent of Code 2018 - Day 8 : Memory Maneuver

function all(input) {
  let numbers = input.split(' ').map(Number);
  let root = {};
  let i = 0;
  let metaSum = 0;
  function step(curr) {
    curr.header = {
      nbChild : numbers[i++],
      nbMeta : numbers[i++],
    };
    curr.childNodes = [];
    curr.metaData = [];
    for (let x = 0; x < curr.header.nbChild; ++x) {
      let prev = curr;
      curr = {};
      prev.childNodes.push(curr);
      step(curr);
      curr = prev;
    }
    curr.metaData = numbers.slice(i, i + curr.header.nbMeta);
    i += curr.header.nbMeta;
    // Part 1 : sum metadatas
    curr.metaData.forEach(m => metaSum += m);
    // Part 2 : compute score
    curr.score = 0;
    if (curr.header.nbChild == 0) {
      curr.metaData.forEach(m => curr.score += m);
    } else {
      for (let index of curr.metaData) {
        if (curr.childNodes[index-1]) curr.score += curr.childNodes[index-1].score;
      }
    }
  }
  step(root);
  console.log(JSON.stringify(root));
  let part1 = metaSum;
  let part2 = root.score;
  return [ part1, part2 ];
}

module.exports = { all };
