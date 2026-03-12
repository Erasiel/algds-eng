from copy import deepcopy
from typing import List, Set


def subsets(number_set: Set[int]) -> List[Set[int]]:
    # The empty set is a subset of every set
    all_subsets = [set()]

    for number in number_set:
        # For every element in the input, and every previously created subset,
        # create two copies of the subset: one that contains the element and
        # one that does not. The latter is already created, it just needs to
        # be copied to the final list of subsets.
        prev_subsets = deepcopy(all_subsets)
        new_subsets = deepcopy(all_subsets)
        for subset in new_subsets:
            subset.add(number)
        all_subsets = prev_subsets + new_subsets

    return all_subsets


if __name__ == "__main__":
    output = None

    # Test #1
    try:
        expected = [set()]
        output = subsets(set())
        assert output == expected
        print("Test #1 passed!")
    except AssertionError:
        print("Test #1 failed! "
              f"Expected output: {expected}, actual output: {output}")
    except Exception as exception:
        print(f"The following exception occured during Test #1:\n{exception}")

    # Test #2
    try:
        expected = [set(), set([1]), set([2]), set([3]), set([1, 2]),
                    set([1, 3]), set([2, 3]), set([1, 2, 3])]
        output = subsets(set([1, 2, 3]))

        from collections import Counter
        from typing import Iterable
        assert isinstance(output, Iterable)
        expected_counter = Counter([tuple(s) for s in expected])
        output_counter = Counter([tuple(s) for s in output])
        assert expected_counter == output_counter
        print("Test #2 passed!")
    except AssertionError:
        print("Test #2 failed! "
              f"Expected output: {expected}, actual output: {output}")
    except Exception as exception:
        print(f"The following exception occured during Test #2:\n{exception}")
