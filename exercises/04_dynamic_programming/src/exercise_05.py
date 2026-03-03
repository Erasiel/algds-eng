from typing import List


def min_change(F: int, P: List[int]) -> int:
    # TODO
    pass


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
