from typing import List


def matmul(mat1: List[List[float]],
           mat2: List[List[float]]
) -> List[List[float]]:
    # TODO
    pass


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
