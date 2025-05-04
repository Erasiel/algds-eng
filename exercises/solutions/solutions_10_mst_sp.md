# Minimum Spanning Trees and Shortest Paths - Solutions

### Exercise 1
Define or briefly describe the following concepts:
- Spanning tree
- Spanning forest
- Minimum spanning tree

### Solution

The **spanning tree** of a connected, undirected graph is a connected subgraph with a minimal number of edges. In practice, a spanning tree can be seen as a selection of the graph's edges that form a tree (i.e. it is connected and acyclic) that contains every vertex of the graph. Only undirected graphs have spanning trees. Note that if a $G = (V, E)$ graph has a spanning tree, the number of edges in the spanning tree is always $|V| - 1$.

An undirected graph that is not connected does not have a spanning tree, however, its connected components have their own spanning trees. The collection of these spanning trees is called the **spanning forest**. Every undirected graph has a spanning forest, and the number of edges in its spanning forest is $|V| - k$ where $k$ is the number of connected components in the graph. Note that if a graph is connected, $k = 1$ and the spanning forest contains only one tree (the spanning tree).

The **minimum spanning tree**, or **MST** of an *edge-weighted*, connected, undirected graph is a spanning tree where the sum of weights is minimal. Formally, let $T$ be a set of edges that form a spanning tree of a graph, then the weight (also known as the cost) of the tree is $w(T) = \sum_{(u, v) \in T}w(u, v)$, where $w(u, v)$ is the weight of the edge $(u, v)$. A spanning tree is minimal if its weight is minimal.

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

### Solution

Starting from the `AdjacencyListGraph` implementation from the previous week, there are a few places it needs to be modified to represent a weighted graph.

The simplest option is to change the adjacency list from storing only the list of neighbors to storing two-element tuples in the form of `(neighbor, edge_weight)`.

A list of differences between the two implementations are as follows:

`add_edge`:

Unweighted implementation:
```py
def add_edge(self, vertex_from: str, vertex_to: str) -> None:
    # Add the vertices if they are not already in the graph
    self.add_vertex(vertex_from)
    self.add_vertex(vertex_to)

    # Check if the edge is not a duplicate and add it
    if not self.edge_exists(vertex_from, vertex_to):
        self.adjacency_list[vertex_from].append(vertex_to)

    # In undirected graphs, the existence of the edge u -> v means the the
    # edge v -> u also exists
    if self.undirected and not self.edge_exists(vertex_to, vertex_from):
        self.adjacency_list[vertex_to].append(vertex_from)
```

Weighted implementation:
```py
def add_edge(self, vertex_from: str, vertex_to: str, weight: int) -> None:
    # Add the vertices if they are not already in the graph
    self.add_vertex(vertex_from)
    self.add_vertex(vertex_to)

    # Check if the edge is not a duplicate and add it
    if not self.edge_exists(vertex_from, vertex_to):
        self.adjacency_list[vertex_from].append((vertex_to, weight))

    # In undirected graphs, the existence of the edge u -> v means the the
    # edge v -> u also exists
    if self.undirected and not self.edge_exists(vertex_to, vertex_from):
        self.adjacency_list[vertex_to].append((vertex_from, weight))
```

Note that we are appending two-element tuples, as discussed earlier.

`edge_exists`:

Unweighted implementation:
```py
def edge_exists(self, vertex_from: str, vertex_to: str) -> bool:
    if vertex_from in self.adjacency_list.keys():
        return vertex_to in self.adjacency_list[vertex_from]
    return False
```

Weighted implementation:
```py
def edge_exists(self, vertex_from: str, vertex_to: str) -> bool:
    if vertex_from in self.adjacency_list.keys():
        for neighbor, weight in self.adjacency_list[vertex_from]:
            if neighbor == vertex_to:
                return True
    return False
```

Note that the implementation became a little more complicated, as the adjacency list now stores two-element tuples, instead of only the neighbors.

`get_edges`:

Unweighted implementation:
```py
def get_edges(self) -> List[Tuple[str, str]]:
    edges = list()
    for vertex, neighbors in self.adjacency_list.items():
        for neighbor in neighbors:
            edges.append((vertex, neighbor))
    return edges
```

Weighted implementation:
```py
def get_edges(self) -> List[Tuple[str, str, int]]:
    edges = list()
    for vertex, neighbors in self.adjacency_list.items():
        for neighbor, weight in neighbors:
            edges.append((vertex, neighbor, weight))
    return edges
```

Again, an edge is not a `(vertex_from, vertex_to)` two-element tuple anymore, but a `(vertex_from, vertex_to, weight)` three-element tuple.

The functions `add_vertex` and `get_vertices` don't need to be modified, and `get_neighbors` is also the same, but the return type is changed. The complete implementation, including the `get_edge_weight` method is as follows:

```py
class WeightedAdjacencyListGraph(WeightedGraph):
    def __init__(self, undirected: bool = False) -> None:
        super().__init__(undirected)
        self.adjacency_list = dict()

    def add_vertex(self, vertex_id: str) -> None:
        if vertex_id not in self.adjacency_list.keys():
            self.adjacency_list[vertex_id] = list()

    def add_edge(self, vertex_from: str, vertex_to: str, weight: int) -> None:
        # Add the vertices if they are not already in the graph
        self.add_vertex(vertex_from)
        self.add_vertex(vertex_to)

        # Check if the edge is not a duplicate and add it
        if not self.edge_exists(vertex_from, vertex_to):
            self.adjacency_list[vertex_from].append((vertex_to, weight))

        # In undirected graphs, the existence of the edge u -> v means the the
        # edge v -> u also exists
        if self.undirected and not self.edge_exists(vertex_to, vertex_from):
            self.adjacency_list[vertex_to].append((vertex_from, weight))

    def get_vertices(self) -> List[str]:
        return list(self.adjacency_list.keys())

    def get_neighbors(self, vertex_id: str) -> List[Tuple[str, int]]:
        if vertex_id in self.adjacency_list.keys():
            return self.adjacency_list[vertex_id]
        raise ValueError(f"Vertex {vertex_id} is not in the graph!")

    def edge_exists(self, vertex_from: str, vertex_to: str) -> bool:
        if vertex_from in self.adjacency_list.keys():
            for neighbor, weight in self.adjacency_list[vertex_from]:
                if neighbor == vertex_to:
                    return True
        return False

    def get_edges(self) -> List[Tuple[str, str, int]]:
        edges = list()
        for vertex, neighbors in self.adjacency_list.items():
            for neighbor, weight in neighbors:
                edges.append((vertex, neighbor, weight))
        return edges

    def get_edge_weight(self, vertex_from: str, vertex_to: str) -> int:
        if self.edge_exists(vertex_from, vertex_to):
            for neighbor, weight in self.adjacency_list[vertex_from]:
                if neighbor == vertex_to:
                    return weight
        else:
            raise ValueError(f"The edge {vertex_from} -> {vertex_to} is not "
                             "in the graph!")
```

---

### Exercise 3

Run Kruskal's algorithm (first without implementing it) on the following graph. Describe the greedy choice and its related implementation.

![MST exercise graph](https://raw.githubusercontent.com/Erasiel/algds-eng/refs/heads/main/exercises/10_mst_sp/img/10_mst_sp_exercise03.svg)

### Solution

The sorted order of edges, and whether they are selected into the minimum spanning tree is as follows:

|  Edge  | Weight | In the MST? |
|:------:|:------:|:-----------:|
| B -- D |    1   |      ✓      |
| E -- G |    1   |      ✓      |
| A -- D |    2   |      ✓      |
| C -- E |    2   |      ✓      |
| A -- B |    3   |      ✗      |
| D -- E |    3   |      ✓      |
| B -- E |    4   |      ✗      |
| D -- F |    4   |      ✓      |
| E -- G |    4   |      ✗      |
| E -- H |    5   |      ✓      |
| C -- H |    6   |      ✗      |

The greedy choice is quite simple: select the edge into the MST that connects two different components (trees) with the lowest cost, until only one component (tree) remains.

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


def kruskal_mst(graph: WeightedGraph) -> List[Tuple[str, str, int]]:
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

### Solution

The implementation is quite simple:

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


def edge_weight(edge: Tuple[str, str, int]) -> int:
    """Returns the weight of a weighted edge."""
    return edge[2]


def filter_duplicate_edges(edges: List[Tuple[str, str, int]]
) -> List[Tuple[str, str, int]]:
    """Filters duplicate undirected edges."""
    unique_edges = []
    for edge in edges:
        vertex_from, vertex_to, weight = edge
        if not ((vertex_from, vertex_to, weight) in unique_edges or
                (vertex_to, vertex_from, weight) in unique_edges):
            unique_edges.append(edge)
    return unique_edges


def kruskal_mst(graph: WeightedGraph) -> List[Tuple[str, str, int]]:
    # Create a disjoint set (union-find) data structure for managing the
    # different trees
    trees = DisjointSet()

    # Initially, every vertex is in its own, one-element tree
    for vertex in graph.get_vertices():
        trees.make_set(vertex)

    # Sort the edges by weight in ascending order
    # Note: since the graph is undirected, every edge will appear twice, i.e.
    # for the edge (u, v) with weight w, there will be an entry (u, v, w) and
    # another entry (v, u, w) in the ordered list. We filter these with the
    # filter_duplicate_edges function, but the algorithm is correct even
    # without this step.
    edges = filter_duplicate_edges(graph.get_edges())
    sorted_edges = sorted(edges, key=edge_weight)

    # Store the list of MST edges
    mst_edges = []

    # Traverse the edges in sorted order
    for edge in sorted_edges:

        # If the edge connects two different trees, add it to the MST and
        # unite these two trees in the disjoint set
        source, dest, weight = edge
        tree_1 = trees.find(source)
        tree_2 = trees.find(dest)

        if tree_1 != tree_2:
            mst_edges.append(edge)
            trees.union(tree_1, tree_2)

    # Return the edges of the MST
    return mst_edges
```

---

### Exercise 5

Run Prim's algorithm (first without implementing it) on the graph of Exercise 3. Start from vertex `H`. Describe the greedy choice and its related implementation.

### Solution

The edges are selected into the minimum spanning tree in the following order:

|    |  Edge  | Weight | Vertex added to the MST |
|:--:|:------:|:------:|:-----------------------:|
| 1. | H -- E |    5   |            E            |
| 2. | E -- G |    1   |            G            |
| 3. | E -- C |    2   |            C            |
| 4. | E -- D |    3   |            D            |
| 5. | D -- B |    1   |            B            |
| 6. | D -- A |    1   |            A            |
| 7. | G -- F |    4   |            F            |

In this case, the greedy choice is selecting the edge that connects a new vertex to the minimum spanning tree with the lowest weight.

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

### Solution

An undirected, weighted graph does not have a minimum spanning tree if it is not connected. To start the solution, let's create an unconnected graph using the `WeightedAdjacencyListGraph` implementation from Exercise 2:

```py
graph = WeightedAdjacencyListGraph(undirected=True)
graph.add_vertex("A")
graph.add_vertex("B")
graph.add_vertex("C")
graph.add_vertex("D")
graph.add_vertex("E")
graph.add_vertex("F")
graph.add_edge("A", "B", 1)
graph.add_edge("A", "C", 2)
graph.add_edge("B", "C", 3)
graph.add_edge("D", "E", 2)
graph.add_edge("D", "F", 1)
graph.add_edge("E", "F", 3)
```

This graph has two connected components, both with three vertices and three edges. By running *either* of the MST algorithms, we get the same list of edges, but this list is not a minimum spanning tree. We can see this by examining the *length* of the output list:

```py
len(prim_mst(graph, start_vertex="A")) # output: 4
len(kruskal_mst(graph))                # output: 4
```

We know upfront that if a graph has a minimum spanning tree, the MST should contain exactly $|V| - 1$ edges. However, both algorithms are cleverly written so that **they output the minimum spanning forest**, which happens to contain one tree if the graph is connected.

The takeaway from this exercise is that both algorithms work on graphs that are not connected, and if the number of edges found by either algorithm is less than $|V| - 1$, the graph is not connected, and therefore the minimum spanning forest found by either algorithm contains more than one tree.

As a final side note, in an extreme edge case, both algorithms can output an empty list. This is only possible if the graph has no edges between different vertices.

---

### Exercise 7

How can you define the shortest path between two vertices in a graph? What variants of the shortest path(s) problem do you know? Which algorithms solve which variant?

### Solution

The shortest path between two vertices can be defined in multiple ways, based on how we measure distance. Last week, we simply counted the number of edges on the path between two vertices as the distance between them (recall breadth-first search).

This week, we are looking at weighted graphs, where a natural way to measure the distance between two vertices is to sum the weights of the edges on the path from the starting vertex to the target vertex. With this definition, the shortest path from $u$ to $v$ is the path on which the sum of weights is minimal, or $\infty$ if there is no path from $u$ to $v$.

When it comes to the shortest paths problem, three variants come to mind:
1. $s-t$ shortest path problem: determine the shortest path from $s$ to $t$
2. Single-source shortest paths problem: determine the shortest paths from $s$ to all other vertices
3. All-pairs shortest paths problem: determine the shortest paths between all pairs of vertices

The lecture discusses three algorithms: Dijkstra's algorithm (which we will look at in detail) and the Bellman-Ford algorithm solve the single-source shortest paths problem, while the Floyd-Warshall algorithm solves the all-pairs shortest paths problem.

---

### Exercise 8

Run Dijkstra's algorithm (first without implementing it) on the following graph. Start from vertex `A`. Describe the greedy choice and its related implementation.

![SP exercise graph](https://raw.githubusercontent.com/Erasiel/algds-eng/refs/heads/main/exercises/10_mst_sp/img/10_mst_sp_exercise08.svg)

### Solution

The output of the algorithm is as follows:

| Vertex | Parent | Distance |
|:------:|:------:|:--------:|
|    A   |   NIL  |     0    |
|    B   |    A   |     3    |
|    C   |    B   |     5    |
|    D   |    A   |     7    |
|    E   |    B   |     8    |
|    F   |    C   |    13    |
|    G   |    F   |    14    |

The greedy choice is as follows: in every iteration, find the vertex with the lowest distance among the 'open' vertices. 'Close' this vertex and update its neighbors if a shorter path exists to them that runs through the newly closed vertex.

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

### Solution

A solution based on the implementation of Prim's algorithm is as follows:

```py
import math
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
    priqueue = PriorityQueue()

    # Initialize each vertex with infinite priority (distance) and no parent
    for vertex in graph.get_vertices():
        priqueue.insert(vertex, math.inf)
        distance[vertex] = math.inf
        parent[vertex] = None

    # Set the start vertex's priority (distance) to 0
    priqueue.set_priority(start_vertex, 0)
    distance[start_vertex] = 0

    # While the priority queue is not empty (i.e. there are 'open' vertices),
    # remove vertex with the lowest priority (distance), 'close' it, and relax
    # its 'open' neighbors
    while len(priqueue) > 0:

        # Remove the vertex with the lowest distance among 'open' vertices.
        # This operation 'closes' the vertex, which means we found the
        # shortest path to it.
        sp_vertex = priqueue.min()
        sp_vertex_distance = priqueue.get_priority(sp_vertex)
        priqueue.extract_min()

        # If the distance of this vertex is infinity, it cannot be reached
        # from the starting vertex. We ignore these vertices (in fact, we
        # could break out of the loop, as all subsequent 'open' vertices will
        # also have infinite distances as we are using a minimum priority
        # queue).
        if distance[sp_vertex] == math.inf:
            continue

        # Traverse the neighbors of the newly closed vertex
        for vertex, edge_weight in graph.get_neighbors(sp_vertex):

            # We only care about 'open' neighbors, a neighbor is 'closed' if
            # it is not in the priority queue
            if not vertex in priqueue: continue

            # If we find a shorter path to the neighbor, update its priority
            # (distance) and parent
            existing_distance = priqueue.get_priority(vertex)
            new_distance = sp_vertex_distance + edge_weight

            if new_distance < existing_distance:
                priqueue.set_priority(vertex, new_distance)
                parent[vertex] = sp_vertex
                distance[vertex] = new_distance

    # Return a dict of DijkstraOut objects
    # This is not strictly required, we could return the `parent` and
    # `distance` dictionaries instead
    return {v: DijkstraOut(parent[v], distance[v])
            for v in graph.get_vertices()}
```

---

### Exercise 10

Give an example graph on which Dijkstra's algorithm is *not* optimal. Why is this? When is the algorithm guaranteed to be optimal? When is it guaranteed to *not* be optimal? Describe sufficient conditions of the input graph for both cases.

### Solution

Dijkstra's algorithm will not give optimal results if a vertex is closed before the shortest path to it is found. You might be wondering how this is possible, after all, closing a vertex means the algorithm found the shortest path to it. The answer is simple: negative weights.

Take the following graph for example:

![Graph with a negative edge weight](https://raw.githubusercontent.com/Erasiel/algds-eng/refs/heads/main/exercises/solutions/img/10_mst_sp_exercise10_solutions_part01.svg)

If we run Dijkstra's algorithm from the vertex A, the shortest path it will find to D will have a distance of 7. The iterations of the algorithm in detail:
1. A is closed with a distance of 0. B's distance is updated to 4 and its parent to A, C's distance is updated to 9 and its parent to A.
2. B is closed with a distance of 4. D's distance is updated to 7 and its parent to B.
3. D is closed with a distance of 7.
4. C is closed with a distance of 9. D is not updated, as it was closed in an earlier iteration.

In reality, the shortest path to D is through C, and its distance should be 9 + (-5) = 4, but the algorithm closed this vertex before this path could have been discovered.

So we see that Dijkstra's algorithm *might not be optimal* if the graph contains negative weights. The algorithm is *guaranteed* to be optimal if all weights are non-negative.

However, Dijkstra's algorithm is still not *guaranteed* to not be optimal if the input graph has negative weights. As an example, the following graph has a negative weight, but Dijkstra's algorithm returns the optimal shortest paths for every vertex:

![Second graph with a negative edge weight](https://raw.githubusercontent.com/Erasiel/algds-eng/refs/heads/main/exercises/solutions/img/10_mst_sp_exercise10_solutions_part02.svg)

The condition that guarantees Dijkstra's algorithm to not be optimal is if the graph has a negative cycle. A negative cycle is a cycle in the graph in which the sum of the edges' weights is negative. Consider the following example:

![Graph with a negative cycle](https://raw.githubusercontent.com/Erasiel/algds-eng/refs/heads/main/exercises/solutions/img/10_mst_sp_exercise10_solutions_part03.svg)

In this graph, the B &rarr; C &rarr; D &rarr; B cycle is a negative cycle, as the edges' weigths sum to -1. In calculating the shortest paths from vertex A, we could traverse this cycle infinitely many times, making the distance of the shortest paths $-\infty$ to all vertices other than A.

However, if we ran Dijkstra's algorithm from vertex A, it would not return the correct shortest paths, because Dijkstra's algorithm closes a vertex once and does not reopen or revisit the same vertex again. Importantly, the Bellman-Ford algorithm (which is discussed in detail in the lecture) is designed to also find negative cycles in the graph.

To summarize, Dijkstra's algorithm is...
- guaranteed to be optimal if all edge weights are non-negative
- might not be optimal if there are negative edge weights (and is therefore incorrect)
- guaranteed to not be optimal if there is a negative cycle in the graph
