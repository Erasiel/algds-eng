from typing import List


def binary_search(list: List[int], x: int, l: int, r: int) -> int:
    # Perform binary search in the subarray `list[l : r + 1]`, i.e., the first
    # index in the subarray is `l`, the last is `r`
    while l <= r:

        # Get the middle index
        m = (l + r) // 2

        # If the element on the middle index is `x`, return the middle index
        if list[m] == x: return m

        # If the element on the middle index is larger than `x`, continue the
        # search in the left half of the subarray
        elif list[m] > x: r = m - 1

        # Otherwise, continue the search in the right half of the subarray
        else: l = m + 1

    # Return -1 if `x` is not in the list
    return -1


def index(list: List[int], x: int) -> int:
    return binary_search(list, x, 0, len(list) - 1)

if __name__ == "__main__":
    output = None

    # Test #1
    try:
        output = index([0, 1, 2, 3, 4], 2)
        assert output == 2
        print("Test #1 passed!")
    except AssertionError:
        print(f"Test #1 failed! Expected output: 2, actual output: {output}")
    except Exception as exception:
        print(f"The following exception occured during Test #1:\n{exception}")

    # Test #2
    try:
        output = index([0, 1, 2, 3, 4], 5)
        assert output == -1
        print("Test #2 passed!")
    except AssertionError:
        print(f"Test #2 failed! Expected output: -1, actual output: {output}")
    except Exception as exception:
        print(f"The following exception occured during Test #2:\n{exception}")