from typing import List, Set


def subsets(number_set: Set[int]) -> List[Set[int]]:
    # TODO
    pass


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
