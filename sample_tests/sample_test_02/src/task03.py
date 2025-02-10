from abc import ABC, abstractmethod
from typing import Set, Tuple, Dict


class Graph(ABC):
    def __init__(self, undirected: bool = False) -> None:
        super().__init__()
        self.undirected = undirected

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

    @abstractmethod
    def get_nodes(self) -> Set[str]:
        raise NotImplementedError("Abstract class Graph does not implement "
                                  "get_nodes")

    @abstractmethod
    def get_neighbors(self, node_id: str) -> Set[str]:
        raise NotImplementedError("Abstract class Graph does not implement "
                                  "get_neighbors")


class GraphImpl(Graph):
    def __init__(self, undirected: bool = False):
        super().__init__(undirected)
        self.adjacency_list: Dict[str, Set[str]] = dict()

    def add_node(self, node_id: str) -> None:
        self.adjacency_list[node_id] = set()

    def add_edge(self, node_from: str, node_to: str) -> None:
        if node_to not in self.adjacency_list[node_from]:
            self.adjacency_list[node_from].add(node_to)
        if self.undirected and node_from not in self.adjacency_list[node_to]:
            self.adjacency_list[node_to].add(node_from)

    def edge_exists(self, node_from: str, node_to: str) -> bool:
        return node_to in self.adjacency_list[node_from]

    def get_nodes(self) -> Set[str]:
        return set(self.adjacency_list.keys())

    def get_edges(self) -> Set[Tuple[str, str]]:
        return {(n1, n2)
                for n1, n1_neighbors in self.adjacency_list.items()
                for n2 in n1_neighbors}

    def get_neighbors(self, node_id: str) -> Set[str]:
        return self.adjacency_list[node_id]


def contains_circle(graph: Graph) -> bool:
    # TODO
    pass


if __name__ == "__main__":
    graph = GraphImpl(undirected=False)
    graph.add_node("A")
    graph.add_node("B")
    graph.add_node("C")
    assert not contains_circle(graph)

    graph = GraphImpl(undirected=False)
    graph.add_node("A")
    graph.add_node("B")
    graph.add_node("C")
    graph.add_edge("A", "B")
    graph.add_edge("A", "C")
    graph.add_edge("B", "C")
    assert not contains_circle(graph)

    graph = GraphImpl(undirected=False)
    graph.add_node("A")
    graph.add_node("B")
    graph.add_node("C")
    graph.add_edge("A", "B")
    graph.add_edge("B", "C")
    graph.add_edge("C", "A")
    assert contains_circle(graph)
