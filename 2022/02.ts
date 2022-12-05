import { part1, part2, printTime, readLines, startTimer } from "./aoc.ts";

// A/X == Rock
// B/Y == Paper
// C/Z == Scissors
//
// ABC == Opponent | XYZ == Me
//
// Part 2:
// X == you lose
// Y == draw
// Z == you win

const winRounds = ["A Y", "B Z", "C X"];
const drawRounds = ["A X", "B Y", "C Z"];
const lossRounds = ["A Z", "B X", "C Y"];

function roundScore(round: string) {
  if (winRounds.includes(round)) {
    return 6; // win
  } else if (drawRounds.includes(round)) {
    return 3; // draw
  } else {
    return 0; // loss
  }
}

function moveScore(move: string) {
  return move.charCodeAt(0) - "W".charCodeAt(0);
}

// translate part2 round to part1
// ex: A Y => A draw => A X
function translate(round: string) {
  const [opponent, order] = round.split(" ");
  if (order === "Z") {
    // win
    return winRounds.find((r) => r.startsWith(opponent))!;
  } else if (order === "Y") {
    // draw
    return drawRounds.find((r) => r.startsWith(opponent))!;
  } else {
    // loss
    return lossRounds.find((r) => r.startsWith(opponent))!;
  }
}

startTimer();
// first compute score for each combo
const scores: { [index: string]: number } = {};
for (const opponent of "ABC") {
  for (const me of "XYZ") {
    const round = `${opponent} ${me}`;
    scores[round] = moveScore(me) + roundScore(round);
  }
}

// then apply on input
const rounds = readLines(false);
part1(rounds.reduce((acc, round) => acc + scores[round], 0));
part2(rounds.map(translate).reduce((acc, round) => acc + scores[round], 0));
printTime();
