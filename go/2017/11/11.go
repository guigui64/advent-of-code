package main

import (
	"fmt"
	"log"
	"math"
	"strings"

	"github.com/guigui64/advent-of-code/goutils/aoc"
	"github.com/guigui64/gcgo/utils"
)

type Hex struct {
	X, Y, Z int
}

func move(h Hex, dir string) Hex {
	switch dir {
	case "s":
		h.X, h.Y, h.Z = h.X, h.Y-1, h.Z+1
	case "n":
		h.X, h.Y, h.Z = h.X, h.Y+1, h.Z-1
	case "ne":
		h.X, h.Y, h.Z = h.X+1, h.Y, h.Z-1
	case "sw":
		h.X, h.Y, h.Z = h.X-1, h.Y, h.Z+1
	case "se":
		h.X, h.Y, h.Z = h.X+1, h.Y-1, h.Z
	case "nw":
		h.X, h.Y, h.Z = h.X-1, h.Y+1, h.Z
	default:
		log.Fatal(dir + " unknown")
	}
	return h
}

func dist(h Hex) int {
	return int((math.Abs(float64(h.X)) + math.Abs(float64(h.Y)) + math.Abs(float64(h.Z))) / 2)
}

func main() {
	f := aoc.ReadAndCheckFile("11.in")
	var h Hex
	var dists []int
	for _, dir := range strings.Split(strings.Split(string(f), "\n")[0], ",") {
		h = move(h, dir)
		dists = append(dists, dist(h))
	}
	fmt.Println(dist(h))
	_, max := utils.MaxIntSlice(dists)
	fmt.Println(max)
}
