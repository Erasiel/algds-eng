from typing import List, Tuple


def sum_zero_index_pair(numbers: List[int]) -> Tuple[int, int]:
    # TODO
    pass


if __name__ == "__main__":
    output = None

    # TEST #1
    try:
        output = sum_zero_index_pair([1, 2, 3, 4, -1, -5, -6, -7])
        assert output == (0, 4)
        print("Test #1 passed!")
    except AssertionError:
        print("Test #1 failed! Expected output: (0, 4), "
              f"actual output: {output}")
    except Exception as exception:
        print(f"The following exception occured during Test #1:\n{exception}")

    # TEST #2
    try:
        output = sum_zero_index_pair([0, -1, 2, -3, 4, -5, 6])
        assert output == (-1, -1)
        print("Test #2 passed!")
    except AssertionError:
        print(f"Test #2 failed! Expected output: (-1, -1), "
              f"actual output: {output}")
    except Exception as exception:
        print(f"The following exception occured during Test #2:\n{exception}")

    # TEST #3
    try:
        output = sum_zero_index_pair([])
        assert output == (-1, -1)
        print("Test #3 passed!")
    except AssertionError:
        print(f"Test #3 failed! Expected output: (-1, -1), "
              f"actual output: {output}")
    except Exception as exception:
        print(f"The following exception occured during Test #3:\n{exception}")
