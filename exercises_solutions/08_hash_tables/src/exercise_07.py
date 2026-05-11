def anagrams(s1: str, s2: str) -> bool:
    # Core idea: calculate the frequencies of every letter in each string
    # separately, then check if these frequencies match between the two
    # strings.
    s1_character_occurences = dict()
    s2_character_occurences = dict()

    for char in s1:
        if char not in s1_character_occurences:
            s1_character_occurences[char] = 0
        s1_character_occurences[char] += 1

    for char in s2:
        if char not in s2_character_occurences:
            s2_character_occurences[char] = 0
        s2_character_occurences[char] += 1

    return s1_character_occurences == s2_character_occurences


if __name__ == "__main__":
    output = None

    # TEST #1
    try:
        output = anagrams("cinema", "iceman")
        assert output == True
        print("Test #1 passed!")
    except AssertionError:
        print("Test #1 failed! Expected output: True, "
              f"actual output: {output}")
    except Exception as exception:
        print(f"The following exception occured during Test #1:\n{exception}")

    # TEST #2
    try:
        output = anagrams("", "")
        assert output == True
        print("Test #2 passed!")
    except AssertionError:
        print("Test #2 failed! Expected output: True, "
              f"actual output: {output}")
    except Exception as exception:
        print(f"The following exception occured during Test #2:\n{exception}")

    # TEST #3
    try:
        output = anagrams("nothing", "something")
        assert output == False
        print("Test #3 passed!")
    except AssertionError:
        print("Test #3 failed! Expected output: False, "
              f"actual output: {output}")
    except Exception as exception:
        print(f"The following exception occured during Test #3:\n{exception}")

    # TEST #4
    try:
        output = anagrams("", "something")
        assert output == False
        print("Test #4 passed!")
    except AssertionError:
        print("Test #4 failed! Expected output: False, "
              f"actual output: {output}")
    except Exception as exception:
        print(f"The following exception occured during Test #4:\n{exception}")
