package main

import (
	"fmt"
	"strings"

	"github.com/guigui64/advent-of-code/goutils/aoc"
)

func cleanUp(stream string) string {
	// remove all escaped characters
	for {
		if exclIdx := strings.Index(stream, "!"); exclIdx != -1 {
			stream = stream[:exclIdx] + stream[exclIdx+2:]
		} else {
			break
		}
	}
	// fmt.Println(stream)
	// remove garbage
	count := 0
	for {
		openingIdx := strings.Index(stream, "<")
		if openingIdx == -1 {
			break
		}
		closingIdx := strings.Index(stream, ">")
		if closingIdx == -1 {
			fmt.Println("< found but > not found ! should not happen !")
		}
		stream = stream[:openingIdx] + stream[closingIdx+1:]
		count += closingIdx - openingIdx - 1
	}
	fmt.Println("removed", count, "characters of garbage")
	// fmt.Println(stream)
	return stream
}

func score(s string) int {
	sco := 0
	current := 0
	for _, c := range s {
		if c == '{' {
			current += 1
		} else if c == '}' {
			sco += current
			current -= 1
		}
	}
	return sco
}

func compute(stream string) int {
	fmt.Println("Computing for :", stream)
	stream = cleanUp(stream)
	return score(stream)
}

func main() {
	f := aoc.ReadAndCheckFile("09.in")
	stream := strings.Split(string(f), "\n")[0]
	fmt.Println(compute("{}"))
	fmt.Println(compute("{{{}}}"))
	fmt.Println(compute("{{},{}}"))
	fmt.Println(compute("{{{},{},{{}}}}"))
	fmt.Println(compute("{<a>,<a>,<a>,<a>}"))
	fmt.Println(compute("{{<ab>},{<ab>},{<ab>},{<ab>}}"))
	fmt.Println(compute("{{<!!>},{<!!>},{<!!>},{<!!>}}"))
	fmt.Println(compute("{{<a!>},{<a!>},{<a!>},{<ab>}}"))
	fmt.Println(compute(stream))
}
