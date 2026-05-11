from typing import List, Tuple


def sum_zero_index_pair(numbers: List[int]) -> Tuple[int, int]:
    # Core idea: track the first occurence of every unique value in the input
    # list. When we find a value x, determine if -x has been found before, as
    # x + (-x) = 0. If it has been found before, its location is known and the
    # return value is given by this known location and the current value's
    # index.

    first_occurence = dict()

    for idx in range(len(numbers)):
        current_value = numbers[idx]
        neg_value = -1 * current_value

        if neg_value in first_occurence.keys():
            first_index = first_occurence[neg_value]
            second_index = idx
            return (first_index, second_index)
        else:
            if current_value not in first_occurence.keys():
                first_occurence[current_value] = idx

    return (-1, -1)



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
