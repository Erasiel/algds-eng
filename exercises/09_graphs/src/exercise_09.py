from typing import List

from exercise_03 import Graph, AdjacencyListGraph
from exercise_08 import is_topological_ordering


def topological_sort(graph: Graph) -> List[str]:
    # TODO
    pass


if __name__ == "__main__":
    # TODO: Create graphs and test your algorithm using the implementation of
    # the `is_topological_ordering` algorithm from Exercise 8

    # Example:
    graph = AdjacencyListGraph()
    graph.add_vertex("A")
    graph.add_vertex("B")
    graph.add_vertex("C")
    graph.add_edge("A", "B")
    graph.add_edge("B", "C")
    assert is_topological_ordering(graph, topological_sort(graph))
