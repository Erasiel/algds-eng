from typing import List


def inner_product(vec1: List[float], vec2: List[float]) -> float:
    # TODO
    pass


if __name__ == "__main__":
    output = None

    # Test #1
    try:
        output = inner_product([1, 2, 1], [2, 2, 2])
        assert output == 8
        print("Test #1 passed!")
    except:
        print(f"Test #1 failed! Expected output: 8, actual output: {output}")

    # Test #2
    try:
        output = inner_product([0.5, 0.5], [3, 3])
        assert output == 3
        print("Test #2 passed!")
    except:
        print(f"Test #2 failed! Expected output: 3, actual output: {output}")

    # Test #3
    try:
        output = inner_product([], [])
        assert output == 0
        print("Test #3 passed!")
    except:
        print(f"Test #3 failed! Expected output: 0, actual output: {output}")
