from typing import List, Tuple


def contains_circular_reference(references: List[Tuple[str, str]]) -> bool:
    # TODO
    pass


if __name__ == "__main__":

    import traceback

    output = None

    # TEST #1
    try:
        output = contains_circular_reference([("A1", "A2"),
                                              ("A2", "A3"),
                                              ("A3", "A4"),
                                              ("A4", "A5"),
                                              ("A5", "A6")])
        assert output == False
        print("Test #1 passed!")
    except AssertionError:
        print("Test #1 failed! Expected output: False, "
              f"actual output: {output}")
    except Exception as exception:
        print(f"The following exception occured during Test #1:\n{exception}")
        traceback.print_exc()

    # TEST #2
    try:
        output = contains_circular_reference([("A1", "A2"),
                                              ("A2", "A3"),
                                              ("A3", "A4"),
                                              ("A4", "A5"),
                                              ("A5", "A1")])
        assert output == True
        print("Test #2 passed!")
    except AssertionError:
        print("Test #2 failed! Expected output: True, "
              f"actual output: {output}")
    except Exception as exception:
        print(f"The following exception occured during Test #2:\n{exception}")
        traceback.print_exc()

    # TEST #3
    try:
        output = contains_circular_reference([])
        assert output == False
        print("Test #3 passed!")
    except AssertionError:
        print("Test #3 failed! Expected output: True, "
              f"actual output: {output}")
    except Exception as exception:
        print(f"The following exception occured during Test #3:\n{exception}")
        traceback.print_exc()
