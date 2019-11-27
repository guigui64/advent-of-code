package main

import (
	"fmt"
	"strings"

	"github.com/guigui64/advent-of-code/goutils/aoc"
)

func main() {
	f := aoc.ReadAndCheckFile("19.in")
	matrix := strings.Split(string(f), "\n")
	matrix = matrix[:len(matrix)-1] // last line is empty
	dir := "down"
	r, c := 0, strings.IndexByte(matrix[0], '|')
	letters := ""
	steps := 0
	for {
		switch dir {
		case "down":
			r++
		case "up":
			r--
		case "right":
			c++
		case "left":
			c--
		default:
			panic("dir unknown :" + dir)
		}
		steps++
		if 'A' <= matrix[r][c] && matrix[r][c] <= 'Z' {
			letters += string(matrix[r][c])
		} else if '+' == matrix[r][c] {
			if dir == "down" || dir == "up" {
				if matrix[r][c-1] != ' ' {
					dir = "left"
				} else if matrix[r][c+1] != ' ' {
					dir = "right"
				} else {
					panic("On + and surrounded by spaces")
				}
			} else {
				if matrix[r-1][c] != ' ' {
					dir = "up"
				} else if matrix[r+1][c] != ' ' {
					dir = "down"
				} else {
					panic("On + and surrounded by spaces")
				}
			}
		} else if ' ' == matrix[r][c] {
			break
		}
	}
	fmt.Println(letters, steps)
}
