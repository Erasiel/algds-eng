# Graphs and Elementary Graph Algorithms - Solutions

### Exercise 1

Define or briefly describe the following concepts:
- Graph
- Directed graph, undirected graph
- Connected graph, strongly connected graph
- Connected component, strongly connected component
- Weighted graph

### Solution

A graph is a mathematical structure used to pairwise relations between objects. These objects are represented as vertices and the relations, or connections between these vertices are represented as edges. Graphs are typically denoted as an ordered pair $G = (V, E)$ where $V$ is the set of vertices and $E \subseteq V \times V$ is the set of edges. A graph without duplicate edges (also known as multiple edges) and self-loops is a *simple* graph.

In a directed graph, all edges have a specified direction, i.e. for $u, v \in V$, the edge $(u, v)$ represents a directed connection *from $u$ to $v$* (sometimes denoted as $u \rightarrow v$). In undirected graphs, an edge represents a connection that goes both ways, so an undirected edge between vertices $u$ and $v$ can be thought of (and is usually implemented as) the combination of the two directed edges $(u, v)$ and $(v, u)$.

An undirected graph is connected if there is a path between all pairs of vertices in the graph. A directed graph is strongly connected if there is a directed path between all pairs of vertices. Note that connected graphs are, by definition, also strongly connected.

A connected component is a connected subgraph within an undirected graph. A strongly connected component is a strongly connected subgraph within a directed graph. Again, connected components are, by definition, also strongly connected.

While both vertices and edges can contain many pieces of information, the most typical form of information attached to these objects is a *weight*. Weights are numbers whose meaning is always task-dependent. The term "weighted graph" typically refers to edge-weighted graphs.

---

### Exercise 2

How can we represent graphs? Describe at least two different approaches. Compare these representations by designing algorithms for the following problems and analysing their time complexities afterwards:
- For a vertex $u$, return a list of $u$'s neighbors
- For two vertices $u$ and $v$, checks if the edge $u \rightarrow v$ is in the graph
- Returns the list of all edges in the graph

Which is the most commonly used graph representation?

### Solution

The two most widely used graph representations are the adjacency list and adjacency matrix representations.

The adjacency list is a dictionary, where keys are vertices and values are lists of vertices. Each vertex's corresponding list contains its neighbors, i.e. the vertices it has a connection to.

The adjacency matrix is a $|V| \times |V|$ sized binary matrix, where each row and each column represent a vertex. The value in the $i^\text{th}$ row and the $j^\text{th}$ column represents whether the edge $v_i \rightarrow v_j$ is in the graph. Note that the adjacency matrix of an undirected graph is symmetrical.

As an example, consider the following graph:

![Example directed graph](https://raw.githubusercontent.com/Erasiel/algds-eng/refs/heads/main/exercises/solutions/img/09_graphs_exercise02_solutions.svg)

Its adjacency list representation is the following:
```py
{
    0: [1, 3],
    1: [2, 3]
    2: [],
    3: [1, 2]
}
```

Its adjacency matrix representation is the following:

```py
[[0, 1, 0, 1],
 [0, 0, 1, 1],
 [0, 0, 0, 0],
 [0, 1, 1, 0]]
```

Of course, both representations have their trade-offs, which can be demonstrated by analysing three specific methods with the following functionalities:

**1. For a vertex $u$, return a list of $u$'s neighbors**

The adjacency list implementation stores the neighbors directly (as $u$'s corresponding value). If our algorithm creates a copy of this list, its time complexity will be $\Theta(d_u)$, where $d_u$ is the *degree* of $u$ (in directed graphs, it is the *out-degree*).

With the adjacency matrix the algorithm would be quite simple: in the row of $u$, list all vertices whose column contains 1. The time complexity of this will be $\Theta(|V|)$.

**2. For two vertices $u$ and $v$, checks if the edge $u \rightarrow v$ is in the graph**

With the adjacency list this algorithm is a contains operation on $u$'s list and as such, its time complexity is $O(d_u)$ again.

The adjacency list stores this information directly, so the algorithm comes down to a simple indexing, whose time complexity is $O(1)$.

**3. Returns the list of all edges in the graph**

With the adjacency list this algorithm would have to traverse the list of all vertices and record every entry in each list. The number of traversed and recorded elements altogether would be $d_1 + d_2 + ... + d_{|V|}$, so the time complexity of this algorithm is $\sum_{i = 1}^{|V|}d_i = \Theta(|E|)$.

With the adjacency matrix we have no other choice than to traverse the entire matrix and record row-column entries where the value is 1. The running time of this algorithm is $\Theta(|V|^2)$

**Which one is better?**

While we cannot say either is outright better than the other, it is rare to see any representation other than the adjacency list. The most notable use case for the adjacency matrix is representing dense graphs, but in the general case, the adjacency list is preferred.

---

### Exercise 3

Implement the adjacency list representation by creating a subclass of the `Graph` abstract class in the code snippet below. Assume all vertices are identified by a string, and the data structure implements a *simple graph* (i.e. a graph without duplicate edges or self-loops).

```py
from abc import ABC, abstractmethod
from typing import Set, Tuple


class Graph(ABC):
    def __init__(self, undirected: bool = False) -> None:
        super().__init__()
        self.undirected = undirected

    @abstractmethod
    def add_vertex(self, vertex_id: str) -> None:
        raise NotImplementedError("Abstract class Graph does not implement "
                                  "add_vertex")

    @abstractmethod
    def add_edge(self, vertex_from: str, vertex_to: str) -> None:
        raise NotImplementedError("Abstract class Graph does not implement "
                                  "add_edge")

    @abstractmethod
    def get_vertices(self) -> List[str]:
        raise NotImplementedError("Abstract class Graph does not implement "
                                  "get_vertices")

    @abstractmethod
    def get_neighbors(self, vertex_id: str) -> List[str]:
        raise NotImplementedError("Abstract class Graph does not implement "
                                  "get_neighbors")

    @abstractmethod
    def edge_exists(self, vertex_from: str, vertex_to: str) -> bool:
        raise NotImplementedError("Abstract class Graph does not implement "
                                  "edge_exists")

    @abstractmethod
    def get_edges(self) -> List[Tuple[str, str]]:
        raise NotImplementedError("Abstract class Graph does not implement "
                                  "get_edges")
```

As further practice, implement the adjacency matrix representation similarly (create another `Graph` subclass, etc.).

### Solution

A fairly straightforward solution is as follows:

```py
class AdjacencyListGraph(Graph):
    def __init__(self, undirected: bool = False) -> None:
        super().__init__(undirected)
        self.adjacency_list = dict()

    def add_vertex(self, vertex_id: str) -> None:
        if vertex_id not in self.adjacency_list.keys():
            self.adjacency_list[vertex_id] = list()

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

    def get_vertices(self) -> List[str]:
        return list(self.adjacency_list.keys())

    def get_neighbors(self, vertex_id: str) -> List[str]:
        if vertex_id in self.adjacency_list.keys():
            return self.adjacency_list[vertex_id]
        raise ValueError(f"Vertex {vertex_id} is not in the graph!")

    def edge_exists(self, vertex_from: str, vertex_to: str) -> bool:
        if vertex_from in self.adjacency_list.keys():
            return vertex_to in self.adjacency_list[vertex_from]
        return False

    def get_edges(self) -> List[Tuple[str, str]]:
        edges = list()
        for vertex, neighbors in self.adjacency_list.items():
            for neighbor in neighbors:
                edges.append((vertex, neighbor))
        return edges
```

---

### Exercise 4

Run breadth-first search (first without implementing it) on the following graph. Start from vertex `A`. What is the output of the algorithm?

![Directed graph](https://raw.githubusercontent.com/Erasiel/algds-eng/refs/heads/main/exercises/09_graphs/img/09_graphs_exercise04.svg)

### Solution

The output of the algorithm is the following:

| Vertex | Parent | Distance |
|:------:|:------:|:--------:|
|    A   |   NIL  |     0    |
|    B   |    A   |     1    |
|    C   |    A   |     1    |
|    D   |    B   |     2    |
|    E   |    B   |     2    |
|    F   |    E   |     3    |
|    G   |   NIL  | $\infty$ |
|    H   |   NIL  | $\infty$ |

Note that there is no path from A to either G or H, so their distances are $\infty$. The distances of all other vertices represent the lengths of shortest paths (in the number of edges) from the starting vertex.

---

### Exercise 5

Using the outline below, implement breadth first search (BFS). Use the example of Exercise 4 and/or the lecture slides for guidance. The `BFSOut` type represents the properties of a vertex that are computed by the algorithm.

```py
from typing import Dict


class BFSOut:
    def __init__(self, parent: str, dist: int, visited: bool) -> None:
        self.parent = parent
        self.dist = dist


def breadth_first_search(graph: Graph, start_vertex: str) -> Dict[str, BFSOut]:
    distance = dict()
    parent = dict()

    # TODO

    # Return a dict of BFSOut objects
    # This is not strictly required, we could return the `parent` and
    # `distance` dictionaries instead
    return {v: BFSOut(parent[v], distance[v]) for v in graph.get_vertices()}
```

Check the correctness of your implementation on the graph of Exercise 3. Use the following code snippet to create the graph:

```py
# `graph` is an object of a subclass of Graph
# e.g. AdjacencyListGraph (Exercise 3)
graph = AdjacencyListGraph()
graph.add_vertex("A")
graph.add_vertex("B")
graph.add_vertex("C")
graph.add_vertex("D")
graph.add_vertex("E")
graph.add_vertex("F")
graph.add_vertex("G")
graph.add_vertex("H")
graph.add_edge("A", "B")
graph.add_edge("A", "C")
graph.add_edge("B", "D")
graph.add_edge("B", "E")
graph.add_edge("C", "E")
graph.add_edge("D", "C")
graph.add_edge("E", "F")
graph.add_edge("G", "F")
graph.add_edge("G", "H")
graph.add_edge("H", "F")
```

### Solution

An implementation of breadth first search that closely follows the book's pseudocode is as follows:

```py
import math
from typing import Dict


class BFSOut:
    def __init__(self, parent: str, dist: int, visited: bool) -> None:
        self.parent = parent
        self.dist = dist


def breadth_first_search(graph: Graph, start_vertex: str) -> Dict[str, BFSOut]:
    distance = dict()
    parent = dict()
    color = dict()

    # Initialize the properties of all vertices
    for v in graph.get_vertices():
        color[v] = "white"
        distance[v] = math.inf
        parent[v] = None

    # Initialize the properties of the starting vertex
    color[start_vertex] = "gray"
    distance[start_vertex] = 0

    # Create a queue and insert the starting starting
    vertex_queue = Queue()
    vertex_queue.enqueue(start_vertex)

    # While the queue is not empty, dequeue the first vertex and explore its
    # neighbors
    while len(vertex_queue) > 0:
        v = vertex_queue.dequeue()

        for n in graph.get_neighbors(v):

            # Unvisited neighbors are placed in the queue and their properties
            # are updated
            if color[n] == "white":
                vertex_queue.enqueue(n)
                color[n] = "grey"
                parent[n] = v
                distance[n] = distance[v] + 1

        # Mark the
        color[v] = "black"

    # Return a dict of BFSOut objects
    # This is not strictly required, we could return the `parent` and
    # `distance` dictionaries instead
    return {v: BFSOut(parent[v], distance[v]) for v in graph.get_vertices()}
```

---

### Exercise 6

Run depth-first search (first without implementing it) on the graph of Exercise 3. Assume that vertices and their neighbors are ordered alphabetically. What is the output of the algorithm?

### Solution

The output of the algorithm is the following:

| Vertex | Parent | Discovered | Finished |
|:------:|:------:|:----------:|:--------:|
|    A   |   NIL  |      1     |    12    |
|    B   |    A   |      2     |    11    |
|    C   |    D   |      4     |     9    |
|    D   |    B   |      3     |    10    |
|    E   |    C   |      5     |     8    |
|    F   |    E   |      6     |     7    |
|    G   |   NIL  |     13     |    16    |
|    H   |    G   |     14     |    15    |

Note that because of the "outer loop", all vertices are visited by the algorithm.

---

### Exercise 7

Using the outline below, implement depth first search (DFS). Use the example of Exercise 6 and/or the lecture slides for guidance. The `DFSOut` type represents the properties of a vertex that are computed by the algorithm.

```py
from typing import Dict


class DFSOut:
    def __init__(self, parent: str, discovered: int, finished: int) -> None:
        self.parent = parent
        self.discovered = discovered
        self.finished = finished


def depth_first_search(graph: Graph) -> Dict[str, DFSOut]:

    def dfs_visit(graph: Graph, vertex: str) -> None:
        # We want to reference and modify `time`, so we must mark it as a
        # not locally declared variable
        nonlocal time

        # TODO
        pass

    parent = dict()
    discovered = dict()
    finished = dict()

    # TODO

    # Return a dict of DFSOut objects
    # This is not strictly required, we could return the `parent` and
    # `distance` dictionaries instead
    return {v: DFSOut(parent[v], discovered[v], finished[v])
            for v in graph.get_vertices()}
```

### Solution

An implementation of depth first search that closely follows the book's pseudocode is as follows:

```py
from typing import Dict


class DFSOut:
    def __init__(self, parent: str, discovered: int, finished: int) -> None:
        self.parent = parent
        self.discovered = discovered
        self.finished = finished


def depth_first_search(graph: Graph) -> Dict[str, DFSOut]:

    def dfs_visit(graph: Graph, vertex: str) -> None:
        """Performs depth-first traversal from the given vertex."""

        # We have to refer to and update the `time` variable, so we must
        # declare it as nonlocal
        nonlocal time

        # When discovering a vertex, increase the time and set the properties
        # of the vertex
        time += 1
        discovered[vertex] = time
        color[vertex] = "gray"

        # Explore all neighbors and visit any undiscovered neighbors
        for n in graph.get_neighbors(vertex):
            if color[n] == "white":
                parent[n] = vertex
                dfs_visit(graph, n)

        # When leaving a vertex (finishing its visit), increase the time and
        # update the properties of the vertex
        time += 1
        finished[vertex] = time
        color[vertex] = "black"

    color = dict()
    parent = dict()
    discovered = dict()
    finished = dict()

    # Initialize the properties of all vertices
    for v in graph.get_vertices():
        color[v] = "white"
        parent[v] = None

    # Initially, set time to 0
    time = 0

    # The "outer loop" explores all undiscovered vertices
    for v in graph.get_vertices():
        if color[v] == "white":
            dfs_visit(graph, v)

    # Return a dict of DFSOut objects
    # This is not strictly required, we could return the `parent`,
    # `discovered`, and `finished` dictionaries instead
    return {v: DFSOut(parent[v], discovered[v], finished[v])
            for v in graph.get_vertices()}
```

---

### Exercise 8

Design and implement an algorithm that determines if a given ordering of a graph's vertices is a valid *topological ordering* of the graph. Use the outline below:

```py
from typing import List


def is_topological_ordering(graph: Graph, ordered_vertices: List[str]) -> bool:
    # TODO
```

### Solution

The topological ordering of a directed graph is an ordering of its vertices such that if $(u, v)$ is an edge in the graph, $u$ must precede $v$ in the ordering of the vertices. It is easy to see that only directed, acyclic graphs (DAGs) can be topologically sorted.

Knowing the definition, the algorithm has to check two conditions:
- All vertices are present in the ordering exactly once
- The definition of topological ordering holds

An example implementation:

```py
from typing import List


def is_topological_ordering(graph: Graph, ordered_vertices: List[str]) -> bool:
    # Condition 1: the sequence contains all vertices exactly once
    for v in graph.get_vertices():
        if v not in ordered_vertices:
            return False
    if len(ordered_vertices) != len(graph.get_vertices()):
        return False

    # Condition 2: the sequence conforms to the definition of topological
    # ordering
    for u, v in graph.get_edges():
        u_idx = ordered_vertices.index(u)
        v_idx = ordered_vertices.index(v)

        if u_idx >= v_idx:
            return False

    return True
```

---

### Exercise 9

Design and implement an algorithm that determines a correct topological ordering of a directed acyclic graph (DAG). Use the implementation of dept-first search from Exercise 6. You don't have to check whether the graph is truly a DAG. Use the outline below:

```py
from typing import List


def topological_sort(graph: Graph) -> List[str]:
    # TODO
```

### Solution

The algorithm for computing a topological ordering of a DAG is a simple modification of the depth first search (DFS) algorithm. Start with an empty list, run DFS on the graph and when the algorithm is finished with a vertex, insert that vertex into the start of the list. When DFS is done, return the list.

An example implementation:

```py
from typing import List


def topological_sort(graph: Graph) -> List[str]:
    def dfs_visit(graph: Graph, vertex: str) -> None:
        color[vertex] = "gray"

        for n in graph.get_neighbors(vertex):
            if color[n] == "white":
                dfs_visit(graph, n)

        # When leaving a vertex, add it to the start of the list
        color[vertex] = "black"
        topological_ordering.insert(0, vertex)

    # We only need the color information of each vertex
    color = dict()
    for v in graph.get_vertices():
        color[v] = "white"

    # Start with an empty list
    topological_ordering = list()

    # Standard DFS
    for v in graph.get_vertices():
        if color[v] == "white":
            dfs_visit(graph, v)

    return topological_ordering
```

Note: as per the description of the exercise, the algorithm does not check whether the input graph is truly a DAG.

---

### Exercise 10

The "Wikipedia game" is a famous game among students. All players start at the same randomly selected Wikipedia page and their goal is to reach a randomly selected destination page as quickly as possible. The only way to move from page A to page B is by clicking a link on page A that takes the player to page B. The player with the least moves from the starting page to the designated page wins the game.

You are given a list of Wikipedia pages and a list of links that can take you from page A to page B. Note that just because there exists a link on page A to page B, there might not exist a link on page B to page A. You are also given the starting and destination pages. Design and develop an algorithm that returns the optimal solution to the Wikipedia game (i.e. the lowest number of moves that takes the player to the destination page from the starting page). If the game cannot be completed, return -1.

Use the following outline:

```py
from typing import List, Tuple


def wikipedia_game(pages: List[str],
                   links: List[Tuple[str, str]],
                   start: str,
                   dest: str
) -> int:
    # TODO
```

Side note: web crawlers work in a similar way, but instead of knowing the list of links upfront, they discover links between pages "on-the-fly" as they visit them.

### Solution

If we think of this problem as a graph problem, then the task is to find the length of the shortest path (in the number of edges) from the starting page to the destination page. Conveniently, breadth-first search finds exactly this. Our job is quite simple: transform the input into a graph, run BFS from the starting vertex and report the distance of the destination vertex. The only edge case is when the game can't be completed, because there is no path from the starting page to the destination page. In this case, the distance will be `math.inf`, but the description specifies that we should return -1.

An example implementation, relying on the `AdjacencyListGraph` class from Exercise 3 and the `breadth_first_search` algorithm from Exercise 5 is as follows:

```py
from typing import List, Tuple
import math


def wikipedia_game(pages: List[str],
                   links: List[Tuple[str, str]],
                   start: str,
                   dest: str
) -> int:
    # Note: edges are directed, as specified in the description
    graph = AdjacencyListGraph(undirected=False)

    # The vertices are the pages
    for page in pages:
        graph.add_vertex(page)

    # The links are the edges
    for link_from, link_to in links:
        graph.add_edge(link_from, link_to)

    # Run BFS
    bfs_out = breadth_first_search(graph, start)

    # Check if the game can be completed
    if bfs_out[dest].dist < math.inf:
        return bfs_out[dest].dist
    else:
        return -1
```
