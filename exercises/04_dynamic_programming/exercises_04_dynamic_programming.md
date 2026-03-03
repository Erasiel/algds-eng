# Dynamic Programming

### Exercise 1

Re-implement the solution to the stairs problem from last week using **dynamic programming**.

As a refresher, the problem was the following:<br>
*Our goal is to get to the top of the $n$-th step in a very long flight of stairs. We start on the ground and we can only move either one or two steps at a time and we can not go backwards. Design and implement a **recursive** algorithm that finds the number of distinct movement sequences we can take to get to get on top of the $n$-th step.*

The recursive implementation was the following:
```py
def steps(n: int) -> int:
    if n == 1: return 1
    if n == 2: return 2
    return steps(n - 1) + steps(n - 2)
```

---

### Exercise 2

Re-implement the solution to the board problem from last week using **dynamic programming**.

As a refresher, the problem was the following:<br>
*On a custom chess board with $n \times m$ positions, we want to move from the top-left corner to the bottom-right corner. We can only move one position down or right at a time and we can not go backwards. Design and implement a recursive algorithm that finds the number of distinct movement sequences we can take to get to get to the bottom-right corner.*

The recursive implementation was the following:
```py
def board(n: int, m: int) -> int:
    if n == 1 or m == 1: return 1
    return board(n - 1, m) + board(n, m - 1)
```

---

### Exercise 3

Re-implement the solution to the board problem from last week and Exercise 2 using **dynamic programming**. Make sure the space complexity of your solution is linear, i.e., $O(n)$ or $O(m)$.

---

### Exercise 4

We are given a chess board with $n \times m$ positions, where each position is assigned a value. Every time we move to a position, we collect its value as points. Design and implement an algorithm using dynamic programming to find the maximum number of points we can obtain on a path from the top-left position (at index `[0, 0]`) to the bottom-right position (at index `[n-1, m-1]`). We can only move one position down or right at a time and we can not go backwards. How would you determine the optimal solution?

**Constraints:**
- $n, m > 0$

---

### Exercise 5

Design and implement a dynamic programming algorithm that solves the minimum change making problem. That is, given an amount of money $F$, coin denominations $P = \{p_1, ..., p_n\}$, and an infinite number of coins of each denomination, find the minimum number of coins of the given denominations that add up to $F$. In other words, find $C = c_1, c_2, ..., c_m$ such that $\sum C = \sum_{i=1}^m c_i = F$, all $c_i \in P$, and $m$ is minimal.

Your implementation should return the minimum number of coins needed for making the change. How would you determine the coins needed for the optimal change?

**Constraints:**
- $F \geq 0$
- $p_i > 0$ for all $i = 1, ..., n$
- $n > 0$

---

### Exercise 6

Design and implement a dynamic programming algorithm that determines the longest common subsequence of two strings. The subsequences of a sequence $S$ are all sequences that can be derived from $S$ by deleting an arbitrary (possibly zero) number of elements from $S$ and not changing the order of the remaining elements.

Your implementation should return the length of the longest common subsequence. How would you determine the longest common subsequence itself?

**Constraints:**
- The length of both strings is greater than, or equal to zero.
