from typing import List, Set


def not_unique(strings: List[str]) -> Set[str]:
    # Core idea: loop over the input list once, keep track of all strings
    # we've seen at least once. If a string is in the set of seen strings, it
    # is not unique.
    # A solution based on frequency counting would also be correct.
    strings_in_the_input = set()
    not_unique_strings = set()

    for string in strings:
        if string in strings_in_the_input:
            not_unique_strings.add(string)
        else:
            strings_in_the_input.add(string)

    return not_unique_strings


if __name__ == "__main__":
    output = None

    # TEST #1
    try:
        output = not_unique(["apple",
                             "peach",
                             "apple",
                             "strawberry",
                             "peach",
                             "apple"])
        expected = {"apple", "peach"}
        assert output == expected
        print("Test #1 passed!")
    except AssertionError:
        print(f"Test #1 failed! Expected output: {expected}, "
              f"actual output: {output}")
    except Exception as exception:
        print(f"The following exception occured during Test #1:\n{exception}")

    # TEST #2
    try:
        output = not_unique(["A", "B", "C", "D", "E"])
        assert output == set()
        print("Test #2 passed!")
    except AssertionError:
        print(f"Test #2 failed! Expected output: {set()}, "
              f"actual output: {output}")
    except Exception as exception:
        print(f"The following exception occured during Test #2:\n{exception}")

    # TEST #3
    try:
        output = not_unique([])
        assert output == set()
        print("Test #3 passed!")
    except AssertionError:
        print(f"Test #3 failed! Expected output: {set()}, "
              f"actual output: {output}")
    except Exception as exception:
        print(f"The following exception occured during Test #3:\n{exception}")
