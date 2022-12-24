import { log, part1, part2, readLines, setDebug } from "./aoc.ts";

const example = true;
setDebug(example);
const lines = readLines(example);
log(lines);

class Blueprint {
  blueprintId: number;
  oreRobotCost: number;
  clayRobotCost: number;
  obsidianRobotOreCost: number;
  obsidianRobotClayCost: number;
  geodeRobotOreCost: number;
  geodeRobotObsidianCost: number;

  constructor(
    blueprintId: number,
    oreRobotCost: number,
    clayRobotCost: number,
    obsidianRobotOreCost: number,
    obsidianRobotClayCost: number,
    geodeRobotOreCost: number,
    geodeRobotObsidianCost: number,
  ) {
    this.blueprintId = blueprintId;
    this.oreRobotCost = oreRobotCost;
    this.clayRobotCost = clayRobotCost;
    this.obsidianRobotOreCost = obsidianRobotOreCost;
    this.obsidianRobotClayCost = obsidianRobotClayCost;
    this.geodeRobotOreCost = geodeRobotOreCost;
    this.geodeRobotObsidianCost = geodeRobotObsidianCost;
  }

  static parse(line: string) {
    const [
      blueprintId,
      oreRobotCost,
      clayRobotCost,
      obsidianRobotOreCost,
      obsidianRobotClayCost,
      geodeRobotOreCost,
      geodeRobotObsidianCost,
    ] = line.match(/\d+/g)!.map(Number);
    return new Blueprint(
      blueprintId,
      oreRobotCost,
      clayRobotCost,
      obsidianRobotOreCost,
      obsidianRobotClayCost,
      geodeRobotOreCost,
      geodeRobotObsidianCost,
    );
  }
}

log(lines.map(Blueprint.parse));

const delay = 24; // minutes

function optimize(b: Blueprint) {
  const state = {
    ore: 1,
    clay: 0,
    obsidian: 0,
  };
}

// part1
part1("TODO");

// part2
part2("TODO");
