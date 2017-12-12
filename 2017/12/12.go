package main

import (
	"fmt"
	"os"
	"reflect"
	"strconv"
	"strings"

	"github.com/guigui64/advent-of-code/goutils/aoc"
)

func main() {
	fileName := "12.in"
	if len(os.Args) > 1 {
		fileName = os.Args[1]
	}
	f := aoc.ReadAndCheckFile(fileName)
	groups := make(map[int]map[int]bool)
	for _, line := range strings.Split(string(f), "\n") {
		if strings.TrimSpace(line) == "" {
			continue
		}
		kv := strings.Split(line, " <-> ")
		key, _ := strconv.Atoi(kv[0])
		var values []int
		for _, v := range strings.Split(kv[1], ", ") {
			vv, _ := strconv.Atoi(v)
			values = append(values, vv)
		}
		values = append(values, key)
		for i := range values {
			for j := range values {
				//if i != j {
				if groups[values[i]] == nil {
					groups[values[i]] = make(map[int]bool)
				}
				groups[values[i]][values[j]] = true
				//}
			}
		}
	}
	fmt.Println(groups)
	group0 := make(map[int]bool)
	alreadyVisited := make(map[int]bool)
	group0 = fill(group0, alreadyVisited, groups, 0)
	fmt.Println(group0, " => ", len(group0))
	var p2groups []map[int]bool
	for v, _ := range groups {
		tmp := make(map[int]bool)
		alreadyVisited = make(map[int]bool)
		tmp = fill(tmp, alreadyVisited, groups, v)
		newGroup := true
		for _, g := range p2groups {
			if reflect.DeepEqual(g, tmp) {
				newGroup = false
			}
		}
		if newGroup {
			p2groups = append(p2groups, tmp)
		}
	}
	fmt.Println(len(p2groups))
}

func fill(dest, alreadyVisited map[int]bool, pool map[int]map[int]bool, n int) map[int]bool {
	alreadyVisited[n] = true
	for v, _ := range pool[n] {
		dest[v] = true
		if !alreadyVisited[v] {
			dest = fill(dest, alreadyVisited, pool, v)
		}
	}
	return dest
}
