package main

import (
	"fmt"
	"os"
	"strconv"
	"strings"

	"github.com/guigui64/advent-of-code/goutils/aoc"
)

func reverse(list []int) []int {
	rlist := make([]int, len(list))
	for i, l := range list {
		rlist[len(list)-1-i] = l
	}
	return rlist
}

func compute(lengths []int, max int) int {
	current, skipSize := 0, 0
	list := make([]int, max+1)
	for i := range list {
		list[i] = i
	}
	for _, l := range lengths {
		// select sublist from current and length
		sublist := make([]int, l)
		for i := range sublist {
			sublist[i] = list[(current+i)%(max+1)]
		}
		// reverse sublist
		sublist = reverse(sublist)
		// inject reversed sublist into the list
		for i := range sublist {
			list[(current+i)%(max+1)] = sublist[i]
		}
		// move cursor and increase skipSize
		current += l + skipSize
		skipSize++
	}
	return list[0] * list[1]
}

func main() {
	fileName := "../10.in"
	max := 255
	if len(os.Args) > 2 { // first is program name, then fileName, then max
		fileName = os.Args[1]
		max, _ = strconv.Atoi(os.Args[2])
	}
	f := aoc.ReadAndCheckFile(fileName)
	slengths := strings.Split(strings.Split(string(f), "\n")[0], ",")
	lengths := make([]int, len(slengths))
	for i, s := range slengths {
		lengths[i], _ = strconv.Atoi(s)
	}
	fmt.Println(compute(lengths, max))
}
