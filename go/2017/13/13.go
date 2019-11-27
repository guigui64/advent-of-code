package main

import (
	"fmt"
	"os"
	"strconv"
	"strings"

	"github.com/guigui64/advent-of-code/goutils/aoc"
)

func scannerAt0AtDate(t, lrange int) bool {
	return t%(2*(lrange-1)) == 0
}

func main() {
	fileName := "13.in"
	if len(os.Args) > 1 {
		fileName = os.Args[1]
	}
	firewall := make(map[int]int)
	maxDepth := 0
	for _, line := range aoc.ReadLines(fileName) {
		depth, _ := strconv.Atoi(strings.Split(line, ": ")[0])
		lrange, _ := strconv.Atoi(strings.Split(line, ": ")[1])
		firewall[depth] = lrange
		if depth > maxDepth {
			maxDepth = depth
		}
	}
	fmt.Println(firewall)
	severity := 0
	for pos := 0; pos < maxDepth+1; pos++ {
		if firewall[pos] != 0 && scannerAt0AtDate(pos, firewall[pos]) {
			severity += pos * firewall[pos]
		}
	}
	fmt.Println(severity)
	// look for min delay
	delay := 1 // 0 is already known to be not enough
	c := make(chan int)
	nbCpu := 1 // seems at least as fast that with 4 cpus...
	for i := 0; i < nbCpu; i++ {
		go func(d int, c chan int, firewall map[int]int) {
			for {
				fail := false
				for pos := 0; pos < maxDepth+1; pos++ {
					if firewall[pos] != 0 && scannerAt0AtDate(d+pos, firewall[pos]) {
						fail = true
						break
					}
				}
				if !fail {
					break
				}
				d += nbCpu
			}
			c <- d

		}(delay+i, c, firewall)
	}
	fmt.Println(<-c)
}
