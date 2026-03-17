from typing import List


class Item:
    def __init__(self, value: int, weight: int) -> None:
        self.value = value
        self.weight = weight


def knapsack(C: int, items: List[Item]) -> int:
    # Create a 2D DP table where every position (i, j) contains the solution
    # of the subproblem 'what is the solution to the 0-1 knapsack problem for
    # a knapsack with capacity `j`, and the first `i` items?'
    n_rows = len(items) + 1
    n_cols = C + 1
    dp_table = [[0] * n_cols for _ in range(n_rows)]

    # Base case (first row): with 0 items, only 0 value can be obtained
    # regardless of the capacity of the knapsack. This is handled by the
    # initialization.

    # Second row onwards
    for i in range(1, n_rows):
        # The current item, introduced in the i-th row, is not available in
        # previous rows
        current_item = items[i - 1]

        # The extreme case of an item with 0 weight is handled by starting the
        # column index (which stands for the capacity of the knapsack) from 0.
        for j in range(0, n_cols):

            # We cannot use the current item
            if j < current_item.weight:
                dp_table[i][j] = dp_table[i - 1][j]

            # If we can use the current item, we have to figure out whether it
            # is actually beneficial to use it.
            else:
                not_using = dp_table[i - 1][j]
                using = dp_table[i - 1][j - current_item.weight] + \
                        current_item.value

                dp_table[i][j] = max(not_using, using)

    return dp_table[-1][-1]


if __name__ == "__main__":
    output = None

    # TEST #1
    try:
        output = knapsack(C=3, items=[Item(value=2, weight=1),
                                      Item(value=3, weight=2),
                                      Item(value=4, weight=3)])
        assert output == 5
        print("Test #1 passed!")
    except AssertionError:
        print(f"Test #1 failed! Expected output: 5, actual output: {output}")
    except Exception as exception:
        print(f"The following exception occured during Test #1:\n{exception}")

    # TEST #2
    try:
        output = knapsack(C=12, items=[Item(value=5, weight=3),
                                       Item(value=4, weight=4),
                                       Item(value=5, weight=2),
                                       Item(value=5, weight=6),
                                       Item(value=4, weight=5)])
        assert output == 15
        print("Test #2 passed!")
    except AssertionError:
        print(f"Test #2 failed! Expected output: 15, actual output: {output}")
    except Exception as exception:
        print(f"The following exception occured during Test #2:\n{exception}")
