import { log, part1, part2, readLines } from "./aoc.ts";

globalThis.example = true;
globalThis.verbose = true;
const lines = readLines();
log(lines);

// part1
{
  let ln = 0;
  const seeds = lines[ln++].split(": ")[1].split(" ").map(Number);
  log(seeds);
  const current = [...seeds];
  let previous = [...seeds];
  while (++ln < lines.length) {
    if (lines[ln] === "") {
      previous = [...current];
      continue;
    }
    const [dest, src, length] = lines[ln].split(" ").map(Number);
    previous.forEach((prev, i) => {
      if (prev >= src && prev < src + length) {
        current[i] = dest + (prev - src);
      }
    });
  }
  part1(Math.min(...current));
}

class Range {
  constructor(
    readonly start: number,
    readonly length: number,
  ) {}
  /** exclusive */
  get end() {
    return this.start + this.length;
  }
  toString() {
    return `[${this.start};${this.end}[(${this.length})`;
  }
  /** returns an array where the first item is the intersection and the rest ranges of non intersected numbers from this */
  slice(other: Range) {
    if (other.start < this.start) {
      if (other.end < this.start) {
        // no intersection - before
        return [null, this];
      } else {
        if (other.end > this.end) {
          // bigger - before and after
          return [this];
        } else {
          // some in common at begginning of this
          return [
            new Range(this.start, other.end - this.start + 1),
            new Range(other.end + 1, this.end - other.end),
          ];
        }
      }
    } else {
      if (other.start > this.end) {
        // no intersection - after
        return [null, this];
      } else {
        if (other.end < this.end) {
          // inside
          return [
            other,
            new Range(this.start, other.start - this.start),
            new Range(other.end + 1, this.end - other.end),
          ];
        } else {
          // some in common at end of this
          return [
            new Range(other.start, this.end - other.start + 1),
            new Range(this.start, other.start - this.start),
          ];
        }
      }
    }
  }
  join(other: Range) {
    const [common, ...rest] = this.slice(other);
    if (common === null) {
      return rest; // no intersection
    }
    const start = Math.min(this.start, other.start);
    return [new Range(start, Math.max(this.end, other.end) - start + 1)];
  }
}
// const T = new Range(10, 10);
// log(T.slice(new Range(0, 30))?.map(String)); // bigger - before and after
// log(T.slice(new Range(0, 10))?.map(String)); // no intersection - before
// log(T.slice(new Range(0, 11))?.map(String)); // 1 in common - before
// log(T.slice(new Range(0, 15))?.map(String)); // 5 in common - before
// log(T.slice(new Range(20, 10))?.map(String)); // no intersection - after
// log(T.slice(new Range(12, 5))?.map(String)); // inside
// log(T.slice(new Range(19, 10))?.map(String)); // 1 in common - after
// log(T.slice(new Range(15, 10))?.map(String)); // 5 in common - after
// log(T.join(new Range(20, 10))?.map(String));
// log(T.join(new Range(0, 15))?.map(String));
// log(T.join(new Range(0, 45))?.map(String));

// Thanks chat GPT
function joinRanges(ranges: Range[]): Range[] {
  if (ranges.length <= 1) {
    return ranges;
  }

  // Sort ranges by start value
  ranges.sort((a, b) => a.start - b.start);

  const result: Range[] = [ranges[0]];

  for (let i = 1; i < ranges.length; i++) {
    const currentRange = ranges[i];
    const lastMergedRange = result[result.length - 1];

    if (currentRange.start <= lastMergedRange.end) {
      // Ranges overlap or touch, merge them
      result[result.length - 1] = new Range(
        lastMergedRange.start,
        Math.max(lastMergedRange.end, currentRange.end) -
          lastMergedRange.start +
          1,
      );
    } else {
      // Ranges do not overlap, add the current range to the result
      result.push(currentRange);
    }
  }

  return result;
}

// part2
{
  let ln = 0;
  const seedsSpec = lines[ln].split(": ")[1].split(" ").map(Number);
  const seeds: Range[] = [];
  for (let i = 0; i < seedsSpec.length; i += 2) {
    seeds.push(new Range(seedsSpec[i], seedsSpec[i + 1]));
  }
  const mins: number[] = [];
  for (const seed of seeds) {
    let current: Range[] = [];
    let previous: Range[] = [seed];
    while (++ln < lines.length) {
      if (lines[ln] === "") {
        log(previous.map(String));
        log(lines[ln + 1]);
        ln++; // skip text part
        continue;
      }
      const [dest, src, length] = lines[ln].split(" ").map(Number);
      previous.forEach((prev) => {
        const [common, ...rest] = prev.slice(new Range(src, length));
        // log(common?.toString(), rest.map(String));
        if (common !== null) {
          current.push(new Range(common.start + (dest - src), common.length));
        }
        if (rest.length > 0) {
          current.push(...rest);
        }
      });
      current = joinRanges(current);
      previous = [...current];
      current = [];
    }
    mins.push(previous[0].start);
  }
  part2(Math.min(...mins));
}
