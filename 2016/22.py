from re import findall
from collections import defaultdict

class Node:
    def __init__(self, x, y, size, used):
        self.x = x
        self.y = y
        self.size = size
        self.used = used
        self.up = None
        self.down = None
        self.right = None
        self.left = None

    def get_name(self):
        return "node-x{}-y{}".format(self.x, self.y)

    def is_empty(self):
        return self.used == 0

    def can_fit_in(self, other):
        return self.used <= (other.size - other.used)

    def move_in(self, dest):
        dest.used += self.used
        self.used = 0

def compute_viables(nodes):
    viable_pairs = set()
    for nodeA in nodes:
        for nodeB in nodes:
            if not nodeA.is_empty() and nodeA != nodeB and nodeA.can_fit_in(nodeB):
                viable_pairs.add((nodeA, nodeB))
    return viable_pairs

def pretty_print(nodes):
    matrix = defaultdict(lambda : defaultdict(str))
    for node in nodes:
        c = '.'
        if node.size > 500:
            c = '#'
        elif node.used == 0:
            c = '_'
        matrix[node.y][node.x] = c
    matrix[0][0] = '!'
    line0 = ""
    line1 = ""
    for x in sorted(matrix[0]):
        line0 += str(int(x/10))
        line1 += str(x%10)
    print("{0:2} {1} {0:2}".format("", line0))
    print("{0:2} {1} {0:2}".format("", line1))
    for y in matrix:
        line = ""
        for x in sorted(matrix[y]):
            line += matrix[y][x]
        if y == 0:
            line = line[:-1] + 'G'
        print("{0:2} {1} {0:2}".format(y, line))
    print("{0:2} {1} {0:2}".format("", line0))
    print("{0:2} {1} {0:2}".format("", line1))

if __name__ == '__main__':
    nodes = []
    target = None
    with open("22.txt", "r") as f:
        for line in f:
            if line.startswith("/dev"):
                x, y = [int(z) for z in findall(r"\d+", line.split()[0].rsplit('/', 1)[1])]
                size, used = [int(z[:-1]) for z in line.split()[1:3]]
                node = Node(x, y, size, used)
                nodes.append(node)
                # print("{} -> Append node at ({},{}) with size {}T and used {}T".format(line, x, y, size, used))
                if target is None or target.x < node.x:
                    target = node

    # Part 1
    print(len(compute_viables(nodes)))

    # Part 2
    print("Target is node at ({},{}) with size {}T and used {}T".format(
        target.x, target.y, target.size, target.used))
    print("""Solve it by looking at this map.
          ! is the node where to move the data
          G is the target
          # are walls (to much data)
          _ are empty nodes
          . are any other node
          1) move the closest _ to the left of G
          2) go from _G to G_ by doing 5 moves
          3) repeat 2 until _G is at the top-left (31 times => 31*5=155)
          4) move G to top-left (+1)""")

    pretty_print(nodes)
