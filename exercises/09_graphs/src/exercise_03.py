from abc import ABC, abstractmethod
from typing import List, Tuple


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


class AdjacencyListGraph(Graph):
    def __init__(self, undirected: bool = False) -> None:
        super().__init__(undirected)
        self.adjacency_list = dict()

    def add_vertex(self, vertex_id: str) -> None:
        # TODO
        pass

    def add_edge(self, vertex_from: str, vertex_to: str) -> None:
        # TODO
        pass

    def get_vertices(self) -> List[str]:
        # TODO
        pass

    def get_neighbors(self, vertex_id: str) -> List[str]:
        # TODO
        pass

    def edge_exists(self, vertex_from: str, vertex_to: str) -> bool:
        # TODO
        pass

    def get_edges(self) -> List[Tuple[str, str]]:
        # TODO
        pass


if __name__ == "__main__":
    # Test 1: directed graph
    # A -> B -> C
    print("Directed graph:")
    graph = AdjacencyListGraph()
    graph.add_vertex("A")
    graph.add_vertex("B")
    graph.add_vertex("C")
    graph.add_edge("A", "B")
    graph.add_edge("B", "C")
    print(f"A's neighbors: {graph.get_neighbors("A")}")
    print(f"B's neighbors: {graph.get_neighbors("B")}")
    print(f"C's neighbors: {graph.get_neighbors("C")}")

    # Test 2: undirected graph
    # A -- B -- C
    print("Undirected graph:")
    graph = AdjacencyListGraph(undirected=True)
    graph.add_vertex("A")
    graph.add_vertex("B")
    graph.add_vertex("C")
    graph.add_edge("A", "B")
    graph.add_edge("B", "C")
    print(f"A's neighbors: {graph.get_neighbors("A")}")
    print(f"B's neighbors: {graph.get_neighbors("B")}")
    print(f"C's neighbors: {graph.get_neighbors("C")}")