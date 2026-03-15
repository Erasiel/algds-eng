def longest_common_subsequence(string1: str, string2: str) -> int:
    # Create a 2D DP table where every position (i, j) contains the solution
    # of the subproblem 'what is the length of the longest common subsequence (LCS) of `string1[:i+1]` and `string2[:j+1]`?'
    n_rows = len(string1) + 1
    n_cols = len(string2) + 1
    dp_table = [[0] * n_cols for _ in range(n_rows)]

    # The base cases (first row, first column), i.e., where one of the
    # substrings is of length zero, are handled by the initialization.
    # Second row, second column onwards
    for i in range(1, n_rows):
        for j in range(1, n_cols):
            char_from_s1 = string1[i - 1]
            char_from_s2 = string2[j - 1]

            # If the two characters match, they contribute to the LCS as its
            # last character, and the rest is the LCS of `string1[:i]` and
            # `string2[:j]`.
            if char_from_s1 == char_from_s2:
                dp_table[i][j] = dp_table[i - 1][j - 1] + 1

            # Otherwise, the LCS is guaranteed to not contain one of these
            # characters.
            else:
                dp_table[i][j] = max(dp_table[i - 1][j], dp_table[i][j - 1])

    return dp_table[-1][-1]

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
