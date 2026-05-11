import math
from typing import Any, Dict, List, Tuple
from collections import deque


def depth_first_search(graph: Dict[Any, List[Any]]
) -> Tuple[Dict[Any, int], Dict[Any, int], Dict[Any, int]]:
    """DFS for a graph using the adjacency list representation.

    The implementation assumes that all vertices in the neighbor lists also appear as vertices in the graph.

    Returns a tuple of three dictionaries, the first containing the discovery
    times, the second the finishing times, and the third the parents of each
    vertex.
    """

    parent = dict()
    color = dict()
    discovery = dict()
    finish = dict()

    # Set the color of every vertex to white, their discovery and finish to 0
    # and their parent to None
    for v in graph.keys():
        color[v] = "white"
        parent[v] = None
        discovery[v] = 0
        finish[v] = 0

    # Create the timestamp variable and set it to 0
    T = 0

    # Define the recursive depth-first traversal
    def _depth_first_traversal(vertex: Any) -> None:
        nonlocal T

        # Increment T by 1
        T += 1

        # Set the parameter vertex's discovery to T and its color to gray
        discovery[vertex] = T
        color[vertex] = "gray"

        # Loop over all neighbors, if a neighbor is white, set its parent and
        # traverse it recursively
        for n in graph[vertex]:
            if color[n] == "white":
                parent[n] = vertex
                _depth_first_traversal(n)

        # Increment T by 1
        T += 1

        # Set the parameter vertex's finish to T and its color to black
        finish[vertex] = T
        color[vertex] = "black"

    # Loop over all vertices, if a vertex is white, traverse it
    for v in graph.keys():
        if color[v] == "white":
            _depth_first_traversal(v)

    return discovery, finish, parent


if __name__ == "__main__":
    graph = {
        "A": ["B", "D"],
        "B": ["C"],
        "C": ["D", "E", "F"],
        "D": ["H"],
        "E": ["F"],
        "F": ["D"],
        "G": ["I", "H"],
        "H": [],
        "I": ["H"],
    }
    dfs_discoveries, dfs_finishes, dfs_parents = depth_first_search(graph)
    print(f"Discoveries: {dfs_discoveries}")
    print(f"Finishes: {dfs_finishes}")
    print(f"Parents: {dfs_parents}")
