package main

import "fmt"
import "math"

func part1(target int) int {
	// fmt.Println(target)
	// Find the length of the square we are on
	// fmt.Println(math.Sqrt(float64(target)))
	// fmt.Println(math.Ceil(math.Sqrt(float64(target))))
	length := int(math.Ceil(math.Sqrt(float64(target))))
	if length%2 == 0 {
		length += 1
	}
	// fmt.Println("length =", length)
	// Distance to center
	dist := (length - 1) / 2
	// fmt.Println("dist =", dist)
	// Center cells of each side
	centers := make([]int, 4)
	for i := range centers {
		centers[i] = length*length - (length-1)*i - dist
		// fmt.Println("center", i, "=", centers[i])
	}
	// Find min of each diff
	var mindiff int
	for i, v := range centers {
		diff := target - v
		if diff < 0 {
			diff = -diff
		}
		if i == 0 {
			mindiff = diff
		} else if diff < mindiff {
			mindiff = diff
		}
	}
	// fmt.Println("mindiff =", mindiff)
	// Result is distance to center + min diff
	return dist + mindiff
}

func main() {
	fmt.Println(part1(12), part1(23), part1(1024))
	fmt.Println(part1(265149))
}
