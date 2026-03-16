# Name: Chester the Tester
# Neptun: T3ST3R
# h-id: h000000


from typing import List


def biggest_square(mtx: List[List[int]]) -> int:
    # Create a 2D DP table where every position (i, j) contains the solution
    # of the subproblem 'what size is the largest square submatrix of ones
    # that has `mtx[i][j]`` as its bottom-right element?'
    n_rows = len(mtx)
    n_cols = len(mtx[0])
    dp_table = [[0] * n_cols for _ in range(n_rows)]

    # Set the max square size to 0 and adjust it when filling the DP-table
    max_square_size = 0

    # If a value in the first row is 1, its corresponding square size is 1
    for j in range(n_cols):
        if mtx[0][j] == 1:
            dp_table[0][j] = 1
            if max_square_size == 0: max_square_size = 1

    # If a value in the first column is 1, its corresponding square size is 1
    for i in range(n_rows):
        if mtx[i][0] == 1:
            dp_table[i][0] = 1
            if max_square_size == 0: max_square_size = 1

    # Second row, second column onwards
    for i in range(1, n_rows):
        for j in range(1, n_cols):

            # `mtx[i][j]` can only be the bottom-right corner of a square of
            # ones if its value is 1.
            if mtx[i][j] == 1:

                # The size of the square is given by the minimum of sizes of
                # squares that end at (i-1, j), (i, j-1) and (i-1, j-1),
                # increased by 1 to account for the 1 at the current index.
                dp_table[i][j] = min(dp_table[i - 1][j],
                                     dp_table[i][j - 1],
                                     dp_table[i - 1][j - 1]) + 1

                # If the current square size is larger than the previous max,
                # update the max square size. We can skip this and instead
                # look up the maximum value in the DP table at the end, but
                # this is more efficient
                if dp_table[i][j] > max_square_size:
                    max_square_size = dp_table[i][j]

    return max_square_size


if __name__ == "__main__":
    import traceback

    output = None

    # TEST #1
    try:
        output = biggest_square([[1]])
        assert output == 1
        print("Test #1 passed!")
    except AssertionError:
        print(f"Test #1 failed! Expected output: 1, actual output: {output}")
    except Exception as exception:
        print(f"The following exception occured during Test #1:\n{exception}")
        traceback.print_exc()

    # TEST #2
    try:
        output = biggest_square([[0]])
        assert output == 0
        print("Test #2 passed!")
    except AssertionError:
        print(f"Test #2 failed! Expected output: 0, actual output: {output}")
    except Exception as exception:
        print(f"The following exception occured during Test #2:\n{exception}")
        traceback.print_exc()

    # TEST #3
    try:
        output = biggest_square([[1, 0, 1],
                                 [0, 1, 0],
                                 [1, 0, 1]])
        assert output == 1
        print("Test #3 passed!")
    except AssertionError:
        print(f"Test #3 failed! Expected output: 1, actual output: {output}")
    except Exception as exception:
        print(f"The following exception occured during Test #3:\n{exception}")
        traceback.print_exc()

    # TEST #4
    try:
        output = biggest_square([[1, 1, 1],
                                 [1, 1, 1],
                                 [1, 1, 0]])
        assert output == 2
        print("Test #4 passed!")
    except AssertionError:
        print(f"Test #4 failed! Expected output: 2, actual output: {output}")
    except Exception as exception:
        print(f"The following exception occured during Test #4:\n{exception}")
        traceback.print_exc()
