# Name:
# Neptun:
# h-id:


from typing import List, Tuple


def max_tasks(tasks: List[Tuple[str, str]]) -> int:
    # TODO
    pass


if __name__ == "__main__":
    import traceback

    output = None

    # TEST #1
    try:
        output = max_tasks([("09:15", "09:45"), ("09:45", "13:00")])
        assert output == 2
        print("Test #1 passed!")
    except AssertionError:
        print(f"Test #1 failed! Expected output: 2, actual output: {output}")
    except Exception as exception:
        print(f"The following exception occured during Test #1:\n{exception}")
        traceback.print_exc()

    # TEST #2
    try:
        output = max_tasks([("09:15", "09:45"), ("09:30", "13:00")])
        assert output == 1
        print("Test #2 passed!")
    except AssertionError:
        print(f"Test #2 failed! Expected output: 1, actual output: {output}")
    except Exception as exception:
        print(f"The following exception occured during Test #2:\n{exception}")
        traceback.print_exc()

    # TEST #3
    try:
        output = max_tasks([("09:30", "13:00"),
                            ("09:15", "09:45"),
                            ("10:00", "18:00")])
        assert output == 4
        print("Test #3 passed!")
    except AssertionError:
        print(f"Test #3 failed! Expected output: 4, actual output: {output}")
    except Exception as exception:
        print(f"The following exception occured during Test #3:\n{exception}")
        traceback.print_exc()
