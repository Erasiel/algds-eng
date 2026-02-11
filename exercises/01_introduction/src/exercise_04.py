from typing import List


def most_frequent_element(l: List[int]) -> int:
    # TODO
    pass


if __name__ == "__main__":
    output = None

    # TEST #1
    try:
        output = most_frequent_element([1, 2, 1, 3, 1, 2])
        assert output == 1
        print("Test #1 passed!")
    except:
        print("Test #1 failed! "
              f"Expected output: 1, actual output: {output}")

    # TEST #2
    try:
        output = most_frequent_element([1, 2, 1, 2, 3])
        assert output == 2
        print("Test #2 passed!")
    except:
        print("Test #2 failed! "
              f"Expected output: 2, actual output: {output}")
