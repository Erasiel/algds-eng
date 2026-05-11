from typing import List


def num_islands(map: List[List[int]]) -> int:
    # TODO
    pass


if __name__ == "__main__":
    output = None

    # TEST #1
    try:
        output = num_islands([[1]])
        assert output == 1
        print("Test #1 passed!")
    except AssertionError:
        print(f"Test #1 failed! Expected output: 1, actual output: {output}")
    except Exception as exception:
        print(f"The following exception occured during Test #1:\n{exception}")

    # TEST #2
    try:
        output = num_islands([[0]])
        assert output == 0
        print("Test #2 passed!")
    except AssertionError:
        print(f"Test #2 failed! Expected output: 0, actual output: {output}")
    except Exception as exception:
        print(f"The following exception occured during Test #2:\n{exception}")

    # TEST #3
    try:
        output = num_islands([[0, 1],
                              [1, 0]])
        assert output == 2
        print("Test #3 passed!")
    except AssertionError:
        print(f"Test #3 failed! Expected output: 2, actual output: {output}")
    except Exception as exception:
        print(f"The following exception occured during Test #3:\n{exception}")

    # TEST #4
    try:
        output = num_islands([[1, 1],
                              [0, 1]])
        assert output == 1
        print("Test #4 passed!")
    except AssertionError:
        print(f"Test #4 failed! Expected output: 1, actual output: {output}")
    except Exception as exception:
        print(f"The following exception occured during Test #4:\n{exception}")

    # TEST #5
    try:
        output = num_islands([[4, 3, 0, 3, 2, 3],
                              [2, 1, 0, 0, 2, 1],
                              [0, 0, 1, 2, 0, 0],
                              [0, 0, 0, 1, 0, 1],
                              [3, 2, 0, 0, 0, 2]])
        assert output == 5
        print("Test #5 passed!")
    except AssertionError:
        print(f"Test #5 failed! Expected output: 5, actual output: {output}")
    except Exception as exception:
        print(f"The following exception occured during Test #5:\n{exception}")
