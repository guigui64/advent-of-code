package main

import "fmt"

func main() {
	var factorA, factorB, divider int64 = 16807, 48271, 2147483647
	// var startA, startB int64 = 65, 8921 // example
	var startA, startB int64 = 512, 191 // input
	total := 0
	previousA, previousB := startA, startB
	for i := 0; i < 40e6; i++ { // 40 million times
		currentA, currentB := previousA*factorA, previousB*factorB
		currentA, currentB = currentA%divider, currentB%divider
		if currentA&0xFFFF == currentB&0xFFFF {
			total++
		}
		previousA, previousB = currentA, currentB
	}
	fmt.Println(total)
	total = 0
	previousA, previousB = startA, startB
	var genA, genB []int64
	for len(genA) < 5e6 || len(genB) < 5e6 {
		currentA, currentB := previousA*factorA, previousB*factorB
		currentA, currentB = currentA%divider, currentB%divider
		if currentA&3 == 0 {
			genA = append(genA, currentA)
		}
		if currentB&7 == 0 {
			genB = append(genB, currentB)
		}
		previousA, previousB = currentA, currentB
	}
	for i := range genA {
		if i == len(genB) {
			break
		}
		if genA[i]&0xFFFF == genB[i]&0xFFFF {
			total++
		}
	}
	fmt.Println(total)
}
