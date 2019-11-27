package main

import (
	"fmt"
	"io/ioutil"
	"strconv"

	"github.com/guigui64/gcgo/utils"
)

func sum(s []int) int {
	sum := 0
	var next int
	for i := 0; i < len(s); i++ {
		next = (i + 1) % len(s)
		if s[i] == s[next] {
			sum += s[i]
		}
	}
	return sum
}

func sum2(s []int) int {
	sum := 0
	var next int
	for i := 0; i < len(s); i++ {
		next = (i + len(s)/2) % len(s)
		if s[i] == s[next] {
			sum += s[i]
		}
	}
	return sum
}

func convert(ascii []byte) []int {
	var err error
	res := make([]int, len(ascii))
	for i := 0; i < len(ascii); i++ {
		res[i], err = strconv.Atoi(string(ascii[i]))
		utils.Check(err)
	}
	return res
}

func main() {

	dat, err := ioutil.ReadFile("01.in")
	utils.Check(err)
	fmt.Print(string(dat))

	fmt.Println("Part 1")
	fmt.Printf("1122 = %d\n", sum([]int{1, 1, 2, 2}))
	fmt.Printf("1111 = %d\n", sum([]int{1, 1, 1, 1}))
	fmt.Printf("1234 = %d\n", sum([]int{1, 2, 3, 4}))
	fmt.Printf("91212129 = %d\n", sum([]int{9, 1, 2, 1, 2, 1, 2, 9}))
	fmt.Printf("puzzle input = %d\n", sum(convert(dat[:len(dat)-1])))

	fmt.Println("\nPart 2")
	fmt.Printf("1212 = %d\n", sum2([]int{1, 2, 1, 2}))
	fmt.Printf("1221 = %d\n", sum2([]int{1, 2, 2, 1}))
	fmt.Printf("123425 = %d\n", sum2([]int{1, 2, 3, 4, 2, 5}))
	fmt.Printf("123123 = %d\n", sum2([]int{1, 2, 3, 1, 2, 3}))
	fmt.Printf("12131415 = %d\n", sum2([]int{1, 2, 1, 3, 1, 4, 1, 5}))
	fmt.Printf("puzzle input = %d\n", sum2(convert(dat[:len(dat)-1])))

}
