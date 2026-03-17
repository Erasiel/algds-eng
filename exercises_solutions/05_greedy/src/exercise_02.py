from typing import List
import math


def min_change(F: int, P: List[int]) -> int:
    # Greedy choice: always use the largest coin denomination.

    P_sorted = sorted(P, reverse=True)
    p_idx = 0
    F_remaining = F
    n_coins = 0

    while F_remaining > 0:
        # Find the largest usable coin
        while p_idx < len(P) - 1 and P_sorted[p_idx] > F_remaining: p_idx += 1

        current_coin = P_sorted[p_idx]
        F_remaining -= current_coin
        n_coins += 1

    if F_remaining != 0:
        return math.inf
    else:
        return n_coins


if __name__ == "__main__":
    print("Testing on F=40, P=[5, 10, 20, 25, 50]")
    print("Optimum: 2")
    print(f"Greedy algorithm: {min_change(40, [5, 10, 20, 25, 50])}")
