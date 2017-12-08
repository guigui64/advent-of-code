package main

import (
	"fmt"
	"strconv"

	"github.com/guigui64/advent-of-code/goutils/aoc"
	"github.com/guigui64/gcgo/utils"
)

func checksum(sheet [][]int) int {
	var sum int
	for _, ssheet := range sheet {
		imin, imax := utils.MinMax(ssheet)
		sum += ssheet[imax] - ssheet[imin]
	}
	return sum
}

func buildSheet(input string) (sheet [][]int) {
	matrix := aoc.ParseInput(input)
	for _, fields := range matrix {
		var line []int
		for _, field := range fields {
			i, _ := strconv.Atoi(field)
			line = append(line, i)
		}
		sheet = append(sheet, line)
	}
	return
}

func divide(s []int) int {
	for i, a := range s {
		for j, b := range s {
			if i != j && a%b == 0 {
				return a / b
			}
		}
	}
	fmt.Println("Couldn't find division for line ", s)
	return 0
}

func checksum2(sheet [][]int) int {
	sum := 0
	for i := range sheet {
		sum += divide(sheet[i])
	}
	return sum
}

func main() {
	fmt.Println("Example from problem")
	sheet := [][]int{
		{5, 1, 9, 5},
		{7, 5, 3},
		{2, 4, 6, 8},
	}
	fmt.Println(checksum(sheet))

	fmt.Println("\nPart 1")
	sheet = buildSheet("02.in")
	fmt.Println(checksum(sheet))

	fmt.Println("\n2nd example from problem")
	sheet2 := [][]int{
		{5, 9, 2, 8},
		{9, 4, 7, 3},
		{3, 8, 6, 5},
	}
	fmt.Println(checksum2(sheet2))

	fmt.Println("\nPart 2")
	fmt.Println(checksum2(sheet))

}
