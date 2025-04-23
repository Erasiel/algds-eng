from typing import Dict

from exercise_03 import Graph, AdjacencyListGraph


class DFSOut:
    def __init__(self, parent: str, discovered: int, finished: int) -> None:
        self.parent = parent
        self.discovered = discovered
        self.finished = finished


def depth_first_search(graph: Graph) -> Dict[str, DFSOut]:

    def dfs_visit(graph: Graph, vertex: str) -> None:
        # We want to reference and modify `time`, so we must mark it as a
        # not locally declared variable:
        # nonlocal time

        # TODO
        pass

    parent = dict()
    discovered = dict()
    finished = dict()

    # TODO

    # Return a dict of DFSOut objects
    # This is not strictly required, we could return the `parent` and
    # `distance` dictionaries instead
    return {v: DFSOut(parent[v], discovered[v], finished[v])
            for v in graph.get_vertices()}


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
    print("DFS output:")
    for node in graph.get_vertices():
        print(f"{node}:\t"
              f"parent: {bfs_output[node].parent}\t"
              f"discovered: {bfs_output[node].discovered}\t"
              f"finished: {bfs_output[node].finished}")

