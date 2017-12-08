package main

import (
	"fmt"
	"os"
	"strconv"
	"strings"

	"github.com/guigui64/advent-of-code/goutils/aoc"
)

type Program struct {
	Weight        int
	Name          string
	HasParent     bool
	ChildrenNames []string
}

func (p Program) TotalWeight(m map[string]Program) (weight int) {
	weight += p.Weight
	for _, cn := range p.ChildrenNames {
		weight += m[cn].TotalWeight(m)
	}
	return
}

func main() {
	fileName := "07.in"
	if len(os.Args) > 1 { // first is prog name
		fileName = os.Args[1]
	}
	input := aoc.ParseInput(fileName)
	towers := make(map[string]Program)
	for _, fields := range input {
		name := fields[0]
		weight, _ := strconv.Atoi(fields[1][1 : len(fields[1])-1])
		program := Program{Weight: weight, Name: name}
		if len(fields) > 2 {
			var children []string
			for _, cf := range fields[3:len(fields)] {
				if idx := strings.Index(cf, ","); idx > -1 {
					cf = cf[0:idx]
				}
				children = append(children, cf)
			}
			program.ChildrenNames = children
		}
		towers[name] = program
	}
	fmt.Println(towers)
	// Loop again for setting the HasParent field
	for _, program := range towers {
		for _, child := range program.ChildrenNames {
			if cprog, ok := towers[child]; ok {
				cprog.HasParent = true
				towers[child] = cprog
			}
		}
	}
	// Loop again to find the root (the only one without parent)
	for _, program := range towers {
		if !program.HasParent {
			fmt.Println(program.Name, "has no parent")
			break
		}
	}
	// Find unbalanced disk
	totalWeights := make(map[string]int)
	for _, program := range towers {
		totalWeights[program.Name] = program.TotalWeight(towers)
	}
	fmt.Println(totalWeights)
	for _, program := range towers {
		if program.ChildrenNames != nil {
			// this program holds a disk
			ref := totalWeights[program.ChildrenNames[0]]
			for i := 1; i < len(program.ChildrenNames); i++ {
				if totalWeights[program.ChildrenNames[i]] != ref {
					fmt.Print(program.Name, " disk is unbalanced")
					fmt.Println(" and has children :", program.ChildrenNames)
					break
				}
			}
		}
	}
	fmt.Println("Look for the answer with the above output :p") // TODO code it

}
