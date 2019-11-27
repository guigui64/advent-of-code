package main

import (
	"fmt"
	"strconv"
	"strings"
)

func main() {
	input := `set b 99
set c b
jnz a 2
jnz 1 5
mul b 100
sub b -100000
set c b
sub c -17000
set f 1
set d 2
set e 2
set g d
mul g e
sub g b
jnz g 2
set f 0
sub e -1
set g e
sub g b
jnz g -8
sub d -1
set g d
sub g b
jnz g -13
jnz f 2
sub h -1
set g b
sub g c
jnz g 2
jnz 1 3
sub b -17
jnz 1 -23`
	registers := make(map[string]int)
	get := func(s string) int {
		if strings.IndexAny(s, "0123456789") != -1 {
			v, err := strconv.Atoi(s)
			if err != nil {
				panic(err)
			}
			return v
		}
		return registers[s]
	}
	commands := strings.Split(input, "\n")
	var instr int
	var mulCntr int
	for count := 0; instr >= 0 && instr < len(commands); count++ {

		command := strings.TrimSpace(commands[instr])
		if command == "" {
			instr++
			continue
		}

		args := strings.Fields(commands[instr])
		switch cmd, argv := args[0], args[1:]; cmd {
		case "set":
			registers[argv[0]] = get(argv[1])
		case "sub":
			registers[argv[0]] -= get(argv[1])
		case "mul":
			registers[argv[0]] *= get(argv[1])
			mulCntr++
		case "jnz":
			if get(argv[0]) == 0 {
				break
			}
			instr += get(argv[1])
			continue
		default:
			panic(command)
		}
		instr++
	}
	fmt.Println(mulCntr)

	for i := 1; i < 10; i += 2 {
		fmt.Println(i)
	}

}
