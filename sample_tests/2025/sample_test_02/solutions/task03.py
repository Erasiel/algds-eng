from abc import ABC, abstractmethod
from typing import List, Tuple

# The design of the algorithm is as follows:
# Run depth-first search (DFS) on the input graph. When we traverse the
# neighbors of a vertex in DFS-Visit, if the neighbor's color is gray, the
# edge to this neighbor is a "back-edge". The graph contains a circle if and
# only if it contains a back-edge.


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


def _contains_circle_dfs(graph: Graph) -> bool:
    """Modified DFS that checks if the graph contains a circle."""

    def _find_circle_dfs(graph: Graph, vertex: str) -> bool:
        """Performs depth-first traversal from the given vertex."""

        # Entering the vertex by setting its color to gray
        color[vertex] = "gray"
        circle_found = False

        for n in graph.get_neighbors(vertex):
            # If we find a gray neighbor, we found a back-edge, which means
            # there is a circle in the graph
            if color[n] == "gray":
                return True

            # Continue DFS by visiting white neighbors and checking if a
            # circle can be found from them
            if color[n] == "white":
                circle_found = _find_circle_dfs(graph, n)

        # Leaving the vertex by setting its color to black
        color[vertex] = "black"
        return circle_found

    # We only need to store a vertex's color, no need for discovered, finished
    # and time
    color = dict()

    # Initialize all vertices with the color white
    for v in graph.get_vertices():
        color[v] = "white"

    # DFS "outer loop": perform DFS-visit on all white vertices
    for v in graph.get_vertices():
        if color[v] == "white":

            # If we find a circle while visiting a vertex, return True
            circle_found = _find_circle_dfs(graph, v)
            if circle_found:
                return True

    # If the outer loop is complete and no circles were found, return False
    return False


def contains_circle(graph: Graph) -> bool:
    return _contains_circle_dfs(graph)


if __name__ == "__main__":
    graph = AdjacencyListGraph(undirected=False)
    graph.add_vertex("A")
    graph.add_vertex("B")
    graph.add_vertex("C")
    assert not contains_circle(graph)

    graph = AdjacencyListGraph(undirected=False)
    graph.add_vertex("A")
    graph.add_vertex("B")
    graph.add_vertex("C")
    graph.add_edge("A", "B")
    graph.add_edge("A", "C")
    graph.add_edge("B", "C")
    assert not contains_circle(graph)

    graph = AdjacencyListGraph(undirected=False)
    graph.add_vertex("A")
    graph.add_vertex("B")
    graph.add_vertex("C")
    graph.add_edge("A", "B")
    graph.add_edge("B", "C")
    graph.add_edge("C", "A")
    assert contains_circle(graph)
