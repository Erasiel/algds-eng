from typing import List

from exercise_03 import Graph, AdjacencyListGraph


def is_topological_ordering(graph: Graph, ordered_vertices: List[str]) -> bool:
    # Edge cases: the ordered list does not contain all vertices, or it contains
    # a vertex more than once

    # TODO
    pass


if __name__ == "__main__":
    # Graph 1:
    # A --> B --> C
    graph = AdjacencyListGraph()
    graph.add_vertex("A")
    graph.add_vertex("B")
    graph.add_vertex("C")
    graph.add_edge("A", "B")
    graph.add_edge("B", "C")
    try:
        assert is_topological_ordering(graph, ["A", "B", "C"])
        assert not is_topological_ordering(graph, ["A", "C", "B"])
        assert not is_topological_ordering(graph, ["B", "A", "C"])
        assert not is_topological_ordering(graph, ["B", "C", "A"])
        assert not is_topological_ordering(graph, ["C", "A", "B"])
        assert not is_topological_ordering(graph, ["C", "B", "A"])
        print("Test 1 succeeded")
    except:
        print("Test 1 failed!\n"
              "For the graph A --> B --> C, ['A', 'B', 'C'] is the only correct "
              "topological ordering")

    # Graph 2:
    # A --> B    C
    # note: C is isolated
    graph = AdjacencyListGraph()
    graph.add_vertex("A")
    graph.add_vertex("B")
    graph.add_vertex("C")
    graph.add_edge("A", "B")
    try:
        assert is_topological_ordering(graph, ["A", "B", "C"])
        assert is_topological_ordering(graph, ["C", "A", "B"])
        assert is_topological_ordering(graph, ["A", "C", "B"])
        assert not is_topological_ordering(graph, ["B", "A", "C"])
        assert not is_topological_ordering(graph, ["B", "C", "A"])
        assert not is_topological_ordering(graph, ["C", "B", "A"])
        print("Test 2 succeeded")
    except:
        print("Test 2 failed!\n"
              "For the graph A --> B    C,\n"
              "['A', 'B', 'C'], ['A', 'C', 'B'], and ['C', 'A', 'B'] "
              "are the only correct topological orderings")
