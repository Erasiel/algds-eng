from typing import List


def number_of_ones(arr: List[int], n: int) -> int:
    if n == 0: return 0

    # Binary search
    l = 0
    r = n - 1
    n_ones = 0

    if arr[0] < arr[-1]:
        # Ascending order
        while l <= r:
            m = (r + l) // 2
            if arr[m] == 0:
                l = m + 1
            else:
                n_ones += r - m + 1
                r = m - 1
    else:
        # Descending order
        while l <= r:
            m = (r + l) // 2
            if arr[m] == 0:
                r = m - 1
            else:
                n_ones += m - l + 1
                l = m + 1

    return n_ones


if __name__ == "__main__":
    assert number_of_ones([0, 0], 2) == 0
    assert number_of_ones([1, 1], 2) == 2
    assert number_of_ones([0, 0, 1, 1, 1, 1, 1], 7) == 5
    assert number_of_ones([1, 1, 1, 1, 1, 0, 0], 7) == 5
