from typing import List


def index(list: List[int], x: int) -> int:
    # TODO
    pass


if __name__ == "__main__":
    output = None

    # Test #1
    try:
        output = index([0, 3, 2, 4, 1], 2)
        assert output == 2
        print("Test #1 passed!")
    except:
        print(f"Test #1 failed! Expected output: 2, actual output: {output}")

    # Test #2
    try:
        output = index([0, 3, 2, 4, 1], 5)
        assert output == -1
        print("Test #2 passed!")
    except:
        print(f"Test #2 failed! Expected output: -1, actual output: {output}")
