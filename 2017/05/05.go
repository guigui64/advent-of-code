package main

import (
	"fmt"
	"strconv"

	"github.com/guigui64/advent-of-code/goutils/aoc"
	"github.com/guigui64/gcgo/utils"
)

func compute(jumps []int, part2 bool) int {
	steps := 1
	idx := 0
	for {
		idx2 := idx + jumps[idx]
		if idx2 >= len(jumps) {
			break
		}
		if part2 && jumps[idx] >= 3 {
			jumps[idx] -= 1
		} else {
			jumps[idx] += 1
		}
		idx = idx2
		steps += 1
	}
	return steps
}

func main() {
	matrix := aoc.ParseInput("05.in")
	var jumps []int
	for _, fields := range matrix {
		i, e := strconv.Atoi(fields[0])
		utils.Check(e)
		jumps = append(jumps, i)
	}
	jumps2 := make([]int, len(jumps))
	fmt.Println("\nPART 1")
	copy(jumps2, jumps)
	fmt.Println("Example :", compute([]int{0, 3, 0, 1, -3}, false))
	fmt.Println("Input :", compute(jumps2, false))
	fmt.Println("\nPART 2")
	copy(jumps2, jumps)
	fmt.Println("Example :", compute([]int{0, 3, 0, 1, -3}, true))
	fmt.Println("Input :", compute(jumps2, true))
}
