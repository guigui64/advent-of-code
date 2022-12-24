import { part1, part2, readLines } from "./aoc.ts";

const input = readLines()[0];

function findMarkerIdx(stream: string, size = 4) {
  for (let i = size; i < stream.length; i++) {
    if (new Set(stream.slice(i - size, i)).size === size) {
      return i;
    }
  }
  throw Error("stream has no marker!");
}

part1(findMarkerIdx(input));
part2(findMarkerIdx(input, 14));
