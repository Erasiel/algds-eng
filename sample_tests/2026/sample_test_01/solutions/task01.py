# Name: Chester the Tester
# Neptun: T3ST3R
# h-id: h000000


from typing import List


def n_ones_ascending(arr: List[int]) -> int:
    # Binary search
    l = 0
    r = len(arr) - 1

    # Collect the number of ones
    n_ones = 0

    while l <= r:
        m = (l + r) // 2

        # If the middle element is zero, only the right half sublist can
        # contain ones
        if arr[m] == 0:
            l = m + 1

        # If the middle element is one, every element in the right half
        # sublist is one, so its length can be added to the number of ones; we
        # then continue the search in the left half sublist
        else:
            n_ones += r - m + 1
            r = m - 1

    return n_ones


def n_ones_descending(arr: List[int]) -> int:
    # Same as above, but for lists sorted in descending order
    l = 0
    r = len(arr) - 1
    n_ones = 0

    while l <= r:
        m = (l + r) // 2
        if arr[m] == 0:
            r = m - 1
        else:
            n_ones += m - l + 1
            l = m + 1

    return n_ones


def number_of_ones(arr: List[int]) -> int:
    if len(arr) == 0: return 0

    if arr[0] < arr[-1]:
        return n_ones_ascending(arr)
    else:
        return n_ones_descending(arr)


if __name__ == "__main__":
    import traceback

    output = None

    # TEST #1
    try:
        output = number_of_ones([0, 0])
        assert output == 0
        print("Test #1 passed!")
    except AssertionError:
        print(f"Test #1 failed! Expected output: 0, actual output: {output}")
    except Exception as exception:
        print(f"The following exception occured during Test #1:\n{exception}")
        traceback.print_exc()

    # TEST #2
    try:
        output = number_of_ones([1, 1])
        assert output == 2
        print("Test #2 passed!")
    except AssertionError:
        print(f"Test #2 failed! Expected output: 2, actual output: {output}")
    except Exception as exception:
        print(f"The following exception occured during Test #2:\n{exception}")
        traceback.print_exc()

    # TEST #3
    try:
        output = number_of_ones([0, 0, 1, 1, 1, 1, 1])
        assert output == 5
        print("Test #3 passed!")
    except AssertionError:
        print(f"Test #3 failed! Expected output: 5, actual output: {output}")
    except Exception as exception:
        print(f"The following exception occured during Test #3:\n{exception}")
        traceback.print_exc()

    # TEST #4
    try:
        output = number_of_ones([1, 1, 1, 1, 1, 0, 0])
        assert output == 5
        print("Test #4 passed!")
    except AssertionError:
        print(f"Test #4 failed! Expected output: 5, actual output: {output}")
    except Exception as exception:
        print(f"The following exception occured during Test #4:\n{exception}")
        traceback.print_exc()
