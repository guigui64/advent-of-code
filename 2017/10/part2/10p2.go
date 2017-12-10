package main

import (
	"fmt"

	"github.com/guigui64/advent-of-code/goutils/aoc"
)

func reverse(list []byte) []byte {
	rlist := make([]byte, len(list))
	for i, l := range list {
		rlist[len(list)-1-i] = l
	}
	return rlist
}

func compute(lengths []byte, max int) []byte {
	current, skipSize := 0, 0
	list := make([]byte, max+1)
	for i := range list {
		list[i] = byte(i)
	}
	for n := 0; n < 64; n++ {
		for _, l := range lengths {
			// select sublist from current and length
			sublist := make([]byte, l)
			for i := range sublist {
				sublist[i] = list[(current+i)%(max+1)]
			}
			// reverse sublist
			sublist = reverse(sublist)
			// inject reversed sublist into the list
			for i := range sublist {
				list[(current+i)%(max+1)] = sublist[i]
			}
			// move cursor and increase skipSize
			current += int(l) + skipSize
			skipSize++
		}
	}
	return list
}

func main() {
	fileName := "../10.in"
	max := 255
	f := aoc.ReadAndCheckFile(fileName)
	lengths := f[:len(f)-1] // ignore last character which is a "\n"
	lengths = append(lengths, 17, 31, 73, 47, 23)
	fmt.Println(lengths)
	list := compute(lengths, max)
	fmt.Println(list)
	denseHash := make([]byte, 16)
	for i, j := 0, 0; i < len(list); i, j = i+16, j+1 {
		for ii := i; ii < i+16; ii++ {
			if ii == i {
				denseHash[j] = list[ii]
			} else {
				denseHash[j] ^= list[ii]
			}
		}
	}
	for _, v := range denseHash {
		fmt.Printf("%02x", v)
	}
	fmt.Println()
}
