package main

import (
	"fmt"
	"strconv"
	"strings"

	"github.com/guigui64/advent-of-code/goutils/aoc"
)

const (
	ACT_ON_ZERO     = 0
	ZERO_WRITE      = 1
	ZERO_DIR        = 2
	ZERO_NEXT_STATE = 3
	ACT_ON_ONE      = 4
	ONE_WRITE       = 5
	ONE_DIR         = 6
	ONE_NEXT_STATE  = 7
)

type State struct {
	write, dir [2]int
	nextState  [2]byte
}

func (s *State) String() string {
	var zeroDirS, oneDirS string
	if s.dir[0] == 1 {
		zeroDirS = "R"
	} else {
		zeroDirS = "L"
	}
	if s.dir[1] == 1 {
		oneDirS = "R"
	} else {
		oneDirS = "L"
	}
	return fmt.Sprintf("{0 : [%d, %s, %d] ; 1 : [%d, %s, %d]}", s.write[0], zeroDirS, s.nextState[0],
		s.write[1], oneDirS, s.nextState[1])
}

func main() {
	f := aoc.ReadAndCheckFile("25.in")
	var startingState, currentState byte
	var numberOfSteps, cursor int
	states := make(map[byte]*State)
	for n, line := range strings.Split(string(f), "\n") {
		if strings.TrimSpace(line) == "" {
			continue
		}
		if n == 0 {
			startingState = line[len(line)-2]
		} else if n == 1 {
			var err error
			numberOfSteps, err = strconv.Atoi(strings.Fields(line)[5])
			if err != nil {
				panic("Impossible to convert number of steps")
			}
		} else {
			if strings.Contains(line, "In state") {
				currentState = line[len(line)-2]
				states[currentState] = new(State)
				cursor = ACT_ON_ZERO
				continue
			} else {
				switch cursor {
				case ZERO_WRITE:
					i, _ := strconv.Atoi(string(line[len(line)-2]))
					states[currentState].write[0] = i
				case ZERO_DIR:
					if strings.Contains(line, "left") {
						states[currentState].dir[0] = -1
					} else {
						states[currentState].dir[0] = 1
					}
				case ONE_WRITE:
					i, _ := strconv.Atoi(string(line[len(line)-2]))
					states[currentState].write[1] = i
				case ONE_DIR:
					if strings.Contains(line, "left") {
						states[currentState].dir[1] = -1
					} else {
						states[currentState].dir[1] = 1
					}
				case ZERO_NEXT_STATE:
					states[currentState].nextState[0] = line[len(line)-2]
				case ONE_NEXT_STATE:
					states[currentState].nextState[1] = line[len(line)-2]
				}
				cursor++
			}
		}
	}
	fmt.Println(startingState, numberOfSteps)
	fmt.Println(states)
	tape := make([]int, numberOfSteps*2)
	cursor = numberOfSteps
	state := startingState
	for step := 0; step < numberOfSteps; step++ {
		previous := tape[cursor]
		tape[cursor] = states[state].write[previous]
		cursor += states[state].dir[previous]
		state = states[state].nextState[previous]
		//		fmt.Println(cursor, tape[cursor-10:cursor+10])
	}
	sum := 0
	for _, t := range tape {
		sum += t
	}
	fmt.Println(sum)
}
