package main

import (
	"fmt"
	"math"
	"strconv"
	"strings"

	"github.com/guigui64/advent-of-code/goutils/aoc"
)

type Particule struct {
	PX, PY, PZ int
	VX, VY, VZ int
	AX, AY, AZ int
}

func (p Particule) distTo0() int {
	return int(math.Abs(float64(p.PX)) + math.Abs(float64(p.PY)) + math.Abs(float64(p.PZ)))
}

func (p1 Particule) equalPos(p2 Particule) bool {
	return p1.PX == p2.PX && p1.PY == p2.PY && p1.PZ == p2.PZ
}

func delete(s []Particule, pos int) []Particule {
	s[pos] = s[len(s)-1]
	s = s[:len(s)-1]
	return s
}

func main() {
	input := aoc.ParseInput("20.in")
	var parts []Particule
	for _, line := range input {
		spos, svel, sacc := line[0][3:len(line[0])-2], line[1][3:len(line[1])-2], line[2][3:len(line[2])-1]
		pos, vel, acc := strings.Split(spos, ","), strings.Split(svel, ","), strings.Split(sacc, ",")
		var p Particule
		p.PX, _ = strconv.Atoi(pos[0])
		p.PY, _ = strconv.Atoi(pos[1])
		p.PZ, _ = strconv.Atoi(pos[2])
		p.VX, _ = strconv.Atoi(vel[0])
		p.VY, _ = strconv.Atoi(vel[1])
		p.VZ, _ = strconv.Atoi(vel[2])
		p.AX, _ = strconv.Atoi(acc[0])
		p.AY, _ = strconv.Atoi(acc[1])
		p.AZ, _ = strconv.Atoi(acc[2])
		parts = append(parts, p)
	}
	bkp := make([]Particule, len(parts))
	copy(bkp, parts)
	// Part 1
	maxtime := int(1e3)
	for t := 0; t < maxtime; t++ {
		for i := range parts {
			parts[i].VX += parts[i].AX
			parts[i].VY += parts[i].AY
			parts[i].VZ += parts[i].AZ
			parts[i].PX += parts[i].VX
			parts[i].PY += parts[i].VY
			parts[i].PZ += parts[i].VZ
		}
		if t%(maxtime/10) == 0 {
			closestIdx := 0
			for i, p := range parts {
				if parts[closestIdx].distTo0() > p.distTo0() {
					closestIdx = i
				}
			}
			fmt.Println("t =", t, "closest =", closestIdx)
		}
	}
	copy(parts, bkp)
	// Part 2
	for t := 0; t < maxtime; t++ {
		for i := range parts {
			parts[i].VX += parts[i].AX
			parts[i].VY += parts[i].AY
			parts[i].VZ += parts[i].AZ
			parts[i].PX += parts[i].VX
			parts[i].PY += parts[i].VY
			parts[i].PZ += parts[i].VZ
		}
		for i := 0; i < len(parts)-1; {
			p1 := parts[i]
			hasEqual := false
			for j := 0; j < len(parts); {
				p2 := parts[j]
				if i != j && p1.equalPos(p2) {
					hasEqual = true
					parts = delete(parts, j)
					continue // do not increase j
				}
				j++
			}
			if hasEqual {
				parts = delete(parts, i)
				continue // do not increase i
			}
			i++
		}
		if t%(maxtime/10) == 0 {
			fmt.Println("t =", t, "remaining particules =", len(parts))
		}
	}
}
