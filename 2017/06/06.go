package main

import (
	"fmt"
	"strconv"

	"github.com/guigui64/advent-of-code/goutils/aoc"
	"github.com/guigui64/gcgo/utils"
)

type States [][]int

func (s States) hasState(v []int) (bool, int) {
	for i, sv := range s {
		if equals(sv, v) {
			return true, i
		}
	}
	return false, 0
}

func equals(a, b []int) bool {
	if len(a) != len(b) {
		return false
	}
	for i, v := range a {
		if v != b[i] {
			return false
		}
	}
	return true
}

func compute(blocks []int) (redist, loop int) {
	var previousStates States
	for {
		if has, iprev := previousStates.hasState(blocks); has {
			loop = redist - iprev
			break
		}
		blocksCopy := make([]int, len(blocks))
		copy(blocksCopy, blocks)
		previousStates = append(previousStates, blocksCopy)
		imax, vmax := utils.MaxIntSlice(blocks)
		blocks[imax] = 0
		for i := 0; i < vmax; i++ {
			blocks[(imax+1+i)%len(blocks)] += 1
		}
		redist++
	}
	return
}

func main() {
	example := []int{0, 2, 7, 0}
	fmt.Println(compute(example))
	fields := aoc.ParseInput("06.in")[0]
	input := make([]int, len(fields))
	for i, s := range fields {
		a, _ := strconv.Atoi(s)
		input[i] = a
	}
	fmt.Println(compute(input))
}
