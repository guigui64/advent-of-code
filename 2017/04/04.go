package main

import (
	"fmt"
	"io/ioutil"
	"sort"
	"strings"
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
	f, _ := ioutil.ReadFile("04.in")
	lines := strings.Split(string(f), "\n")
	sum := 0
	for _, line := range lines {
		if strings.TrimSpace(line) == "" {
			continue
		}
		words := strings.Fields(line)
		valid := uniq(words)
		fmt.Println(words, "->", valid)
		if valid {
			sum += 1
		}
	}
	fmt.Println("Part 1 :", sum)

	sum = 0
	for _, line := range lines {
		if strings.TrimSpace(line) == "" {
			continue
		}
		words := strings.Fields(line)
		valid := uniq2(words)
		fmt.Println(words, "->", valid)
		if valid {
			sum += 1
		}
	}
	fmt.Println("Part 2 :", sum)
}
