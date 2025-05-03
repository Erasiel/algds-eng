# Minimum Spanning Trees and Shortest Paths

### Exercise 1
Define or briefly describe the following concepts:
- Spanning tree
- Spanning forest
- Minimum spanning tree

---

### Exercise 2

Given the `WeightedGraph` abstract class, extend the adjacency list representation from the previous week to represent edge-weighted graphs. Assume all weights are integers.

```py
class WeightedGraph(ABC):
    def __init__(self, undirected: bool = False) -> None:
        super().__init__()
        self.undirected = undirected

    @abstractmethod
    def add_vertex(self, vertex_id: str) -> None:
        raise NotImplementedError("Abstract class Graph does not implement "
                                  "add_vertex")

    @abstractmethod
    def add_edge(self, vertex_from: str, vertex_to: str, weight: int) -> None:
        raise NotImplementedError("Abstract class Graph does not implement "
                                  "add_edge")

    @abstractmethod
    def get_vertices(self) -> List[str]:
        raise NotImplementedError("Abstract class Graph does not implement "
                                  "get_vertices")

    @abstractmethod
    def get_neighbors(self, vertex_id: str) -> List[Tuple[str, int]]:
        raise NotImplementedError("Abstract class Graph does not implement "
                                  "get_neighbors")

    @abstractmethod
    def edge_exists(self, vertex_from: str, vertex_to: str) -> bool:
        raise NotImplementedError("Abstract class Graph does not implement "
                                  "edge_exists")

    @abstractmethod
    def get_edges(self) -> List[Tuple[str, str, int]]:
        raise NotImplementedError("Abstract class Graph does not implement "
                                  "get_edges")

    @abstractmethod
    def get_edge_weight(self, vertex_from: str, vertex_to: str) -> int:
        raise NotImplementedError("Abstract class Graph does not implement "
                                  "get_edge_weight")
```

---

### Exercise 3

Run Kruskal's algorithm (first without implementing it) on the following graph. Describe the greedy choice and its related implementation.

![MST exercise graph](./img/10_mst_sp_exercise03.svg)

---

### Exercise 4

Implement Kruskal's algorithm. Use the example of Exercise 3 for guidance and the outline below with the edge-weighted `Graph` subclasses from Exercise 2. Return the list of edges that make up the minimum spanning tree. You are given an extremely simple Union-Find (also known as Disjoint Set) implementation.

```py
from typing import List, Tuple


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
# `graph` is an object of a subclass of WeightedGraph with undirected=True (Exercise 2)
graph.add_vertex("A")
graph.add_vertex("B")
graph.add_vertex("C")
graph.add_vertex("D")
graph.add_vertex("E")
graph.add_vertex("F")
graph.add_vertex("G")
graph.add_vertex("H")
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

Run Prim's algorithm (first without implementing it) on the graph of Exercise 3. Start from vertex `H`. Describe the greedy choice and its related implementation.

---

### Exercise 6

You are given the complete implementation of Prim's algorithm. What would be the algorithm's output on a graph that does not have a minimum spanning tree? Try it on a simple example.

What would be the output of Kruskal's algorithm in the same case?

```py
from typing import List, Tuple


def prim_mst(graph: WeightedGraph,
             start_vertex: str
) -> List[Tuple[str, str, int]]:

    # Create a minimum priority queue for storing vertices where the priority of
    # a vertex is the cost of adding it to the MST. During the algorithm, the
    # priority of a vertex is the cost of adding that vertex to the MST.
    priqueue = PriorityQueue()

    # Store the parents of each vertex
    parent = dict()

    # Store the list of MST edges
    mst_edges = list()

    # Initialize each vertex with infinite priority and no parent
    for vertex in graph.get_vertices():
        priqueue.insert(vertex, math.inf)
        parent[vertex] = None

    # Set the start vertex's priority to 0
    priqueue.set_priority(start_vertex, 0)

    # Repeat the following until all vertices are added to the MST
    while len(priqueue) > 0:

        # The vertex with the lowest cost is the next to be added to the MST
        mst_vertex = priqueue.min()
        mst_edge_weight = priqueue.get_priority(mst_vertex)
        priqueue.extract_min()

        # If the vertex has a valid parent, add the corresponding edge to the
        # MST edges
        if parent[mst_vertex] is not None:
            mst_edges.append((parent[mst_vertex], mst_vertex, mst_edge_weight))

        # Iterate over the neighbors of the new MST vertex
        for vertex, edge_weight in graph.get_neighbors(mst_vertex):

            # We don't care about a neighbor that is already in the MST
            if not vertex in priqueue: continue

            # If the edge to the neighbor has a lower weight than the previous
            # lowest weight, update the neighbor
            found_weight = priqueue.get_priority(vertex)
            if edge_weight < found_weight:
                priqueue.set_priority(vertex, edge_weight)
                parent[vertex] = mst_vertex

    # Return the edges of the MST
    return mst_edges
```

---

### Exercise 7

How can you define the shortest path between two vertices in a graph? What variants of the shortest path(s) problem do you know? Which algorithms solve which variant?

---

### Exercise 8

Run Dijkstra's algorithm (first without implementing it) on the following graph. Start from vertex `A`. Describe the greedy choice and its related implementation.

![SP exercise graph](img/10_mst_sp_exercise08.svg)

---

### Exercise 9

Using the outline below, implement Dijkstra's algorithm. The `DijkstraOut` type represents the properties of a vertex that are computed by the algorithm.

```py
from typing import Dict


class DijkstraOut:
    def __init__(self, parent: str, dist: int) -> None:
        self.parent = parent
        self.dist = dist


def dijkstra_sssp(graph: WeightedGraph,
                  start_vertex: str
) -> Dict[str, DijkstraOut]:
    distance = dict()
    parent = dict()

    # TODO

    # Return a dict of DijkstraOut objects
    # This is not strictly required, we could return the `parent` and
    # `distance` dictionaries instead
    return {v: DijkstraOut(parent[v], distance[v])
            for v in graph.get_vertices()}
```

Hints:
- You can use the implementation of breadth-first search from the previous week. The difference between BFS and Dijkstra's algorithm is the used data structure: BFS uses a queue, Dijkstra uses a minimum priority queue where the priority of a vertex is its distance from the starting vertex.
- You can also use the implementation of Prim's algorithm from Exercise 6. The main difference between Prim and Dijkstra is the priority of each vertex: in Prim's algorithm, it's the cost of adding the vertex to the MST, in Dijkstra's algorithm, it's the vertex's distance from the starting vertex.


```py
# `graph` is an object of a subclass of WeightedGraph with undirected=True (Exercise 2)
graph.add_vertex("A")
graph.add_vertex("B")
graph.add_vertex("C")
graph.add_vertex("D")
graph.add_vertex("E")
graph.add_vertex("F")
graph.add_vertex("G")
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

