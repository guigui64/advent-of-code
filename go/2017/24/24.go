package main

import (
	"fmt"
	"strconv"
	"strings"
)

type Node struct{ E1, E2 int }

func computeStrength(nodes []Node) (strength int) {
	for _, node := range nodes {
		strength += node.E1 + node.E2
	}
	return
}

func find(bridge, pool []Node, maxStrength, longestLength, longestStrength int) (int, int, int) {
	if computeStrength(bridge) > maxStrength {
		maxStrength = computeStrength(bridge)
	}
	if len(bridge) > longestLength {
		longestLength = len(bridge)
		longestStrength = computeStrength(bridge)
	} else if len(bridge) == longestLength && computeStrength(bridge) > longestStrength {
		longestStrength = computeStrength(bridge)
	}
	if len(pool) == 0 {
		return maxStrength, longestLength, longestStrength
	}
	for i := range pool {
		if pool[i].E1 == bridge[len(bridge)-1].E2 {
			cbridge := make([]Node, len(bridge))
			copy(cbridge, bridge)
			cbridge = append(cbridge, pool[i])
			cpool := make([]Node, len(pool))
			copy(cpool, pool)
			cpool[i] = cpool[len(cpool)-1]
			cpool = cpool[:len(cpool)-1]
			maxStrength, longestLength, longestStrength = find(cbridge, cpool, maxStrength, longestLength, longestStrength)
		} else if pool[i].E2 == bridge[len(bridge)-1].E2 {
			cbridge := make([]Node, len(bridge)+1)
			copy(cbridge, bridge)
			cbridge[len(cbridge)-1].E1, cbridge[len(cbridge)-1].E2 = pool[i].E2, pool[i].E1
			cpool := make([]Node, len(pool))
			copy(cpool, pool)
			cpool[i] = cpool[len(cpool)-1]
			cpool = cpool[:len(cpool)-1]
			maxStrength, longestLength, longestStrength = find(cbridge, cpool, maxStrength, longestLength, longestStrength)
		}
	}
	return maxStrength, longestLength, longestStrength
}

func main() {
	input := `50/41
19/43
17/50
32/32
22/44
9/39
49/49
50/39
49/10
37/28
33/44
14/14
14/40
8/40
10/25
38/26
23/6
4/16
49/25
6/39
0/50
19/36
37/37
42/26
17/0
24/4
0/36
6/9
41/3
13/3
49/21
19/34
16/46
22/33
11/6
22/26
16/40
27/21
31/46
13/2
24/7
37/45
49/2
32/11
3/10
32/49
36/21
47/47
43/43
27/19
14/22
13/43
29/0
33/36
2/6`
	var nodes []Node
	for _, line := range strings.Split(input, "\n") {
		if line == "" {
			continue
		}
		sends := strings.Split(line, "/")
		e1, _ := strconv.Atoi(sends[0])
		e2, _ := strconv.Atoi(sends[1])
		nodes = append(nodes, Node{e1, e2})
	}
	var maxStrength, longestLength, longestStrength int
	for i, node := range nodes {
		if node.E1 == 0 {
			bridge := []Node{node}
			pool := make([]Node, len(nodes))
			copy(pool, nodes)
			pool[i] = pool[len(pool)-1]
			pool = pool[:len(pool)-1]
			maxStrength, longestLength, longestStrength = find(bridge, pool, maxStrength, longestLength, longestStrength)
		} else if node.E2 == 0 {
			bridge := []Node{node}
			bridge[len(bridge)-1].E1, bridge[len(bridge)-1].E2 = node.E2, node.E1
			pool := make([]Node, len(nodes))
			copy(pool, nodes)
			pool[i] = pool[len(pool)-1]
			pool = pool[:len(pool)-1]
			maxStrength, longestLength, longestStrength = find(bridge, pool, maxStrength, longestLength, longestStrength)
		}
	}
	fmt.Println(maxStrength)
	fmt.Println(longestStrength)
}
