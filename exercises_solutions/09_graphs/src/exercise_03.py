import math
from typing import Any, Dict, List, Tuple
from collections import deque


def breadth_first_search(graph: Dict[Any, List[Any]],
                         start_vertex: Any
) -> Tuple[Dict[Any, int], Dict[Any, int]]:
    """BFS for a graph using the adjacency list representation.

    The implementation assumes that `start_vertex` is a vertex in the graph,
    and that all vertices in the neighbor lists also appear as vertices in the
    graph.

    Returns a tuple of two dictionaries, the first containing the distances of
    all vertices from the starting vertex, and the second containing the
    parent of each vertex on the shortest path to them from the starting
    vertex.
    """

    distance = dict()
    parent = dict()
    visited = dict()

    # Mark every vertex as unvisited, set their parent to None and their
    # distance to infinity
    for v in graph.keys():
        visited[v] = False
        parent[v] = None
        distance[v] = math.inf

    # Mark the starting vertex as visited and set its distance to 0
    visited[start_vertex] = True
    distance[start_vertex] = 0

    # Initialize a queue and insert the starting vertex
    queue = deque()
    queue.append(start_vertex)

    # Repeat while the queue is not empty
    while len(queue) > 0:

        # Remove the first element of the queue
        v = queue.popleft()

        # Mark every unvisited neighbor as visited, update their distance and
        # parent, and add them to the queue
        for n in graph[v]:
            if not visited[n]:
                visited[n] = True
                distance[n] = distance[v] + 1
                parent[n] = v
                queue.append(n)

    # Return the distances and parents of every vertex
    return distance, parent


if __name__ == "__main__":
    graph = {
        "A": ["B", "C"],
        "B": ["D"],
        "C": ["D", "E", "F"],
        "D": ["H"],
        "E": ["F"],
        "F": ["D"],
        "G": ["I", "H"],
        "H": [],
        "I": ["H"],
    }
    bfs_distances, bfs_parents = breadth_first_search(graph, "A")
    print(f"Distances: {bfs_distances}")
    print(f"Parents: {bfs_parents}")
