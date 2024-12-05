// Define the Node interface for the graph
type Node<T> = {
  value: T;
  adjacent: Node<T>[];
};

// Define a Queue class for BFS traversal
class Queue<T> {
  private items: T[];

  constructor() {
    this.items = [];
  }

  enqueue(item: T): void {
    this.items.push(item);
  }

  dequeue(): T | undefined {
    return this.items.shift();
  }

  isEmpty(): boolean {
    return this.items.length === 0;
  }
}

// BFS implementation
export function BFS<T>(startNode: Node<T>, targetValue: T): Node<T> | null {
  // Keep track of visited nodes to avoid cycles
  const visited = new Set<Node<T>>();

  // Create queue for BFS
  const queue = new Queue<Node<T>>();
  queue.enqueue(startNode);

  while (!queue.isEmpty()) {
    const currentNode = queue.dequeue();

    // Skip if undefined (shouldn't happen in practice)
    if (!currentNode) continue;

    // Check if we found the target
    if (currentNode.value === targetValue) {
      return currentNode;
    }

    // Mark current node as visited
    visited.add(currentNode);

    // Add all unvisited adjacent nodes to queue
    for (const adjacentNode of currentNode.adjacent) {
      if (!visited.has(adjacentNode)) {
        queue.enqueue(adjacentNode);
      }
    }
  }

  // Target value not found
  return null;
}

// // Example usage
// function createSampleGraph(): Node<number> {
//   const node1: Node<number> = { value: 1, adjacent: [] };
//   const node2: Node<number> = { value: 2, adjacent: [] };
//   const node3: Node<number> = { value: 3, adjacent: [] };
//   const node4: Node<number> = { value: 4, adjacent: [] };
//   const node5: Node<number> = { value: 5, adjacent: [] };
//
//   node1.adjacent = [node2, node3];
//   node2.adjacent = [node4];
//   node3.adjacent = [node4, node5];
//   node4.adjacent = [node5];
//   node5.adjacent = [];
//
//   return node1;
// }
//
// // Test the implementation
// const graph = createSampleGraph();
// const result = breadthFirstSearch(graph, 5);
// console.log(
//   result ? `Found node with value ${result.value}` : "Value not found",
// );
