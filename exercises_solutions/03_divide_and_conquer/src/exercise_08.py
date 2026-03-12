from typing import List


def merge(left: List[int], right: List[int]) -> List[int]:
    # Prepare the output list
    output = [None] * (len(left) + len(right))

    # Three indices are used in the merging process. At all times,
    # `left[left_idx]` and `right[right_idx]` are the lowest non-merged
    # elements from the two lists, and `out_idx` is index in the output where
    # the next element will be merged
    left_idx = 0
    right_idx = 0
    out_idx = 0

    # While both sublists have non-merged items, merge them in sorted order
    while left_idx < len(left) and right_idx < len(right):
        if left[left_idx] < right[right_idx]:
            output[out_idx] = left[left_idx]
            left_idx += 1
        else:
            output[out_idx] = right[right_idx]
            right_idx += 1

        out_idx += 1

    # If a list has non-merged elements, copy them directly to the end of the
    # output list. Note that out of the following two while loops, only one
    # will be executed.
    while left_idx < len(left):
        output[out_idx] = left[left_idx]
        left_idx += 1
        out_idx += 1

    while right_idx < len(right):
        output[out_idx] = right[right_idx]
        right_idx += 1
        out_idx += 1

    return output


def merge_sort(list: List[int]) -> int:
    # A list that contains at most 1 element is sorted
    if len(list) <= 1: return list

    # Divide the list into two halves and sort them recursively
    m = len(list) // 2
    left_sorted_sublist = merge_sort(list[:m])
    right_sorted_sublist = merge_sort(list[m:])

    # Merge the two sorted sublists
    return merge(left_sorted_sublist, right_sorted_sublist)


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
