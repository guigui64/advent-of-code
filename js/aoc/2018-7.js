// Advent of Code 2018 - Day 7 : The Sum of Its Parts

function all(input, nbWorkers = 5, offset = 60) {
  if (input == '') {
    console.log('No input');
    return;
  }
  const re = /Step (\w+) must be finished before step (\w+) can begin\./;
  let available = {};
  let prerequisites = {};
  let prerequisites2 = {};
  for (let line of input.split(/\n/)) {
    const [x, y] = re.exec(line).slice(1);
    if (available[x] === undefined) available[x] = [];
    if (available[y] === undefined) available[y] = [];
    available[x].push(y);
    if (prerequisites2[y] === undefined) prerequisites2[y] = 0;
    prerequisites2[y]++;
    if (prerequisites[y] === undefined) prerequisites[y] = 0;
    prerequisites[y]++;
  }
  for (let x in available) {
    available[x] = available[x].sort();
  }
  console.log(available);
  console.log(prerequisites);
  let queue = [];
  // Starting tasks
  for (let x in available) {
    if (!Object.keys(prerequisites).includes(x)) {
      queue.push(x);
    }
  }
  let order = [];
  while (queue.length > 0) {
    let curr = queue.sort()[0];
    // remove curr
    queue = queue.filter(x => x != curr);
    order.push(curr);
    for (let a of available[curr]) {
      prerequisites[a]--;
      prerequisites[a] == 0 && queue.push(a);
    }
  }
  console.log(order);
  let part1 = order.join('');
  /*
  // Part 2
  let workers = new Array(nbWorkers);
  for (let i = 0; i < nbWorkers; ++i) workers[i] = '.';
  queue = [];
  // Starting tasks
  for (let x in available) {
    if (!Object.keys(prerequisites2).includes(x)) {
      queue.push(x);
    }
  }
  for (let i in queue) {
    workers[i] = queue[i];
    queue = queue.filter(x => x != workers[i]);
    for (let a of available[workers[i]]) {
      prerequisites2[a]--;
      prerequisites2[a] == 0 && queue.push(a);
    }
  }
  let time = 0;
  while (workers.some(w => w != '.')) {
    console.log(time);
    console.log(workers);
    // Check tasks
    for (let w in workers) {
      let task = workers[w];
      if (task != '.' && time >= offset + (task.charCodeAt(0) - 'A'.charCodeAt(0) + 1)) {
        console.log('Finished task ' + task);
        queue = queue.filter(x => x != task);
        for (let a of available[task]) {
          prerequisites2[a]--;
          prerequisites2[a] == 0 && queue.push(a);
        }
        workers[w] = '.';
        task = '.';
      }
      if (task == '.' && queue.length > 0) {
        workers[w] = queue.sort()[0];
      }
    }
    time++;
  }
  */
  let part2 = 'Not implemented yet';
  return [ part1, part2 ];
}

module.exports = { all };
