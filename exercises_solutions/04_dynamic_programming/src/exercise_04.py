from typing import List


def max_points(board: List[List[int]]) -> int:
    # Create a 2D DP table where every position (i, j) contains the solution
    # of the subproblem 'what is the maximum number of points we can collect
    # from the top-left corner to the (i, j) position in the input?'
    n_rows = len(board)
    n_cols = len(board[0])
    dp_table = [[0] * n_cols for _ in range(n_rows)]

    # Top-left corner
    dp_table[0][0] = board[0][0]

    # First column
    for i in range(1, n_rows):
        dp_table[i][0] = dp_table[i - 1][0] + board[i][0]

    # First row
    for j in range(1, n_cols):
        dp_table[0][j] = dp_table[0][j - 1] + board[0][j]

    # Second row, second column onwards...
    for i in range(1, n_rows):
        for j in range(1, n_cols):
            dp_table[i][j] = max(dp_table[i - 1][j], dp_table[i][j - 1]) + \
                             board[i][j]

    return dp_table[n_rows - 1][n_cols - 1]


if __name__ == "__main__":
    output = None

    # TEST #1
    try:
        output = max_points([[1]])
        assert output == 1
        print("Test #1 passed!")
    except AssertionError:
        print(f"Test #1 failed! Expected output: 1, actual output: {output}")
    except Exception as exception:
        print(f"The following exception occured during Test #1:\n{exception}")

    # TEST #2
    try:
        output = max_points([[1, 2, 3], [3, 1, 0]])
        assert output == 6
        print("Test #2 passed!")
    except AssertionError:
        print(f"Test #2 failed! Expected output: 6, actual output: {output}")
    except Exception as exception:
        print(f"The following exception occured during Test #2:\n{exception}")
