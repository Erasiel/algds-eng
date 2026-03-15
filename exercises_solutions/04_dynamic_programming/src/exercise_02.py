def board_recursive(n: int, m: int) -> int:
    if n == 1 or m == 1: return 1
    return board_recursive(n - 1, m) + board_recursive(n, m - 1)


def board(n: int, m: int) -> int:
    # By initializing the DP table with 1s, we can skip explicitly setting the
    # values of the base cases (first column and row).
    dp_table = [[1] * m for _ in range(n)]

    # Base cases - commented as the initialization takes care of these
    # First column
    # for i in range(n): dp_table[i][0] = 1

    # First row
    # for j in range(m): dp_table[0][j] = 1

    # Second row, second column onwards
    for i in range(1, n):
        for j in range(1, m):
            dp_table[i][j] = dp_table[i - 1][j] + dp_table[i][j - 1]

    return dp_table[-1][-1]

if __name__ == "__main__":
    output = None

    # TEST #1
    try:
        output = board(1, 1)
        assert output == 1
        print("Test #1 passed!")
    except AssertionError:
        print(f"Test #1 failed! Expected output: 1, actual output: {output}")
    except Exception as exception:
        print(f"The following exception occured during Test #1:\n{exception}")

    # TEST #2
    try:
        output = board(2, 2)
        assert output == 2
        print("Test #2 passed!")
    except AssertionError:
        print(f"Test #2 failed! Expected output: 2, actual output: {output}")
    except Exception as exception:
        print(f"The following exception occured during Test #2:\n{exception}")
