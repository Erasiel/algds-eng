import math
from typing import List, Tuple, Any

from exercise_02 import WeightedGraph, WeightedAdjacencyListGraph


class PriorityQueue:
    """Extremely simple priority queue implementation.

    This implementation uses a dictionary where keys are stored items and their
    priorities are their corresponding values. `insert` and `set_priority` are
    O(1), `get_priority`, `min`, and `extract_min` are O(n).
    """

    def __init__(self) -> None:
        self.elements = dict()

    def insert(self, key: Any, priority: int) -> None:
        if key not in self.elements:
            self.elements[key] = priority

    def set_priority(self, key: Any, priority: int) -> None:
        if key in self.elements:
            self.elements[key] = priority

    def get_priority(self, key) -> int:
        if key in self.elements:
            return self.elements[key]
        raise ValueError(f"The key {key} is not in the priority queue!")

    def min(self) -> Any:
        min_key, min_priority = next(iter(self.elements.items()))

        for key, priority in self.elements.items():
            if priority < min_priority:
                min_priority = priority
                min_key = key

        return min_key

    def extract_min(self) -> Any:
        min_key, min_priority = next(iter(self.elements.items()))

        for key, priority in self.elements.items():
            if priority < min_priority:
                min_priority = priority
                min_key = key

        self.elements.pop(min_key, None)

        return min_key

    def __contains__(self, item: Any) -> bool:
        return item in self.elements.keys()

    def __len__(self) -> int:
        return len(self.elements)


def prim_mst(graph: WeightedGraph,
             start_vertex: str
) -> List[Tuple[str, str, int]]:

    # Create a minimum priority queue for storing vertices where the priority of
    # a vertex is the cost of adding it to the MST. During the algorithm, the
    # priority of a vertex is the cost of adding that vertex to the MST.
    priqueue = PriorityQueue()

    # Store the parents of each vertex
    parent = dict()

    # Store the list of MST edges
    mst_edges = list()

    # Initialize each vertex with infinite priority and no parent
    for vertex in graph.get_vertices():
        priqueue.insert(vertex, math.inf)
        parent[vertex] = None

    # Set the start vertex's priority to 0
    priqueue.set_priority(start_vertex, 0)

    # Repeat the following until all vertices are added to the MST
    while len(priqueue) > 0:

        # The vertex with the lowest cost is the next to be added to the MST
        mst_vertex = priqueue.min()
        mst_edge_weight = priqueue.get_priority(mst_vertex)
        priqueue.extract_min()

        # If the vertex has a valid parent, add the corresponding edge to the
        # MST edges
        if parent[mst_vertex] is not None:
            mst_edges.append((parent[mst_vertex], mst_vertex, mst_edge_weight))

        # Iterate over the neighbors of the new MST vertex
        for vertex, edge_weight in graph.get_neighbors(mst_vertex):

            # We don't care about a neighbor that is already in the MST
            if not vertex in priqueue: continue

            # If the edge to the neighbor has a lower weight than the previous
            # lowest weight, update the neighbor
            found_weight = priqueue.get_priority(vertex)
            if edge_weight < found_weight:
                priqueue.set_priority(vertex, edge_weight)
                parent[vertex] = mst_vertex

    # Return the edges of the MST
    return mst_edges


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

    mst_edges = prim_mst(graph, start_vertex="H")
    print(mst_edges)
