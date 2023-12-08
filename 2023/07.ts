import { count, log, part1, part2, readLines } from "./aoc.ts";

globalThis.example = false;
const lines = readLines();
log(lines);

const cardsOrder = [
  "A",
  "K",
  "Q",
  "J",
  "T",
  "9",
  "8",
  "7",
  "6",
  "5",
  "4",
  "3",
  "2",
] as const;
const cardsOrder2 = [
  "A",
  "K",
  "Q",
  "T",
  "9",
  "8",
  "7",
  "6",
  "5",
  "4",
  "3",
  "2",
  "J",
] as const;
type Card = (typeof cardsOrder)[number];
function compareCards(a: Card, b: Card) {
  const order = part === 1 ? cardsOrder : cardsOrder2;
  return order.indexOf(b) - order.indexOf(a);
}

type Hand = [Card, Card, Card, Card, Card];

function isFiveOfAKind(hand: Hand) {
  const c = count(hand);
  return [...c.values()].toSorted().join("") === "5";
}
function isFourOfAKind(hand: Hand) {
  const c = count(hand);
  return [...c.values()].toSorted().join("") === "14";
}
function isThreeOfAKind(hand: Hand) {
  const c = count(hand);
  return [...c.values()].toSorted().join("") === "113";
}
function isFullHouse(hand: Hand) {
  const c = count(hand);
  return [...c.values()].toSorted().join("") === "23";
}
function isTwoPairs(hand: Hand) {
  const c = count(hand);
  return [...c.values()].toSorted().join("") === "122";
}
function isOnePair(hand: Hand) {
  const c = count(hand);
  return [...c.values()].toSorted().join("") === "1112";
}

function compareHands(a: Hand, b: Hand) {
  const A = part === 1 ? a : optimizedHand(a);
  const B = part === 1 ? b : optimizedHand(b);
  if (isFiveOfAKind(A)) {
    if (isFiveOfAKind(B)) {
      return secondCompareHands(a, b);
    }
    return 1;
  } else if (isFourOfAKind(A)) {
    if (isFiveOfAKind(B)) {
      return -1;
    } else if (isFourOfAKind(B)) {
      return secondCompareHands(a, b);
    }
    return 1;
  } else if (isFullHouse(A)) {
    if (isFiveOfAKind(B) || isFourOfAKind(B)) {
      return -1;
    } else if (isFullHouse(B)) {
      return secondCompareHands(a, b);
    }
    return 1;
  } else if (isThreeOfAKind(A)) {
    if (isFiveOfAKind(B) || isFourOfAKind(B) || isFullHouse(B)) {
      return -1;
    } else if (isThreeOfAKind(B)) {
      return secondCompareHands(a, b);
    }
    return 1;
  } else if (isTwoPairs(A)) {
    if (
      isFiveOfAKind(B) ||
      isFourOfAKind(B) ||
      isFullHouse(B) ||
      isThreeOfAKind(B)
    ) {
      return -1;
    } else if (isTwoPairs(B)) {
      return secondCompareHands(a, b);
    }
    return 1;
  } else if (isOnePair(A)) {
    if (
      isFiveOfAKind(B) ||
      isFourOfAKind(B) ||
      isFullHouse(B) ||
      isThreeOfAKind(B) ||
      isTwoPairs(B)
    ) {
      return -1;
    } else if (isOnePair(B)) {
      return secondCompareHands(a, b);
    }
    return 1;
  } else {
    if (
      isFiveOfAKind(B) ||
      isFourOfAKind(B) ||
      isFullHouse(B) ||
      isThreeOfAKind(B) ||
      isTwoPairs(B) ||
      isOnePair(B)
    ) {
      return -1;
    }
    return secondCompareHands(a, b);
  }
}
function secondCompareHands(a: Hand, b: Hand) {
  for (let i = 0; i < a.length; i++) {
    if (a[i] !== b[i]) {
      return compareCards(a[i], b[i]);
    }
  }
  return 0;
}

function optimizedHand(hand: Hand): Hand {
  if (!hand.includes("J")) return hand;
  const c = count(hand);
  const j = c.get("J")!;
  if (j === 5) return "AAAAA".split("") as Hand;
  c.delete("J");
  const newC = [...c.entries()].toSorted((a, b) => b[1] - a[1]);
  log(newC);
  newC[0][1] += j;
  const hand2 = newC.flatMap((a) => a[0].repeat(a[1]).split("")) as Hand;
  return hand2;
}

const handsAndBids = lines
  .map((line) => line.split(/\s+/))
  .map(([h, b]) => [h.split("") as Hand, +b] as const);
log(handsAndBids);

// part1
let part = 1;
part1(
  handsAndBids
    .toSorted((a, b) => compareHands(a[0], b[0]))
    .map((a) => a[1])
    .reduce((a, c, i) => a + c * (i + 1)),
);

// part2
part = 2;
part2(
  handsAndBids
    .toSorted((a, b) => compareHands(a[0], b[0]))
    .map((a) => a[1])
    .reduce((a, c, i) => a + c * (i + 1)),
);
