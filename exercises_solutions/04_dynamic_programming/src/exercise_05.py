from typing import List
import math


def min_change_2d(F: int, P: List[int]) -> int:
    # Create a 2D DP table where every position (i, j) contains the solution
    # of the subproblem 'what is the solution to the minimum change making
    # problem for `j` amount of money, and the first `i` coins in P?'
    n_rows = len(P) + 1
    n_cols = F + 1
    dp_table = [[0] * n_cols for _ in range(n_rows)]

    # Base case #1 (first column), i.e., 0 money can be exchanged to 0 coins,
    # is handled by the initialization.
    # Base case #2: first row (no usable coins): if the amount of money is
    # greater than 0, the change cannot be made. We use the `math.inf`, the
    # infinity constant to indicate this. As infinity + anything is infinity,
    # if the cange cannot be made, the algorithm will return infinity as well.
    for j in range(1, n_cols): dp_table[0][j] = math.inf

    # Second row, second column onwards
    for i in range(1, n_rows):

        # The current coin, introduced in the i-th row, is not available in
        # previous rows
        current_coin = P[i - 1]

        for j in range(1, n_cols):

            # If we cannot use the current coin, we must copy the previous row
            if j < current_coin:
                dp_table[i][j] = dp_table[i - 1][j]

            # If we can use the current coin, we have to figure out whether it
            # is actually beneficial to use it.
            else:
                dp_table[i][j] = min(dp_table[i - 1][j],
                                     dp_table[i][j - current_coin] + 1)

    return dp_table[-1][-1]


def min_change(F: int, P: List[int]) -> int:
    # The optimal algorithm uses only a 1D DP-table (one row) to simulate the
    # 2D DP-table, similar to Exercise 03. The logic is the same as in the 2D
    # case above.
    n_cols = F + 1
    dp_table = [math.inf] * n_cols
    dp_table[0] = 0

    for i in range(len(P)):
        current_coin = P[i]

        # Starting the loop from the current coin's value handles all cases
        # where the current coin cannot be used.
        for j in range(current_coin, n_cols):
            dp_table[j] = min(dp_table[j], dp_table[j - current_coin] + 1)

    return dp_table[-1]



if __name__ == "__main__":
    output = None

    # TEST #1
    try:
        output = min_change(10, [1, 2, 4, 6])
        assert output == 2
        print("Test #1 passed!")
    except AssertionError:
        print(f"Test #1 failed! Expected output: 2, actual output: {output}")
    except Exception as exception:
        print(f"The following exception occured during Test #1:\n{exception}")

    # TEST #2
    try:
        output = min_change(11, [1, 5, 7])
        assert output == 3
        print("Test #2 passed!")
    except AssertionError:
        print(f"Test #2 failed! Expected output: 3, actual output: {output}")
    except Exception as exception:
        print(f"The following exception occured during Test #2:\n{exception}")
