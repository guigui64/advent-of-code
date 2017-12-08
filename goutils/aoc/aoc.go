// Package aoc provides specific functions for the advent-of-code event
package aoc

import (
	"io/ioutil"
	"strings"

	"github.com/guigui64/gcgo/utils"
)

func ReadAndCheckFile(fileName string) []byte {
	f, e := ioutil.ReadFile(fileName)
	utils.Check(e)
	return f
}

func ParseInput(fileName string) [][]string {
	file := ReadAndCheckFile(fileName)
	var fieldsMatrix [][]string
	for _, line := range strings.Split(string(file), "\n") {
		if strings.TrimSpace(line) != "" {
			fieldsMatrix = append(fieldsMatrix, strings.Fields(line))
		}
	}
	return fieldsMatrix
}
