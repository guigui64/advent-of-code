import { part1, part2, readLines, sum } from "./aoc.ts";

class File {
  parent?: File;
  children: File[];
  fullname: string;
  size: number;

  constructor(name: string, parent?: File, size = 0) {
    this.parent = parent;
    this.children = [];
    this.fullname = parent ? parent.fullname + "/" + name : name;
    this.size = size;
  }

  // store sizes per dir to get solutions of both parts + use as cache
  static sizes: Map<string, number> = new Map();
  getSize() {
    if (this.children.length === 0) {
      // this is not a dir: simply return the this size, no need to store in map
      return this.size;
    }
    if (!File.sizes.has(this.fullname)) {
      File.sizes.set(this.fullname, sum(this.children.map((f) => f.getSize())));
    }
    return File.sizes.get(this.fullname)!;
  }
}

const lines = readLines(false);
const root = new File("/");
let dir = root;
for (const line of lines) {
  if (line.startsWith("$ cd /")) {
    dir = root;
  } else if (line.startsWith("$ cd ..")) {
    dir = dir.parent || root; // fancy real FS emulation :)
  } else if (line.startsWith("$ cd")) {
    const newDir = new File(line.slice(5), dir);
    dir.children.push(newDir);
    dir = newDir;
  } else if (line.startsWith("$ ls")) {
    continue;
  } else if (line.startsWith("dir")) {
    continue;
  } else {
    const [size, name] = line.split(" ");
    dir.children.push(new File(name, dir, parseInt(size)));
  }
}
const total = root.getSize();
part1(sum(Array.from(File.sizes.values()).filter((s) => s <= 100_000)));

// part2
part2(
  Math.min(
    ...Array.from(File.sizes.values()).filter(
      (size) => size >= 30_000_000 - (70_000_000 - total),
    ),
  ),
);
printTime();
