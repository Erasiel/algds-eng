# Name: Chester the Tester
# Neptun: T3ST3R
# h-id: h000000


from typing import Set


def coin_change_possibilities(F: int, P: Set[int]) -> int:

    dp_table = [[0] * (F + 1) for _ in range(len(P) + 1)]

    # Base case: 0 money can be exchanged in exactly 1 way (with zero coins)
    for row_idx in range(len(P) + 1): dp_table[row_idx][0] = 1

    coin_idx = 1

    # Note that throughout the loop, `coin == P[coin_idx - 1]`
    for coin in P:

        for money in range(1, F + 1):

            # If we can't use the current coin, we can only use the previous coins
            if money < coin:
                dp_table[coin_idx][money] = dp_table[coin_idx - 1][money]

            # Otherwise, find the number of possible changes
            else:
                # option 1: we dont use the current coin
                n_ways_no_use = dp_table[coin_idx - 1][money]

                # option 2: we use the current coin
                n_ways_use = dp_table[coin_idx][money - coin]

                dp_table[coin_idx][money] = n_ways_no_use + n_ways_use

        # Increase the coin index
        coin_idx += 1

    return dp_table[-1][-1]


# Another possible solution, based on the more compact 1D solution of the coin
# change problem:
def coin_change_possibilities_compact(F: int, P: Set[int]) -> int:
    dp_table = [0 for _ in range(F + 1)]
    dp_table[0] = 1

    for coin in P:
        for money in range(coin, F + 1):
            dp_table[money] += dp_table[money - coin]

    return dp_table[-1]


if __name__ == "__main__":
    import traceback

    output = None

    # TEST #1
    try:
        output = coin_change_possibilities(10, {1})
        assert output == 1
        print("Test #1 passed!")
    except AssertionError:
        print(f"Test #1 failed! Expected output: 1, actual output: {output}")
    except Exception as exception:
        print(f"The following exception occured during Test #1:\n{exception}")
        traceback.print_exc()

    # TEST #2
    try:
        output = coin_change_possibilities(10, {1, 5})
        assert output == 3
        print("Test #2 passed!")
    except AssertionError:
        print(f"Test #2 failed! Expected output: 3, actual output: {output}")
    except Exception as exception:
        print(f"The following exception occured during Test #2:\n{exception}")
        traceback.print_exc()

    # TEST #3
    try:
        output = coin_change_possibilities(10, {1, 5, 7})
        assert output == 4
        print("Test #3 passed!")
    except AssertionError:
        print(f"Test #3 failed! Expected output: 4, actual output: {output}")
    except Exception as exception:
        print(f"The following exception occured during Test #3:\n{exception}")
        traceback.print_exc()

    # TEST #4
    try:
        output = coin_change_possibilities(10, {3, 6, 9})
        assert output == 0
        print("Test #4 passed!")
    except AssertionError:
        print(f"Test #4 failed! Expected output: 0, actual output: {output}")
    except Exception as exception:
        print(f"The following exception occured during Test #4:\n{exception}")
        traceback.print_exc()

    # TEST #5
    try:
        output = coin_change_possibilities(0, {1, 5, 7})
        assert output == 1
        print("Test #5 passed!")
    except AssertionError:
        print(f"Test #5 failed! Expected output: 1, actual output: {output}")
    except Exception as exception:
        print(f"The following exception occured during Test #5:\n{exception}")
        traceback.print_exc()

