from typing import List, Tuple


def contains_circular_reference(references: List[Tuple[str, str]]) -> bool:
    # Build a graph of the directed edges
    graph = {}

    for cell_from, cell_to in references:
        if cell_from not in graph:
            graph[cell_from] = [cell_to]
        else:
            graph[cell_from].append(cell_to)

        if cell_to not in graph: graph[cell_to] = []

    # Run standard DFS on the graph and only monitor the color of the
    # vertices. If during the depth first traversal a node has a gray
    # neighbor, there is a circle in the graph.

    color = {vertex: "white" for vertex in graph.keys()}

    # Modified depth first traversal for circle detection. Note that the
    # function returns True if, along the traversal, it finds an edge that
    # forms a circle. Otherwise, it visits all white neighbors to look for a
    # circle.
    def _circle_detection_dfs(vertex: str) -> bool:

        # Set the color of the vertex to gray
        color[vertex] = "gray"

        # Loop over all neighbors
        for neighbor in graph[vertex]:

            # If a neighbor is gray, we found a circle
            if color[neighbor] == "gray":
                return True

            # Keep traversing white neighbors to look for a circle
            elif color[neighbor] == "white":
                if _circle_detection_dfs(neighbor):
                    return True

        # Set the color of the vertex to black
        color[vertex] = "black"

        # If the function returns here, it means we have not found a circle
        return False

    # DFS for circle detection. If during the traversal of any vertex a circle
    # is found, the algorithm returns True. Otherwise, there is no circle, the
    # loop completes and the algorithm returns False.
    for vertex in graph.keys():
        if color[vertex] == "white":
            has_circle = _circle_detection_dfs(vertex)
            if has_circle:
                return True

    return False

if __name__ == "__main__":

    import traceback

    output = None

    # TEST #1
    try:
        output = contains_circular_reference([("A1", "A2"),
                                              ("A2", "A3"),
                                              ("A3", "A4"),
                                              ("A4", "A5"),
                                              ("A5", "A6")])
        assert output == False
        print("Test #1 passed!")
    except AssertionError:
        print("Test #1 failed! Expected output: False, "
              f"actual output: {output}")
    except Exception as exception:
        print(f"The following exception occured during Test #1:\n{exception}")
        traceback.print_exc()

    # TEST #2
    try:
        output = contains_circular_reference([("A1", "A2"),
                                              ("A2", "A3"),
                                              ("A3", "A4"),
                                              ("A4", "A5"),
                                              ("A5", "A1")])
        assert output == True
        print("Test #2 passed!")
    except AssertionError:
        print("Test #2 failed! Expected output: True, "
              f"actual output: {output}")
    except Exception as exception:
        print(f"The following exception occured during Test #2:\n{exception}")
        traceback.print_exc()

    # TEST #3
    try:
        output = contains_circular_reference([])
        assert output == False
        print("Test #3 passed!")
    except AssertionError:
        print("Test #3 failed! Expected output: True, "
              f"actual output: {output}")
    except Exception as exception:
        print(f"The following exception occured during Test #3:\n{exception}")
        traceback.print_exc()
