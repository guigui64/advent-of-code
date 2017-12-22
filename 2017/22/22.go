package main

import "fmt"

func main() {
	example := [][]byte{
		[]byte("..#"),
		[]byte("#.."),
		[]byte("..."),
	}
	input := [][]byte{
		[]byte(".#...#.#.##..##....##.#.#"),
		[]byte("###.###..##...##.##....##"),
		[]byte("....#.###..#...#####..#.#"),
		[]byte(".##.######..###.##..#...#"),
		[]byte("#..#..#..##..###...#..###"),
		[]byte("..####...#.##.#.#.##.####"),
		[]byte("#......#..####..###..###."),
		[]byte("#####.##.#.#.##.###.#.#.#"),
		[]byte(".#.###....###....##....##"),
		[]byte(".......########.#.#...#.."),
		[]byte("...###.####.##..###.##..#"),
		[]byte("#.#.###.####.###.###.###."),
		[]byte(".######...###.....#......"),
		[]byte("....##.###..#.#.###...##."),
		[]byte("#.###..###.#.#.##.#.##.##"),
		[]byte("#.#.#..###...###.###....."),
		[]byte("##..##.##...##.##..##.#.#"),
		[]byte(".....##......##..#.##...#"),
		[]byte("..##.#.###.#...#####.#.##"),
		[]byte("....##..#.#.#.#..###.#..#"),
		[]byte("###..##.##....##.#....##."),
		[]byte("#..####...####.#.##..#.##"),
		[]byte("####.###...####..##.#.#.#"),
		[]byte("#.#.#.###.....###.##.###."),
		[]byte(".#...##.#.##..###.#.###.."),
	}
	fmt.Println(compute(example, 1000, 10000, false))
	fmt.Println(compute(input, 5000, 10000, false))

	fmt.Println(compute(example, 1000, 10000000, true))
	fmt.Println(compute(input, 1000, 10000000, true))
}

const (
	UP    = 0
	RIGHT = 1
	DOWN  = 2
	LEFT  = 3
)

func compute(in [][]byte, margin, maxIter int, part2 bool) (infections int) {
	theMap := make([][]byte, len(in)+2*margin)
	for i := range theMap {
		theMap[i] = make([]byte, len(in[0])+2*margin)
		for j := range theMap[i] {
			theMap[i][j] = '.'
			if i >= margin && i < len(theMap)-margin {
				if j >= margin && j < len(theMap[i])-margin {
					theMap[i][j] = in[i-margin][j-margin]
				}
			}
		}
	}
	// display(theMap)
	vI, vJ, vDir := len(theMap)/2, len(theMap[0])/2, UP
	for iter := 0; iter < maxIter; iter++ {
		// 	fmt.Println(vI, vJ, vDir)
		if !part2 {
			if theMap[vI][vJ] == '#' {
				// current node is infected
				// turn right
				vDir = (vDir + 1) % 4
				theMap[vI][vJ] = '.'
			} else {
				// current node is clean
				// turn left
				vDir = (vDir - 1) % 4
				if vDir == -1 {
					vDir = 3
				}
				theMap[vI][vJ] = '#'
				infections++
			}
		} else {
			if theMap[vI][vJ] == '#' {
				vDir = (vDir + 1) % 4
				theMap[vI][vJ] = 'F'
			} else if theMap[vI][vJ] == '.' {
				vDir--
				if vDir == -1 {
					vDir = 3
				}
				theMap[vI][vJ] = 'W'
			} else if theMap[vI][vJ] == 'W' {
				theMap[vI][vJ] = '#'
				infections++
			} else if theMap[vI][vJ] == 'F' {
				vDir = (vDir + 2) % 4
				theMap[vI][vJ] = '.'
			}
		}
		switch vDir {
		case UP:
			vI--
		case DOWN:
			vI++
		case RIGHT:
			vJ++
		case LEFT:
			vJ--
		}
	}
	// display(theMap)
	return
}

func display(image [][]byte) {
	for _, line := range image {
		fmt.Println(string(line))
	}
}
