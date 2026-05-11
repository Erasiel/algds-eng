from typing import Any, Dict, List, Tuple


def add_vertex(G: Dict[Any, List[Any]], v: Any) -> None:
    if v not in G.keys(): G[v] = []


def add_edge(G: Dict[Any, List[Any]], u: Any, v: Any) -> None:
    # Note that this function only adds the directed edge u --> v
    # For an undirected edge, call both add_edge(u, v) and add_edge(v, u)
    # If u and/or v is not a vertex in the graph, this function also adds them
    # to the vertices
    if u not in G.keys():
        G[u] = [v]
    else:
        G[u].append(v)

    if v not in G.keys(): G[v] = []


def get_vertices(G: Dict[Any, List[Any]]) -> List[Any]:
    return list(G.keys())


def get_edges(G: Dict[Any, List[Any]]) -> List[Tuple[Any, Any]]:
    edges = []
    for u in G.keys():
        for v in G[u]:
            edges.append((u, v))
    return edges


def get_neighbors(G: Dict[Any, List[Any]], v: Any) -> List[Any]:
    return G[v]


if __name__ == "__main__":
    graph = dict()
    add_vertex(graph, "A")
    add_vertex(graph, "B")
    add_vertex(graph, "C")
    add_vertex(graph, "D")
    add_edge(graph, "A", "B")
    add_edge(graph, "B", "A")
    add_edge(graph, "A", "C")
    add_edge(graph, "B", "D")
    add_edge(graph, "C", "D")
    print(graph)
    print(f"The vertices of the graph: {get_vertices(graph)}")
    print(f"The edges of the graph: {get_edges(graph)}")
    print(f"The neighbors of A in the graph: {get_neighbors(graph, "A")}")
    print(f"The neighbors of D in the graph: {get_neighbors(graph, "D")}")