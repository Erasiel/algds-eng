from typing import Set


def coin_change_possibilities(F: int, P: Set[int], n: int) -> int:

    dp_table = [[0] * (F + 1) for _ in range(n + 1)]

    # Base case: 0 money can be exchanged in exactly 1 way (with zero coins)
    for row_idx in range(n + 1): dp_table[row_idx][0] = 1

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
def coin_change_possibilities_compact(F: int, P: Set[int], n: int) -> int:
    dp_table = [0 for _ in range(F + 1)]
    dp_table[0] = 1

    for coin in P:
        for money in range(coin, F + 1):
            dp_table[money] += dp_table[money - coin]

    return dp_table[-1]


if __name__ == "__main__":
    assert coin_change_possibilities_compact(10, {1}, 1) == 1
    assert coin_change_possibilities_compact(10, {1, 5}, 2) == 3
    assert coin_change_possibilities_compact(10, {1, 5, 7}, 3) == 4
