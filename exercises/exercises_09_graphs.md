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

How can we represent graphs? Describe and implement at least two distinct approaches by creating subclasses of the `Graph` abstract class in the snippet below. Assume all nodes are identified by a string (e.g. `"A"`, `"B"`, etc.) and the data structure implements a simple graph (i.e. a graph without duplicate edges or self-loops).

```py
from abc import ABC, abstractmethod


class Graph(ABC):
    def __init__(self, directed: bool = True) -> None:
        super().__init__()
        self.directed = directed

    @abstractmethod
    def add_node(self, node_id: str) -> None:
        raise NotImplementedError("Abstract class Graph does not implement "
                                  "add_node")

    @abstractmethod
    def add_edge(self, node_from: str, node_to: str) -> None:
        raise NotImplementedError("Abstract class Graph does not implement "
                                  "add_edge")

    @abstractmethod
    def edge_exists(self, node_from: str, node_to: str) -> bool:
        raise NotImplementedError("Abstract class Graph does not implement "
                                  "edge_exists")

    @abstractmethod
    def get_edges(self) -> Set[Tuple[str, str]]:
        raise NotImplementedError("Abstract class Graph does not implement "
                                  "get_edges")
```

When is one representation better than the other? Compare graph representations by implementing `edge_exists` and `get_edges` and analyzing their time complexity. `edge_exits` should determine whether a given edge exists in the graph, and `get_edges` should return the list of all edges in the graph.

---

### Exercise 3

Run breadth-first search (first without implementing it) on the following graph. Start from node `A`. What is the output of the algorithm?

![Directed graph](img/09_graphs_exercise03.svg)

---

### Exercise 4

Implement breadth-first search. Use the example of Exercise 3 for guidance and the outline below with one of the `Graph` subclasses from Exercise 2. The `BFSOut` type represents the properties of a node we compute with the algorithm. Feel free to use this type in tracking the properties of nodes during the algorithm. Extend the graph implementation with any public (or private) method if you deem it necessary.

```py
class BFSOut:
    def __init__(self, parent: str, dist: int, visited: bool) -> None:
        self.parent = parent
        self.dist = dist
        self.visited = visited


def breadth_first_search(graph: Graph, start_node: str) -> Dict[str, BFSOut]:
    # TODO
```

Check the correctness of your implementation on the graph of Exercise 3. Use the following code snippet to create the graph:

```py
# `graph` is an object of a subclass of Graph (Exercise 2)
graph.add_node("A")
graph.add_node("B")
graph.add_node("C")
graph.add_node("D")
graph.add_node("E")
graph.add_node("F")
graph.add_node("G")
graph.add_node("H")
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

### Exercise 5

Run depth-first search (first without implementing it) on the graph of Exercise 3. Assume that nodes and neighbors are ordered alphabetically. What is the output of the algorithm?

---

### Exercise 6

Implement depth-first search. Use the example of Exercise 3 for guidance and the outline below with one of the `Graph` subclasses from Exercise 2. The `DFSOut` type represents the properties of a node we compute with the algorithm. Feel free to use this type in tracking the properties of nodes during the algorithm. Extend the graph implementation with any public (or private) method if you deem it necessary.


```py
class DFSOut:
    def __init__(self,
                 parent: str,
                 discovered: int,
                 finished: int,
                 visited: bool
    ) -> None:
        self.parent = parent
        self.discovered = discovered
        self.finished = finished
        self.visited = visited


def depth_first_search(graph: Graph) -> Dict[str, DFSOut]:
    # TODO
```

---

### Exercise 7

Design and implement an algorithm that determines if a given ordering of a graph's nodes is a valid *topological sort* of the the graph. Use the outline below:

```py
def is_topological_sort(graph: Graph, nodes: List[str]) -> bool:
    # TODO
```

---

### Exercise 8

Design and implement an algorithm that determines a correct topological sort of a directed acyclic graph (DAG). Use the implementation of dept-first search from Exercise 6. You don't have to check whether the graph is truly a DAG.
