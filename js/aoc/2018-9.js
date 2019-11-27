// Advent of Code 2018 - Day 9 : Marble Mania

function addAfter(value, marble) {
  const toAdd = { value, prev: marble, next: marble.next };
  marble.next.prev = toAdd;
  marble.next = toAdd;
  return toAdd;
}

function solve(nbPlayers, worthLast) {
  let players = []; // hold the scores of the players
  for (let p = 0; p < nbPlayers; ++p) players.push(0);
  let current = { value: 0 }; // 1st marble
  current.next = current;
  current.prev = current;
  let currentPlayer = 0;
  for (let m = 1; m <= worthLast; ++m) {
    if (m % 23 == 0) {
      players[currentPlayer] += m;
      current = current.prev.prev.prev.prev.prev.prev;
      players[currentPlayer] += current.prev.value;
      current.prev.prev.next = current;
      current.prev = current.prev.prev;
    } else {
      current = addAfter(m, current.next);
    }
    currentPlayer = (currentPlayer + 1) % nbPlayers;
  }
  return Math.max(...players);
}

function all(input) {
  const [nbPlayers, worthLast] = input.match(/\d+/g).map(Number);
  let part1 = solve(nbPlayers, worthLast);
  let part2 = solve(nbPlayers, worthLast * 100);
  return [ part1, part2 ];
}

module.exports = { all };
