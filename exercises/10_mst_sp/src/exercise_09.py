import math
from typing import Dict

from exercise_02 import WeightedGraph, WeightedAdjacencyListGraph
from exercise_06 import PriorityQueue


class DijkstraOut:
    def __init__(self, parent: str, dist: int) -> None:
        self.parent = parent
        self.dist = dist


def dijkstra_sssp(graph: WeightedGraph,
                  start_vertex: str
) -> Dict[str, DijkstraOut]:
    distance = dict()
    parent = dict()

    # TODO

    # Return a dict of DijkstraOut objects
    # This is not strictly required, we could return the `parent` and
    # `distance` dictionaries instead
    return {v: DijkstraOut(parent[v], distance[v])
            for v in graph.get_vertices()}


if __name__ == "__main__":
    graph = WeightedAdjacencyListGraph()
    graph.add_vertex("A")
    graph.add_vertex("B")
    graph.add_vertex("C")
    graph.add_vertex("D")
    graph.add_vertex("E")
    graph.add_vertex("F")
    graph.add_vertex("G")
    graph.add_edge("A", "B", 3)
    graph.add_edge("A", "D", 7)
    graph.add_edge("A", "E", 10)
    graph.add_edge("B", "C", 2)
    graph.add_edge("B", "E", 5)
    graph.add_edge("C", "F", 8)
    graph.add_edge("D", "E", 4)
    graph.add_edge("D", "G", 8)
    graph.add_edge("E", "G", 7)
    graph.add_edge("F", "E", 2)
    graph.add_edge("F", "G", 1)

    dijkstra_output = dijkstra_sssp(graph, "A")
    print("Dijkstra output:")
    for vertex in graph.get_vertices():
        print(f"{vertex}:\t"
              f"parent: {dijkstra_output[vertex].parent}\t"
              f"distance: {dijkstra_output[vertex].dist}")
