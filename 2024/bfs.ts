// Define the Node interface for the graph
export type Node<T> = {
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

// Path type to store both the node and the path taken to reach it
interface PathNode<T> {
  node: Node<T>;
  path: Node<T>[];
}

export function findAllPaths<T>(
  startNode: Node<T>,
  targetValue: T,
): Node<T>[][] {
  // Store all found paths
  const allPaths: Node<T>[][] = [];

  // Queue will store nodes along with their paths
  const queue = new Queue<PathNode<T>>();
  queue.enqueue({ node: startNode, path: [startNode] });

  while (!queue.isEmpty()) {
    const currentPath = queue.dequeue();
    if (!currentPath) continue;

    const { node: currentNode, path: currentNodePath } = currentPath;

    // If we found target value, add the path to our results
    if (currentNode.value === targetValue) {
      allPaths.push([...currentNodePath]);
      continue;
    }

    // Process adjacent nodes
    for (const adjacentNode of currentNode.adjacent) {
      // Skip if this would create a cycle
      if (currentNodePath.includes(adjacentNode)) continue;

      // Create new path including this adjacent node
      const newPath = [...currentNodePath, adjacentNode];
      queue.enqueue({
        node: adjacentNode,
        path: newPath,
      });
    }
  }

  return allPaths;
}

export function findAllTargets<T>(
  startNode: Node<T>,
  targetValue: T,
): Set<Node<T>> {
  // Store all found paths
  const allTargets: Set<Node<T>> = new Set();

  // Queue will store nodes along with their paths
  const queue = new Queue<PathNode<T>>();
  queue.enqueue({ node: startNode, path: [startNode] });

  while (!queue.isEmpty()) {
    const currentPath = queue.dequeue();
    if (!currentPath) continue;

    const { node: currentNode, path: currentNodePath } = currentPath;

    // If we found target value, add the path to our results
    if (currentNode.value === targetValue) {
      allTargets.add(currentNode);
      continue;
    }

    // Process adjacent nodes
    for (const adjacentNode of currentNode.adjacent) {
      // Skip if this would create a cycle
      if (currentNodePath.includes(adjacentNode)) continue;

      // Create new path including this adjacent node
      const newPath = [...currentNodePath, adjacentNode];
      queue.enqueue({
        node: adjacentNode,
        path: newPath,
      });
    }
  }

  return allTargets;
}
