from typing import List


def merge_sort(list: List[int]) -> int:
    # TODO
    pass


if __name__ == "__main__":
    output = None

    # TEST #1
    try:
        output = merge_sort([11, 8, 5, 10, 3, 1, 9, 2, 4, 7, 6])
        expected = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
        assert output == expected
        print("Test #1 passed!")
    except AssertionError:
        print("Test #1 failed! "
              f"Expected output: {expected}, actual output: {output}")
    except Exception as exception:
        print(f"The following exception occured during Test #1:\n{exception}")

    # TEST #2
    try:
        output = merge_sort([2, 1])
        assert output == [1, 2]
        print("Test #2 passed!")
    except AssertionError:
        print("Test #2 failed! "
              f"Expected output: [1, 2], actual output: {output}")
    except Exception as exception:
        print(f"The following exception occured during Test #2:\n{exception}")

    # TEST #3
    try:
        output = merge_sort([])
        assert output == []
        print("Test #3 passed!")
    except AssertionError:
        print(f"Test #3 failed! Expected output: [], actual output: {output}")
    except Exception as exception:
        print(f"The following exception occured during Test #3:\n{exception}")
