package main

import (
	"fmt"
	"sort"

	"github.com/guigui64/advent-of-code/goutils/aoc"
)

func uniq(words []string) bool {
	for i := range words {
		for j := range words {
			if i != j && words[i] == words[j] {
				return false
			}
		}
	}
	return true
}

func StringToRuneSlice(s string) []rune {
	var r []rune
	for _, runeValue := range s {
		r = append(r, runeValue)
	}
	return r
}

func anagram(w1, w2 string) bool {
	r1 := StringToRuneSlice(w1)
	r2 := StringToRuneSlice(w2)

	sort.Slice(r1, func(i, j int) bool { return r1[i] < r1[j] })
	sort.Slice(r2, func(i, j int) bool { return r2[i] < r2[j] })

	return string(r1) == string(r2)

}

func uniq2(words []string) bool {
	for i := range words {
		for j := range words {
			if i != j && anagram(words[i], words[j]) {
				return false
			}
		}
	}
	return true
}

func main() {
	input := aoc.ParseInput("04.in")
	sum := 0
	for _, words := range input {
		valid := uniq(words)
		fmt.Println(words, "->", valid)
		if valid {
			sum += 1
		}
	}
	fmt.Println("Part 1 :", sum)

	sum = 0
	for _, words := range input {
		valid := uniq2(words)
		fmt.Println(words, "->", valid)
		if valid {
			sum += 1
		}
	}
	fmt.Println("Part 2 :", sum)
}
