package main

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
	"strings"
)

// A Cell of a Bingo board
type Cell struct {
	X, Y   uint
	Value  int
	Marked bool
}

func (c *Cell) Mark() {
	c.Marked = true
}

// A Bingo board
type Board struct {
	H, W   uint
	Cells  []Cell
	HasWon bool
}

// Find Cell at x,y in board
func (b *Board) Find(x, y uint) *Cell {
	for _, cell := range b.Cells {
		if cell.X == x && cell.Y == y {
			return &cell
		}
	}
	panic("Could not find cell...")
}

// Check if board has won
func (b *Board) Wins() bool {
	// Check rows
	for h := uint(0); h < b.H; h++ {
		wins := true
		for w := uint(0); w < b.W; w++ {
			cell := b.Find(w, h)
			if !cell.Marked {
				wins = false
				break
			}
		}
		if wins {
			return true
		}
	}
	// Check columns
	for w := uint(0); w < b.W; w++ {
		wins := true
		for h := uint(0); h < b.H; h++ {
			cell := b.Find(w, h)
			if !cell.Marked {
				wins = false
				break
			}
		}
		if wins {
			return true
		}
	}
	return false
}

func (b *Board) Score(last int) int {
	sum := 0
	for _, cell := range b.Cells {
		if !cell.Marked {
			sum += cell.Value
		}
	}
	return sum * last
}

func (b *Board) Play(number int) {
	for i := range b.Cells {
		if b.Cells[i].Value == number {
			b.Cells[i].Mark()
		}
	}
}

func (b *Board) String() string {
	var sb strings.Builder
	for h := uint(0); h < b.H; h++ {
		for w := uint(0); w < b.W; w++ {
			cell := b.Find(w, h)
			m := " "
			if cell.Marked {
				m = "*"
			}
			sb.WriteString(fmt.Sprintf("%s%02d%s ", m, cell.Value, m))
		}
		sb.WriteString("\n")
	}
	return sb.String()
}

func NewBoard(lines []string) Board {
	h := uint(len(lines))
	w := uint(len(strings.Fields(lines[0])))
	board := Board{H: h, W: w, Cells: make([]Cell, 0, h*w), HasWon: false}
	for y, line := range lines {
		for x, num := range strings.Fields(line) {
			value, err := strconv.Atoi(num)
			if err != nil {
				panic(err)
			}
			board.Cells = append(board.Cells, Cell{uint(x), uint(y), value, false})
		}
	}
	return board
}

func main() {
	filename := "04.txt"
	if len(os.Args) > 1 {
		filename = os.Args[1]
	}
	file, err := os.Open(filename)
	if err != nil {
		panic(err)
	}
	defer file.Close()

	scanner := bufio.NewScanner(file)
	bingo := make([]int, 0)
	boardIn := make([]string, 0)
	boards := make([]Board, 0)
	for scanner.Scan() {
		line := scanner.Text()
		if len(bingo) == 0 {
			for _, number := range strings.Split(line, ",") {
				inum, err := strconv.Atoi(number)
				if err != nil {
					panic(err)
				}
				bingo = append(bingo, inum)
			}
			continue
		}

		if len(line) == 0 {
			if len(boardIn) == 0 {
				continue
			}
			boards = append(boards, NewBoard(boardIn))
			boardIn = make([]string, 0)
			continue
		}

		boardIn = append(boardIn, line)
	}
	boards = append(boards, NewBoard(boardIn))

	for _, number := range bingo {
		// fmt.Println("Playing", number)
		for i, board := range boards {
			if board.HasWon {
				continue
			}
			board.Play(number)
			// fmt.Println(board.String())
			if board.Wins() {
				fmt.Println("Board", i, "wins")
				fmt.Println(board.Score(number))
				boards[i].HasWon = true
			}
		}
	}
}
