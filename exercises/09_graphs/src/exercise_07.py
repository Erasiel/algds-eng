from typing import Dict

from exercise_03 import Graph, AdjacencyListGraph


class DFSOut:
    def __init__(self,
                 parent: str,
                 discovered: int,
                 finished: int,
                 visited: bool
    ) -> None:
        self.parent = parent
        self.discovered = discovered
        self.finished = finished
        self.visited = visited


def depth_first_search(graph: Graph) -> Dict[str, DFSOut]:
    # TODO
    pass


if __name__ == "__main__":
    # Exercise 6
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

    bfs_output = depth_first_search(graph)
    print("BFS output:")
    for node in graph.get_vertices():
        print(f"{node}:\t"
              f"parent:{bfs_output[node].parent}\t"
              f"discovered: {bfs_output[node].discovered}\t"
              f"finished: {bfs_output[node].finished}")

