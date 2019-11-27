package main

import (
	"fmt"
	"strconv"
	"strings"

	"github.com/guigui64/advent-of-code/goutils/aoc"
)

func spin(s, move string) string {
	n, _ := strconv.Atoi(move)
	return s[len(s)-n:] + s[:len(s)-n]
}

func exchange(s, move string) string {
	a, _ := strconv.Atoi(strings.Split(move, "/")[0])
	b, _ := strconv.Atoi(strings.Split(move, "/")[1])
	if a > b {
		a, b = b, a
	}
	return s[:a] + string(s[b]) + s[a+1:b] + string(s[a]) + s[b+1:]
}

func partner(s, move string) string {
	a := strings.IndexByte(s, move[0])
	b := strings.IndexByte(s, move[2])
	if a > b {
		a, b = b, a
	}
	return s[:a] + string(s[b]) + s[a+1:b] + string(s[a]) + s[b+1:]
}

type BoolInt struct {
	B bool
	I int
}

func main() {
	f := aoc.ReadAndCheckFile("16.in")
	programs := "abcdefghijklmnop"
	moves := strings.Split(string(f[:len(f)-1]), ",")
	for _, move := range moves {
		switch move[0] {
		case 's':
			programs = spin(programs, move[1:])
		case 'x':
			programs = exchange(programs, move[1:])
		case 'p':
			programs = partner(programs, move[1:])
		default:
			panic("Unknown move " + move)
		}
	}
	fmt.Println(programs)
	orders := make(map[string]BoolInt)
	orders["abcdefghijklmnop"] = BoolInt{true, 0}
	for i := 1; i < 1e9; i++ {
		if orders[programs].B {
			// find order with index 1e9 % i
			for s, bi := range orders {
				if bi.I == 1e9%i {
					fmt.Println(s)
					return
				}
			}
		}
		orders[programs] = BoolInt{true, i}
		for _, move := range moves {
			switch move[0] {
			case 's':
				programs = spin(programs, move[1:])
			case 'x':
				programs = exchange(programs, move[1:])
			case 'p':
				programs = partner(programs, move[1:])
			default:
				panic("Unknown move " + move)
			}
		}
	}
}
