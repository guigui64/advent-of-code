package main

import (
	"fmt"
	"io/ioutil"
	"strconv"
	"strings"
)

func minmax(s []int) (min, max int) {
	min = s[0]
	max = s[0]
	for _, v := range s {
		if v > max {
			max = v
		}
		if v < min {
			min = v
		}
	}
	return
}

func checksum(sheet [][]int) int {
	var sum int
	for _, ssheet := range sheet {
		min, max := minmax(ssheet)
		sum += max - min
	}
	return sum
}

func buildSheet(input string) (sheet [][]int) {
	text, _ := ioutil.ReadFile(input)
	for _, sline := range strings.Split(string(text), "\n") {
		if len(strings.TrimSpace(sline)) == 0 {
			continue
		}
		var line []int
		for _, field := range strings.Fields(sline) {
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
