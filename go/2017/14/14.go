package main

import (
	"fmt"
	"strconv"
)

func reverse(list []byte) []byte {
	rlist := make([]byte, len(list))
	for i, l := range list {
		rlist[len(list)-1-i] = l
	}
	return rlist
}

func compute(lengths []byte, max int) []byte {
	lengths = append(lengths, 17, 31, 73, 47, 23)
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

func knotHash(b []byte) string {
	list := compute(b, 255)
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
	hash := ""
	for _, v := range denseHash {
		hash += fmt.Sprintf("%02x", v)
	}
	return hash
}

func hexToBinString(in string) string {
	out := ""
	for _, c := range in {
		i, _ := strconv.ParseInt(string(c), 16, 8)
		out += fmt.Sprintf("%04b", i)
	}
	return out
}

func search(matrix [][]bool, i, j int, visited [][]bool) {
	if visited[i][j] {
		return
	}
	if !matrix[i][j] {
		return
	}
	visited[i][j] = true
	if i > 0 {
		search(matrix, i-1, j, visited)
	}
	if j > 0 {
		search(matrix, i, j-1, visited)
	}
	if i < 127 {
		search(matrix, i+1, j, visited)
	}
	if j < 127 {
		search(matrix, i, j+1, visited)
	}
}

func main() {
	// fmt.Println(hexToBinString("a0c2017"))
	// key := "flqrgnkx"
	key := "wenycdww"
	used := 0
	matrix := make([][]bool, 128)
	for row := 0; row < 128; row++ {
		hash := knotHash([]byte(key + "-" + strconv.Itoa(row)))
		bin := hexToBinString(hash)
		matrix[row] = make([]bool, 128)
		for i, c := range bin {
			if c == '1' {
				used++
				matrix[row][i] = true
			}
		}
	}
	fmt.Println("Number of used squares :", used)
	nbGroups := 0
	visited := make([][]bool, 128)
	for i := range visited {
		visited[i] = make([]bool, 128)
	}
	for i := range matrix {
		for j, b := range matrix[i] {
			if visited[i][j] {
				continue
			}
			if !b {
				continue
			}
			nbGroups++
			search(matrix, i, j, visited)
		}
	}
	fmt.Println("Number of groups :", nbGroups)
}
