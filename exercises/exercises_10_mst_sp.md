# Minimum Spanning Trees and Shortest Paths

### Exercise 1
Define or briefly describe the following concepts:
- Spanning tree
- Spanning forest
- Minimum spanning tree

---

### Exercise 2

Extend the `Graph` abstract class and one of its implementations from the previous week to represent edge-weighted graphs. All weigths are integer values.

---

### Exercise 3

Run Kruskal's algorithm (first without implementing it) on the following graph. Describe the greedy choice and its related implementation.

![MST exercise graph](./img/10_mst_sp_exercise03.svg)

---

### Exercise 4

Implement Kruskal's algorithm. Use the example of Exercise 3 for guidance and the outline below with the edge-weighted `Graph` subclasses from Exercise 2. Return the list of edges that make up the minimum spanning tree. You are given an extremely simple Union-Find (also known as Disjoint Set) implementation.

```py
class DisjointSet:
    def __init__(self) -> None:
        self.elements = {}

    def make_set(self, elem: str) -> None:
        """Creates a new one-element set."""
        self.elements[elem] = elem

    def union(self, u: str, v: str) -> None:
        """Unites the two sets that contain `u` and `v`."""
        rep_u = self.find(u)
        rep_v = self.find(v)
        for elem in self.elements:
            if self.find(elem) == rep_u:
                self.elements[elem] = rep_v

    def find(self, u: str) -> str:
        """Finds the representative of the set that contains `u`."""
        return self.elements[u]


def kruskal_mst(graph: Graph) -> List[Tuple[str, str, int]]:
    # TODO
```

Check the correctness of your implementation on the graph of Exercise 3. Use the following code snippet to create the graph:

```py
# `graph` is an object of a subclass of Graph with undirected=True (Exercise 2)
graph.add_node("A")
graph.add_node("B")
graph.add_node("C")
graph.add_node("D")
graph.add_node("E")
graph.add_node("F")
graph.add_node("G")
graph.add_node("H")
graph.add_edge("A", "B", 3)
graph.add_edge("A", "D", 2)
graph.add_edge("B", "D", 1)
graph.add_edge("B", "E", 4)
graph.add_edge("C", "E", 2)
graph.add_edge("C", "H", 6)
graph.add_edge("D", "E", 3)
graph.add_edge("D", "F", 4)
graph.add_edge("E", "G", 1)
graph.add_edge("E", "H", 5)
graph.add_edge("F", "G", 4)
```

---

### Exercise 5

Run Prim's algorithm (first without implementing it) on the graph of Exercise 3. Start from node `H`. Describe the greedy choice and its related implementation.

---

### Exercise 6

You are given a basic outline of Prim's algorithm. The algorithm seems to follow the original pseudocode, so you can assume it to be correct. However, a key component, namely, the `PriorityQueue` implementation is missing. Finish the implementation without modifying the `prim_mst` algorithm. Make sure the algorithm is correct.

```py
import math


class PriorityQueue:
    # TODO
    pass


def prim_mst(graph: Graph, start_node: str) -> List[Tuple[str, str, int]]:

    # Create a minimum priority queue for storing nodes where the priority of a
    # node is the cost of adding it to the MST.
    node_priqueue = PriorityQueue(min_first=True)

    # Store the parents of each node.
    node_parent = dict()

    # Store the list of MST edges
    mst_edges = list()

    # Initialize each node with infinite priority and no parent
    for node in graph.get_nodes():
        node_priqueue.insert(node, math.inf)
        node_parent[node] = None

    # Set the start node's priority to 0
    node_priqueue.set_priority(start_node, 0)

    # Repeat the following until all nodes are added to the MST
    while not node_priqueue.is_empty():

        # The node with the lowest cost is the next to be added to the MST
        mst_node = node_priqueue.top()
        mst_edge_weight = node_priqueue.get_priority(mst_node)
        node_priqueue.remove_top()

        # If the node has a valid parent, add the corresponding edge to the MST
        # edges
        if node_parent[mst_node] is not None:
            mst_edges.append((node_parent[mst_node], mst_node, mst_edge_weight))

        # Iterate over the neighbors of the new MST node
        for node, edge_weight in graph.get_neighbors(mst_node):

            # We don't care about a neighbor that's already in the MST
            if not node_priqueue.contains(node): continue

            # If the edge to the neighbor has a lower weight than the previous
            # lowest weight, update the neighbor
            found_weight = node_priqueue.get_priority(node)
            if edge_weight < found_weight:
                node_priqueue.set_priority(node, edge_weight)
                node_parent[node] = mst_node

    # Return the edges of the MST
    return mst_edges
```

---

### Exercise 7

How can you define the shortest path between two nodes in a graph? What variants of the shortest path(s) problem do you know? Which algorithms solve which variant?

---

### Exercise 8

Run Dijkstra's algorithm (first without implementing it) on the following graph. Start from node `A`. Describe the greedy choice and its related implementation.

![SP exercise graph](img/10_mst_sp_exercise08.svg)

---

### Exercise 9

Implement Dijkstra's algorithm. Since the algorithms of Dijkstra and Prim are very similar, use your implementation of Prim's algorithm as a starting point.

Check the correctness of your implementation on the graph of Exercise 3. Use the following code snippet to create the graph:

```py
# `graph` is an object of a subclass of Graph with undirected=False (Exercise 2)
graph.add_node("A")
graph.add_node("B")
graph.add_node("C")
graph.add_node("D")
graph.add_node("E")
graph.add_node("F")
graph.add_node("G")
graph.add_edge("A", "B", 3)
graph.add_edge("A", "D", 7)
graph.add_edge("A", "E", 10)
graph.add_edge("B", "C", 2)
graph.add_edge("B", "E", 5)
graph.add_edge("C", "F", 8)
graph.add_edge("D", "E", 4)
graph.add_edge("D", "G", 8)
graph.add_edge("E", "G", 7)
graph.add_edge("F", "E", 2)
graph.add_edge("F", "G", 1)
```

---

### Exercise 10

Give an example graph on which Dijkstra's algorithm is *not* optimal. Why is this? When is the algorithm guaranteed to be optimal? When is it guaranteed to *not* be optimal? Describe sufficient conditions of the input graph for both cases.

