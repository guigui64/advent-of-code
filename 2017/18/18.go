package main

import (
	"fmt"
	"strconv"
	"strings"
	"time"

	"github.com/guigui64/advent-of-code/goutils/aoc"
)

func main() {
	f := aoc.ReadAndCheckFile("18.in")
	var instr []string
	for _, line := range strings.Split(string(f), "\n") {
		if line == "" {
			continue
		}
		instr = append(instr, line)
	}
	fmt.Println("Part 1")
	fmt.Println(part1(instr))
	fmt.Println()
	fmt.Println("Part 2")
	part2(instr)
}

func part2(instr []string) {
	c0 := make(chan int, 100)
	c1 := make(chan int, 100)
	prog := func(instr []string, id int, send, rec chan int) {
		registers := make(map[string]int)
		registers["p"] = id
		i := 0
		count := 0
		for i >= 0 && i < len(instr) {
			fields := strings.Fields(instr[i])
			switch fields[0] {
			case "snd":
				select {
				case send <- valueOf(registers, fields[1]):
					fmt.Println(id, ": send", valueOf(registers, fields[1]))
					count++
					if id == 1 {
						fmt.Println(count)
					}
				case <-time.After(time.Second):
					panic("timeout at send")
					return
				}
			case "set":
				registers[fields[1]] = valueOf(registers, fields[2])
			case "add":
				registers[fields[1]] += valueOf(registers, fields[2])
			case "mul":
				registers[fields[1]] *= valueOf(registers, fields[2])
			case "mod":
				registers[fields[1]] %= valueOf(registers, fields[2])
			case "rcv":
				select {
				case registers[fields[1]] = <-rec:
					fmt.Println(id, ": received", registers[fields[1]])
				case <-time.After(time.Second):
					panic("timeout at receive")
					return
				}
			case "jgz":
				if valueOf(registers, fields[1]) != 0 {
					i += valueOf(registers, fields[2])
					continue
				}
			}
			i++
		}
	}
	go prog(instr, 0, c0, c1)
	prog(instr, 1, c1, c0)
}

func part1(instr []string) int {
	registers := make(map[string]int)
	lastPlayed := -1
	i := 0
InstrLoop:
	for i >= 0 && i < len(instr) {
		fields := strings.Fields(instr[i])
		switch fields[0] {
		case "snd":
			lastPlayed = valueOf(registers, fields[1])
		case "set":
			registers[fields[1]] = valueOf(registers, fields[2])
		case "add":
			registers[fields[1]] += valueOf(registers, fields[2])
		case "mul":
			registers[fields[1]] *= valueOf(registers, fields[2])
		case "mod":
			registers[fields[1]] %= valueOf(registers, fields[2])
		case "rcv":
			if valueOf(registers, fields[1]) != 0 {
				return lastPlayed
			}
		case "jgz":
			if valueOf(registers, fields[1]) != 0 {
				i += valueOf(registers, fields[2])
				continue InstrLoop
			}
		}
		i++
	}
	return lastPlayed
}

func valueOf(registers map[string]int, key string) int {
	if a, err := strconv.Atoi(key); err == nil {
		return a
	} else {
		return registers[key]
	}
}
