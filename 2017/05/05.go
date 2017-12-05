package main

import (
	"fmt"
	"io/ioutil"
	"strconv"
	"strings"
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
	f, _ := ioutil.ReadFile("05.in")
	lines := strings.Split(string(f), "\n")
	var jumps []int
	for _, line := range lines {
		if strings.TrimSpace(line) != "" {
			i, ok := strconv.Atoi(line)
			if ok != nil {
				panic(ok)
			}
			jumps = append(jumps, i)
		}
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
