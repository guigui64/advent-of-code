package main

import (
	"fmt"

	"github.com/guigui64/gcgo/utils"
)

func main() {
	steps := 366 // input
	// steps := 3 // example

	spin := []int{0}
	pos := 0

	for i := 1; i < 2018; i++ {
		pos = (pos+steps)%len(spin) + 1
		spin = utils.InsertInt(spin, pos, i)
		// fmt.Println(spin, pos)
	}

	fmt.Println(spin[pos+1])

	pos = 0
	length := 1
	valueAfter0 := -1
	for i := 1; i < 50000000; i++ {
		pos = (pos+steps)%length + 1
		if pos == 1 {
			valueAfter0 = i
		}
		length++
	}

	fmt.Println(valueAfter0)
}
