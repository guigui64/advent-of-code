package main

import (
	"fmt"
	"os"
	"strconv"

	"github.com/guigui64/advent-of-code/goutils/aoc"
)

func main() {
	fileName := "08.in"
	if len(os.Args) > 1 { // first is prog name
		fileName = os.Args[1]
	}
	input := aoc.ParseInput(fileName)
	regs := make(map[string]int) // zero value is already 0 :)
	highest := 0
	for _, fields := range input {
		condition := fields[4:]
		reg := regs[condition[0]]
		value, _ := strconv.Atoi(condition[2])
		doOp := false
		switch condition[1] {
		case ">":
			doOp = reg > value
		case "<":
			doOp = reg < value
		case ">=":
			doOp = reg >= value
		case "<=":
			doOp = reg <= value
		case "==":
			doOp = reg == value
		case "!=":
			doOp = reg != value
		default:
			fmt.Println("ERROR : Impossible operator :", condition[1])
		}
		if doOp {
			value, _ := strconv.Atoi(fields[2])
			if fields[1] == "inc" {
				regs[fields[0]] += value
			} else {
				regs[fields[0]] -= value
			}
			if regs[fields[0]] > highest {
				highest = regs[fields[0]]
			}
		}
	}
	fmt.Println(regs)
	max := 0
	first := true
	for _, v := range regs {
		if first {
			max = v
			first = false
		} else {
			if v > max {
				max = v
			}
		}
	}
	fmt.Println(max)
	fmt.Println(highest)
}
