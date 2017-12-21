package main

import (
	"fmt"
	"log"
	"reflect"
	"strings"

	"github.com/guigui64/advent-of-code/goutils/aoc"
)

func display(image [][]byte) {
	for _, line := range image {
		fmt.Println(string(line))
	}
}

func flip(image [][]byte) [][]byte {
	cop := make([][]byte, len(image))
	for i := range cop {
		cop[i] = make([]byte, len(image[i]))
		copy(cop[i], image[i])
	}
	for _, line := range cop {
		for left, right := 0, len(line)-1; left < right; left, right = left+1, right-1 {
			line[left], line[right] = line[right], line[left]
		}
	}
	return cop
}

func rotate(image [][]byte) [][]byte {
	height, width := len(image), len(image[0])
	rot := make([][]byte, width)
	for i := 0; i < width; i++ {
		rot[i] = make([]byte, height)
		for j := 0; j < height; j++ {
			rot[i][j] = image[height-j-1][i]
		}
	}
	return rot
}

type Rule struct {
	Key, Value [][]byte
}

func compare(image, ref [][]byte) bool {
	return reflect.DeepEqual(image, ref)
}

func compareEvery(image, ref [][]byte) bool {
	return compare(image, ref) || compare(flip(image), ref) ||
		compare(rotate(image), ref) || compare(flip(rotate(image)), ref) ||
		compare(rotate(rotate(image)), ref) || compare(flip(rotate(rotate(image))), ref) ||
		compare(rotate(rotate(rotate(image))), ref) || compare(flip(rotate(rotate(rotate(image)))), ref)
}

func findRule(image [][]byte, rules []Rule) (int, bool) {
	for i, rule := range rules {
		if compareEvery(image, rule.Key) {
			return i, true
		}
	}
	return 0, false
}

func count(image [][]byte) int {
	total := 0
	for i := range image {
		for j := range image[i] {
			if image[i][j] == '#' {
				total++
			}
		}
	}
	return total
}

func main() {
	image := [][]byte{
		[]byte(".#."),
		[]byte("..#"),
		[]byte("###"),
	}
	input := aoc.ReadAndCheckFile("21.in")
	var rules []Rule
	for _, line := range strings.Split(string(input), "\n") {
		if strings.TrimSpace(line) == "" {
			continue
		}
		kv := strings.Split(line, " => ")
		var rule Rule
		for _, l := range strings.Split(kv[0], "/") {
			rule.Key = append(rule.Key, []byte(l))
		}
		for _, l := range strings.Split(kv[1], "/") {
			rule.Value = append(rule.Value, []byte(l))
		}
		rules = append(rules, rule)
	}
	iterations := 18
	it := 0
	for ; it < iterations; it++ {
		fmt.Println(it)
		if len(image)%2 == 0 {
			newSize := len(image) / 2 * 3
			newImage := make([][]byte, newSize)
			for i := 0; i < len(image)/2; i++ {
				for j := 0; j < len(image[i])/2; j++ {
					part := make([][]byte, 2)
					part[0] = image[2*i][2*j : 2*j+2]
					part[1] = image[2*i+1][2*j : 2*j+2]
					if ridx, ok := findRule(part, rules); ok {
						newImage[3*i] = append(newImage[3*i], rules[ridx].Value[0]...)
						newImage[3*i+1] = append(newImage[3*i+1], rules[ridx].Value[1]...)
						newImage[3*i+2] = append(newImage[3*i+2], rules[ridx].Value[2]...)
					} else {
						display(part)
						log.Fatal("Matched no rule")
					}
				}
			}
			image = newImage
		} else {
			newSize := len(image) / 3 * 4
			newImage := make([][]byte, newSize)
			for i := 0; i < len(image)/3; i++ {
				for j := 0; j < len(image[i])/3; j++ {
					part := make([][]byte, 3)
					part[0] = image[3*i][3*j : 3*j+3]
					part[1] = image[3*i+1][3*j : 3*j+3]
					part[2] = image[3*i+2][3*j : 3*j+3]
					if ridx, ok := findRule(part, rules); ok {
						newImage[4*i] = append(newImage[4*i], rules[ridx].Value[0]...)
						newImage[4*i+1] = append(newImage[4*i+1], rules[ridx].Value[1]...)
						newImage[4*i+2] = append(newImage[4*i+2], rules[ridx].Value[2]...)
						newImage[4*i+3] = append(newImage[4*i+3], rules[ridx].Value[3]...)
					} else {
						display(part)
						log.Fatal("Matched no rule")
					}
				}
			}
			image = newImage
		}
		if it == 4 {
			display(image)
			fmt.Println("Part 1 :", count(image))
		}
	}
	fmt.Println("Part 2 :", count(image))
}
