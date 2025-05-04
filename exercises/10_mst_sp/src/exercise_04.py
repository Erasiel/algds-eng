from typing import List, Tuple

from exercise_02 import WeightedGraph, WeightedAdjacencyListGraph


class DisjointSet:
    """Extremely simple disjoint set (union-find) implementation."""

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
    pass


if __name__ == "__main__":
    graph = WeightedAdjacencyListGraph(undirected=True)
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

    mst_edges = kruskal_mst(graph)
    print(mst_edges)
