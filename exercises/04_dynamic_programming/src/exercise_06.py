def longest_common_subsequence(string1: str, string2: str) -> int:
    # TODO
    pass


if __name__ == "__main__":
    output = None

    # TEST #1
    try:
        output = longest_common_subsequence("apple", "alien")
        assert output == 3
        print("Test #1 passed!")
    except AssertionError:
        print(f"Test #1 failed! Expected output: 3, actual output: {output}")
    except Exception as exception:
        print(f"The following exception occured during Test #1:\n{exception}")

    # TEST #2
    try:
        output = longest_common_subsequence("banana", "lettuce")
        assert output == 0
        print("Test #2 passed!")
    except AssertionError:
        print(f"Test #2 failed! Expected output: 0, actual output: {output}")
    except Exception as exception:
        print(f"The following exception occured during Test #2:\n{exception}")

    # TEST #3
    try:
        output = longest_common_subsequence("stone", "tenants")
        assert output == 2
        print("Test #3 passed!")
    except AssertionError:
        print(f"Test #3 failed! Expected output: 2, actual output: {output}")
    except Exception as exception:
        print(f"The following exception occured during Test #3:\n{exception}")
