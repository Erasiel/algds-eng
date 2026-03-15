def board_recursive(n: int, m: int) -> int:
    if n == 1 or m == 1: return 1
    return board_recursive(n - 1, m) + board_recursive(n, m - 1)


def board(n: int, m: int) -> int:
    # Simulate filling the 2D DP table with just one row, starting with the
    # first row
    dp_table = [1] * m

    # Second row onwards...
    for _ in range(1, n):
        for j in range(1, m):
            # dp_table[j] = dp_table[j] + dp_table[j - 1] # Same as below
            dp_table[j] += dp_table[j - 1]

    return dp_table[-1]


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
