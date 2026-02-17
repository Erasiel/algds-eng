from typing import List


def matrix_mean(matrix: List[List[float]]) -> float:
    # TODO
    pass


if __name__ == "__main__":
    output = None

    # TEST #1
    try:
        output = matrix_mean([[1]])
        assert output == 1.0
        print("Test #1 passed!")
    except AssertionError:
        print("Test #1 failed! "
              f"Expected output: 1.0, actual output: {output}")
    except Exception as exception:
        print(f"The following exception occured during Test #1:\n{exception}")

    # TEST #2
    try:
        output = matrix_mean([[1, 3]])
        assert output == 2.0
        print("Test #2 passed!")
    except AssertionError:
        print("Test #2 failed! "
              f"Expected output: 2.0, actual output: {output}")
    except Exception as exception:
        print(f"The following exception occured during Test #2:\n{exception}")

    # TEST #3
    try:
        output = matrix_mean([[1, 2, 3], [3, 4, 5]])
        assert output == 3.0
        print("Test #3 passed!")
    except AssertionError:
        print("Test #3 failed! "
              f"Expected output: 3.0, actual output: {output}")
    except Exception as exception:
        print(f"The following exception occured during Test #3:\n{exception}")
