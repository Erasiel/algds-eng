from typing import List


def max_points(board: List[List[int]]) -> int:
    # TODO
    pass


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
