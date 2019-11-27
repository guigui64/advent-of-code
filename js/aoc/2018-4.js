// Advent of Code 2018 - Day 4 : Repose Record

function all(input) {
  let log = new Map();
  for (let line of input.split(/\n/)) {
    line = line.trim();
    if (line == "") continue;
    const date = new Date(line.slice(1, line.indexOf(']')));
    let event = -1, guardId = -1;
    if (line.includes('begins')) {
      event = 'begins';
      guardId = /#(\d+)/.exec(line)[1];
    } else if (line.includes('falls asleep')) {
      event = 'falls asleep';
    } else if (line.includes('wakes up')) {
      event = 'wakes up';
    }
    log.set(date, { event, guardId });
  }
  // Sort with the dates
  log = new Map([...log.entries()].sort((a,b) => a[0] - b[0]));
  let guardId = -1;
  let latestAsleep;
  let counts = {};
  let datesAsleep = {};
  for (let [date, entry] of log) {
    if (entry.event == 'begins') {
      guardId = entry.guardId;
      if (counts[guardId] === undefined) counts[guardId] = [ 0 ];
      else counts[guardId].push(0);
      if (datesAsleep[guardId] === undefined) datesAsleep[guardId] = {};
    } else if (entry.event == 'falls asleep') {
      latestAsleep = date;
    } else { // wakes up
      counts[guardId][counts[guardId].length - 1] += (date - latestAsleep) / 60000;
      for (let d = latestAsleep; d < date; d.setMinutes(d.getMinutes() + 1)) {
        if (datesAsleep[guardId][d.getMinutes()] === undefined) datesAsleep[guardId][d.getMinutes()] = 1;
        else datesAsleep[guardId][d.getMinutes()]++;
      }
    }
  }
  // Find most asleep guard
  let max = 0;
  for (let g in counts) {
    let sum = counts[g].reduce((a,b) => a + b);
    if (sum > max) {
      max = sum;
      guardId = g;
    }
  }
  // Find most asleep minute
  let minute = 0;
  max = 0;
  for (let m in datesAsleep[guardId]) {
    if (datesAsleep[guardId][m] > max) {
      max = datesAsleep[guardId][m];
      minute = m;
    }
  }
  let part1 = guardId * minute;
  // Find most alseep minute for all guards
  max = 0;
  for (let g in datesAsleep) {
    for (let m in datesAsleep[g]) {
      if (datesAsleep[g][m] > max) {
        max = datesAsleep[g][m];
        minute = m;
        guardId = g;
      }
    }
  }
  let part2 = guardId * minute;
  return [part1, part2];
}

module.exports = { all };
