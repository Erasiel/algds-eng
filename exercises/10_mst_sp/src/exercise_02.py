from abc import ABC, abstractmethod
from typing import List, Tuple


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


class WeightedAdjacencyListGraph(WeightedGraph):
    def __init__(self, undirected: bool = False) -> None:
        super().__init__(undirected)
        self.adjacency_list = dict()

    def add_vertex(self, vertex_id: str) -> None:
        if vertex_id not in self.adjacency_list.keys():
            self.adjacency_list[vertex_id] = list()

    def add_edge(self, vertex_from: str, vertex_to: str, weight: int) -> None:
        # TODO

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

    def get_neighbors(self, vertex_id: str) -> List[Tuple[str, int]]:
        if vertex_id in self.adjacency_list.keys():
            return self.adjacency_list[vertex_id]
        raise ValueError(f"Vertex {vertex_id} is not in the graph!")

    def edge_exists(self, vertex_from: str, vertex_to: str) -> bool:
        # TODO

        if vertex_from in self.adjacency_list.keys():
            return vertex_to in self.adjacency_list[vertex_from]
        return False

    def get_edges(self) -> List[Tuple[str, str, int]]:
        # TODO

        edges = list()
        for vertex, neighbors in self.adjacency_list.items():
            for neighbor in neighbors:
                edges.append((vertex, neighbor))
        return edges

    def get_edge_weight(self, vertex_from: str, vertex_to: str) -> int:
        # TODO
        pass


if __name__ == "__main__":
    # Test 1: directed graph
    # A --5--> B --7-> C
    print("Directed graph:")
    graph = WeightedAdjacencyListGraph()
    graph.add_vertex("A")
    graph.add_vertex("B")
    graph.add_vertex("C")
    graph.add_edge("A", "B", 5)
    graph.add_edge("B", "C", 7)
    print(f"A's neighbors: {graph.get_neighbors('A')}")
    print(f"B's neighbors: {graph.get_neighbors('B')}")
    print(f"C's neighbors: {graph.get_neighbors('C')}")
    print(f"The weight of the A -> B edge: {graph.get_edge_weight('A', 'B')}")
    print(f"The weight of the B -> C edge: {graph.get_edge_weight('B', 'C')}")

    # Test 2: undirected graph
    # A --3-- B --4-- C
    print("Undirected graph:")
    graph = WeightedAdjacencyListGraph(undirected=True)
    graph.add_vertex("A")
    graph.add_vertex("B")
    graph.add_vertex("C")
    graph.add_edge("A", "B", 3)
    graph.add_edge("B", "C", 4)
    print(f"A's neighbors: {graph.get_neighbors("A")}")
    print(f"B's neighbors: {graph.get_neighbors("B")}")
    print(f"C's neighbors: {graph.get_neighbors("C")}")
    print(f"The weight of the A -- B edge: {graph.get_edge_weight('A', 'B')}")
    print(f"The weight of the B -- C edge: {graph.get_edge_weight('B', 'C')}")
