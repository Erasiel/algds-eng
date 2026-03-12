def survival(n: int, m: int, x: int, y: int, k: int) -> float:
    # Check whether the pirate has stepped off the island
    if x < 1 or y < 1 or x > n or y > m: return 0

    # If the pirate is still on the island, check if there are still moves
    # remaining. If there are no remaining moves, the pirate survived.
    if k == 0: return 1

    # Simulate a move in each direction with equal probability (25%).
    # Afterwards, the number of remaining moves is reduced by one, as
    # indicated by the `k - 1` parameter.
    return 0.25 * (survival(n, m, x - 1, y, k - 1) +
                   survival(n, m, x + 1, y, k - 1) +
                   survival(n, m, x, y - 1, k - 1) +
                   survival(n, m, x, y + 1, k - 1))


if __name__ == "__main__":
    output = None

    # TEST #1
    try:
        output = survival(1, 1, 1, 1, 1)
        assert output == 0
        print("Test #1 passed!")
    except AssertionError:
        print(f"Test #1 failed! Expected output: 0, actual output: {output}")
    except Exception as exception:
        print(f"The following exception occured during Test #1:\n{exception}")

    # TEST #2
    try:
        output = survival(2, 2, 1, 1, 1)
        assert output == 0.5
        print("Test #2 passed!")
    except AssertionError:
        print(f"Test #2 failed! Expected output: 0.5, actual output: {output}")
    except Exception as exception:
        print(f"The following exception occured during Test #2:\n{exception}")
