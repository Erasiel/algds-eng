from typing import List


def max_points(board: List[List[int]]) -> int:
    # Greedy choice: move towards the neighboring tile that has a larger value.

    n_rows = len(board)
    n_cols = len(board[0])

    curr_i = 0
    curr_j = 0
    total_points = board[0][0]

    while curr_i < n_rows - 1 or curr_j < n_cols - 1:
        # Can we move in both directions?
        if curr_i < n_rows - 1 and curr_j < n_cols - 1:
            val_right = board[curr_i][curr_j + 1]
            val_down = board[curr_i + 1][curr_j]

            if val_down > val_right: curr_i += 1
            else: curr_j += 1

        # We can only move down
        elif curr_j == n_cols - 1: curr_i += 1

        # We can only move right
        else: curr_j += 1

        total_points += board[curr_i][curr_j]

    return total_points

if __name__ == "__main__":
    print("Testing on the matrix [[1, 2, 3], [3, 1, 0]]")
    print("Optimum: 6")
    print(f"Greedy algorithm: {max_points([[1, 2, 3], [3, 1, 0]])}")
