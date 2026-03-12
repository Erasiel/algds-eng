from typing import List


def matmul(mat1: List[List[float]],
           mat2: List[List[float]]
) -> List[List[float]]:
    # Prepare the 2-dimensional output matrix
    n = len(mat1)
    result_matrix = [[0] * n for _ in range(n)]

    for i in range(n):
        for j in range(n):

            # Calculate `result_matrix[i][j]``, which is the inner product of
            # the i-th row of `mat1`, i.e., `mat1[i][:]`, and the j-th column
            # of `mat2`, i.e., `mat2[:][j]`
            inner_product = 0
            for k in range(n):
                inner_product += mat1[i][k] * mat2[k][j]
            result_matrix[i][j] = inner_product

    return result_matrix


if __name__ == "__main__":
    output = None

    # Test #1
    try:
        expected = [[1]]
        output = matmul([[.5]], [[2]])
        assert output == expected
        print("Test #1 passed!")
    except AssertionError:
        print("Test #1 failed! "
              f"Expected output: {expected}, actual output: {output}")
    except Exception as exception:
        print(f"The following exception occured during Test #1:\n{exception}")

    # Test #2
    try:
        expected = [[13, 16], [29, 36]]
        output = matmul([[1, 2], [3, 4]], [[3, 4], [5, 6]])
        assert output == expected
        print("Test #2 passed!")
    except AssertionError:
        print("Test #2 failed! "
              f"Expected output: {expected}, actual output: {output}")
    except Exception as exception:
        print(f"The following exception occured during Test #2:\n{exception}")
