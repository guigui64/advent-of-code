import { part1, part2, printTime, readLines, startTimer, sum } from "./aoc.ts";

type File = {
  parent?: File;
  children: File[];
  fullname: string;
  size: number;
};
function newFile(name: string, parent?: File, size = 0): File {
  return {
    parent,
    children: [],
    fullname: parent ? parent.fullname + "/" + name : name,
    size,
  };
}

const sizes: Map<string, number> = new Map();
function size(file: File) {
  if (file.children.length === 0) {
    // this is not a dir: simply return the file size, no need to store in map
    return file.size;
  }
  if (!sizes.has(file.fullname)) {
    sizes.set(file.fullname, sum(file.children.map(size)));
  }
  return sizes.get(file.fullname)!;
}

startTimer();
const lines = readLines(false);
const root = newFile("/");
let dir = root;
for (const line of lines) {
  if (line.startsWith("$ cd /")) {
    dir = root;
  } else if (line.startsWith("$ cd ..")) {
    dir = dir.parent || root; // fancy real FS emulation :)
  } else if (line.startsWith("$ cd")) {
    const newDir = newFile(line.slice(5), dir);
    dir.children.push(newDir);
    dir = newDir;
  } else if (line.startsWith("$ ls")) {
    continue;
  } else if (line.startsWith("dir")) {
    continue;
  } else {
    const [size, name] = line.split(" ");
    dir.children.push(newFile(name, dir, parseInt(size)));
  }
}
const total = size(root);
part1(sum(Array.from(sizes.values()).filter((s) => s <= 100_000)));
printTime();

// part2
part2(
  Math.min(
    ...Array.from(sizes.values()).filter(
      (size) => size >= 30_000_000 - (70_000_000 - total),
    ),
  ),
);
printTime();
