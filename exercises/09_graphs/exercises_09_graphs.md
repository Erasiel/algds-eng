# Graphs and Elementary Graph Algorithms

### Exercise 1

Define or briefly describe the following concepts:
- Graph
- Directed graph, undirected graph
- Connected graph, strongly connected graph
- Connected component, strongly connected component
- Weighted graph

---

### Exercise 2

How can we represent graphs? Describe at least two different approaches. Compare these representations by designing algorithms for the following problems and analysing their time complexities afterwards:
- For a vertex $u$, return a list of $u$'s neighbors
- For two vertices $u$ and $v$, checks if the edge $u \rightarrow v$ is in the graph
- Returns the list of all edges in the graph

Which is the most commonly used graph representation?

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

---

### Exercise 4

Run breadth-first search (first without implementing it) on the following graph. Start from vertex `A`. What is the output of the algorithm?

![Directed graph](img/09_graphs_exercise04.svg)

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

---

### Exercise 6

Run depth-first search (first without implementing it) on the graph of Exercise 3. Assume that vertices and their neighbors are ordered alphabetically. What is the output of the algorithm?

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

---

### Exercise 8

Design and implement an algorithm that determines if a given ordering of a graph's vertices is a valid *topological ordering* of the graph. Use the outline below:

```py
from typing import List


def is_topological_ordering(graph: Graph, ordered_vertices: List[str]) -> bool:
    # TODO
```

---

### Exercise 9

Design and implement an algorithm that determines a correct topological ordering of a directed acyclic graph (DAG). Use the implementation of dept-first search from Exercise 6. You don't have to check whether the graph is truly a DAG. Use the outline below:

```py
from typing import List


def topological_sort(graph: Graph) -> List[str]:
    # TODO
```

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
