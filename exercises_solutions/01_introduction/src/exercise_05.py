def num_unique_characters(string: str) -> str:
    # A set stores every unique element exactly once
    # After adding all characters of the input to the set, the length of the
    # set will be the number of unique characters
    character_set = set()

    for character in string:
        character_set.add(character)

    return len(character_set)


if __name__ == "__main__":
    output = None

    # TEST #1
    try:
        output = num_unique_characters("00101")
        assert output == 2
        print("Test #1 passed!")
    except AssertionError:
        print("Test #1 failed! "
              f"Expected output: 2, actual output: {output}")
    except Exception as exception:
        print(f"The following exception occured during Test #1:\n{exception}")

    # TEST #2
    try:
        output = num_unique_characters("12345432123454321")
        assert output == 5
        print("Test #2 passed!")
    except AssertionError:
        print("Test #2 failed! "
              f"Expected output: 5, actual output: {output}")
    except Exception as exception:
        print(f"The following exception occured during Test #2:\n{exception}")

    # TEST #3
    try:
        output = num_unique_characters("")
        assert output == 0
        print("Test #3 passed!")
    except AssertionError:
        print("Test #3 failed! "
              f"Expected output: 0, actual output: {output}")
    except Exception as exception:
        print(f"The following exception occured during Test #3:\n{exception}")
