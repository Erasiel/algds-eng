from typing import List


def num_islands(map: List[List[int]]) -> int:
    # Treat the problem like a graph problem: land tiles are vertices that are
    # connected by undirected edges if they are connected on the map. Then,
    # the number of islands is given by the number of components DFS discovers.

    # Get the size of the map
    n_rows = len(map)
    n_cols = len(map[0])

    def _dfs_helper(map: List[List[int]], row_idx: int, col_idx: int) -> None:
        # We only need to mark visited positions on the map, no need to track
        # discovery and finish times. We'll mark visited positions by setting
        # their values to -1.
        map[row_idx][col_idx] = -1

        # Find unvisited neighbors and continue traversal
        # Pay attention to indexing
        if row_idx + 1 < n_rows and map[row_idx + 1][col_idx] > 0:
            _dfs_helper(map, row_idx + 1, col_idx)
        if row_idx - 1 >= 0 and map[row_idx - 1][col_idx] > 0:
            _dfs_helper(map, row_idx - 1, col_idx)
        if col_idx + 1 < n_cols and map[row_idx][col_idx + 1] > 0:
            _dfs_helper(map, row_idx, col_idx + 1)
        if col_idx - 1 >= 0 and map[row_idx][col_idx - 1] > 0:
            _dfs_helper(map, row_idx, col_idx - 1)

    # Set the initial number of islands as 0
    n_islands = 0

    # Perform DFS on the map. Finding an unvisited land tile means a new
    # island is found, and we need to mark all of its tiles using depth first
    # traversal.
    for i in range(n_rows):
        for j in range(n_cols):
            if map[i][j] > 0:
                n_islands += 1
                _dfs_helper(map, i, j)

    # Return the number of islands
    return n_islands


if __name__ == "__main__":
    output = None

    # TEST #1
    try:
        output = num_islands([[1]])
        assert output == 1
        print("Test #1 passed!")
    except AssertionError:
        print(f"Test #1 failed! Expected output: 1, actual output: {output}")
    except Exception as exception:
        print(f"The following exception occured during Test #1:\n{exception}")

    # TEST #2
    try:
        output = num_islands([[0]])
        assert output == 0
        print("Test #2 passed!")
    except AssertionError:
        print(f"Test #2 failed! Expected output: 0, actual output: {output}")
    except Exception as exception:
        print(f"The following exception occured during Test #2:\n{exception}")

    # TEST #3
    try:
        output = num_islands([[0, 1],
                              [1, 0]])
        assert output == 2
        print("Test #3 passed!")
    except AssertionError:
        print(f"Test #3 failed! Expected output: 2, actual output: {output}")
    except Exception as exception:
        print(f"The following exception occured during Test #3:\n{exception}")

    # TEST #4
    try:
        output = num_islands([[1, 1],
                              [0, 1]])
        assert output == 1
        print("Test #4 passed!")
    except AssertionError:
        print(f"Test #4 failed! Expected output: 1, actual output: {output}")
    except Exception as exception:
        print(f"The following exception occured during Test #4:\n{exception}")

    # TEST #5
    try:
        output = num_islands([[4, 3, 0, 3, 2, 3],
                              [2, 1, 0, 0, 2, 1],
                              [0, 0, 1, 2, 0, 0],
                              [0, 0, 0, 1, 0, 1],
                              [3, 2, 0, 0, 0, 2]])
        assert output == 5
        print("Test #5 passed!")
    except AssertionError:
        print(f"Test #5 failed! Expected output: 5, actual output: {output}")
    except Exception as exception:
        print(f"The following exception occured during Test #5:\n{exception}")
