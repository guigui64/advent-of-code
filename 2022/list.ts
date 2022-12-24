import { range } from "./aoc.ts";

export default class DLLEntry<T> {
  value: T;
  next?: DLLEntry<T>;
  prev?: DLLEntry<T>;

  constructor(value: T) {
    this.value = value;
  }

  toString() {
    return `${this.prev?.value} -> [${this.value}] -> ${this.next?.value}`;
  }

  move(shift: number, size: number) {
    if (shift === 0) return;
    const move = Math.abs(shift) % (size - 1);
    // remove this from neighbors
    this.prev!.next = this.next;
    this.next!.prev = this.prev;
    // find new position
    for (let i = 0; i < move; i++) {
      if (shift > 0) {
        this.next = this.next!.next;
        this.prev = this.prev!.next;
      } else {
        this.next = this.prev;
        this.prev = this.prev!.prev;
      }
    }
    // insert this
    this.prev!.next = this;
    this.next!.prev = this;
  }

  get(delta: number, size: number) {
    // deno-lint-ignore no-this-alias
    let n: DLLEntry<T> = this;
    range(delta % size).forEach(() => n = n.next!);
    return n.value;
  }
}

export function makeDLL<T>(list: T[]) {
  const entries = list.map((v) => new DLLEntry(v));
  for (let i = 0; i < entries.length - 1; i++) {
    entries[i].next = entries[i + 1];
    entries[i + 1].prev = entries[i];
  }
  entries[entries.length - 1].next = entries[0];
  entries[0].prev = entries[entries.length - 1];
  return entries;
}
