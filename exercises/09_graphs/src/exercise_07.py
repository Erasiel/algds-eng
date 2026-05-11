from typing import List


def num_transformations(start_word: str,
                        dest_word: str,
                        word_list: List[str]
) -> int:
    # TODO
    pass


if __name__ == "__main__":

    output = None

    # TEST #1
    try:
        output = num_transformations("hit",
                                     "cog",
                                     ["hot", "dot", "dog", "lot", "log", "cog"])
        assert output == 4
        print("Test #1 passed!")
    except AssertionError:
        print(f"Test #1 failed! Expected output: 4, actual output: {output}")
    except Exception as exception:
        print(f"The following exception occured during Test #1:\n{exception}")

    # TEST #2
    try:
        output = num_transformations("hit",
                                     "cog",
                                     ["hot", "dot", "dog", "lot", "log"])
        assert output == -1
        print("Test #2 passed!")
    except AssertionError:
        print(f"Test #2 failed! Expected output: -1, actual output: {output}")
    except Exception as exception:
        print(f"The following exception occured during Test #2:\n{exception}")

    # TEST #3
    try:
        output = num_transformations("hit",
                                     "lit",
                                     ["hot", "dot", "lot", "log", "lit"])
        assert output == 1
        print("Test #3 passed!")
    except AssertionError:
        print(f"Test #3 failed! Expected output: 1, actual output: {output}")
    except Exception as exception:
        print(f"The following exception occured during Test #3:\n{exception}")

    # TEST #4
    try:
        output = num_transformations("hit",
                                     "god",
                                     ["hot", "god", "lot", "log", "lit"])
        assert output == -1
        print("Test #4 passed!")
    except AssertionError:
        print(f"Test #4 failed! Expected output: -1, actual output: {output}")
    except Exception as exception:
        print(f"The following exception occured during Test #4:\n{exception}")
