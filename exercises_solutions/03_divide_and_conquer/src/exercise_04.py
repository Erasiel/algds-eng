from typing import List


def binary_search(list: List[int], x: int, l: int, r: int) -> int:
    if l > r: return -1

    m = (l + r) // 2
    if list[m] == x: return m
    elif list[m] < x: return binary_search(list, x, m + 1, r)
    else: return binary_search(list, x, l, m - 1)


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
