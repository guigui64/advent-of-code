package main

import (
	"fmt"
	"strings"

	"github.com/guigui64/advent-of-code/goutils/aoc"
)

func main() {
	fields := aoc.ParseInput("19.in")
	transitions := fields[:len(fields)-2]
	// empty line
	molecule := fields[len(fields)-1][0]
	replacements := make(map[string]int)
	elements := make(map[string]bool) // acts like a set
	for _, tr := range transitions {
		key := tr[0]
		// tr[1] is '=>'
		value := tr[2]
		if key != "e" {
			elements[key] = true
		}
		last := 0
		for {
			i := strings.Index(molecule[last:], key)
			if i == -1 {
				break
			}
			i += last
			last = i + 1
			substituion := molecule[0:i] + value + molecule[i+len(key):]
			replacements[substituion]++
		}
	}
	fmt.Println(len(replacements))
	nbElements := 0
	// Rn and Ar are parentheses
	nbCommas := 0 // Y is a comma
	for _, b := range molecule {
		if 'A' <= b && b <= 'Z' {
			nbElements++ // count caps
			if b == 'Y' {
				nbCommas++
			}
		}
	}
	nbParentheses := strings.Count(molecule, "Rn") + strings.Count(molecule, "Ar")
	// magic formula (thanks to /u/askalski on /r/adventofcode !)
	fmt.Println(nbElements - nbParentheses - 2*nbCommas - 1)
}
