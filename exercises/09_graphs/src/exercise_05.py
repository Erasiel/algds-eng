import math
from typing import Any, Dict
from collections import deque

from exercise_03 import Graph, AdjacencyListGraph


class Queue:
    def __init__(self):
        self.queue = deque()

    def enqueue(self, x: Any) -> None:
        self.queue.extend(x)

    def dequeue(self) -> Any:
        return self.queue.popleft()

    def first(self) -> Any:
        return self.queue[0]

    def __len__(self) -> int:
        return len(self.queue)


class BFSOut:
    def __init__(self, parent: str, dist: int) -> None:
        self.parent = parent
        self.dist = dist


def breadth_first_search(graph: Graph, start_vertex: str) -> Dict[str, BFSOut]:
    distance = dict()
    parent = dict()

    # TODO

    # Return a dict of BFSOut objects
    # This is not strictly required, we could return the `parent` and
    # `distance` dictionaries instead
    return {v: BFSOut(parent[v], distance[v]) for v in graph.get_vertices()}


if __name__ == "__main__":
    # Exercise 4
    graph = AdjacencyListGraph()
    graph.add_vertex("A")
    graph.add_vertex("B")
    graph.add_vertex("C")
    graph.add_vertex("D")
    graph.add_vertex("E")
    graph.add_vertex("F")
    graph.add_vertex("G")
    graph.add_vertex("H")
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

    bfs_output = breadth_first_search(graph, "A")
    print("BFS output:")
    for node in graph.get_vertices():
        print(f"{node}:\t"
              f"parent: {bfs_output[node].parent}\t"
              f"distance: {bfs_output[node].dist}")
