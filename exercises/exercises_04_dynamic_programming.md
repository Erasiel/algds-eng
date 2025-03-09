# Dynamic Programming

### Exercise 1

Re-implement the following algorithms using dynamic programming!

```py
def steps(n: int) -> int:
    if n == 1: return 1
    if n == 2: return 2
    return steps(n - 1) + steps(n - 2)


def board(n: int, m: int) -> int:
    if n == 1 or m == 1: return 1
    return board(n - 1, m) + board(n, m - 1)
```

As a reminder, the problems these algorithms solve are the following:

`steps`:<br />
Our goal is to get to the top of the $n$-th step in a very long flight of stairs. We can only move either one or two steps with at a time and we can not go backwards. Design and implement a recursive algorithm that finds the number of distinct movement sequences we can take to get to get on top of the $n$-th step.

`board`:<br />
On a custom chess board with $n \times m$ positions, we want to move from the top-left corner to the bottom-right corner. We can only move one position down or right at a time and we can not go backwards. Design and implement a recursive algorithm that finds the number of distinct movement sequences we can take to get to get to the top-right corner.

Use the following outlines:

```py
def steps_dp(n: int) -> int:
    # TODO


def board_dp(n: int, m: int) -> int:
    # TODO
```

---

### Exercise 2

Using the $O$-notation, analyze the time and space complexities of the algorithms of the previous exercise and compare them to their recursive counterparts (see Exercise 4 of week 3).

---

### Exercise 3

Re-implement `boards_dp` so that it uses only $O(n)$ or $O(m)$ additional space, without changing its time complexity.

---

### Exercise 4

We are given a chess board with $n \times m$ positions, where each position is assigned a value. Every time we move to a position, we collect its value as points. Design and implement an algorithm using dynamic programming to find a path from the top-left position (at index `[0, 0]`) to the bottom-right position (at index `[n-1, k-1]`) that maximizes the collected points along the way. We can only move one position down or right at a time and we can not go backwards.

Return a tuple with two elements: the first is the sum of points along the way, and the second is the list of indices (two element tuples) corresponding to the positions that we move to on the path that yields the maximum points. If multiple paths exist that yield the same maximum, return only one such path.

**Constraints:**
- $n, m > 0$

Use the following outline:

```py
from typing import List, Tuple


def max_value_path(board: List[List[int]],
                   n: int,
                   m: int
) -> Tuple[int, List[Tuple[int, int]]]:
    # TODO
```

Hint: start by computing the maximum value, and derive the path to it from the dynamic programming table.

Example: for $n = m = 2$ and the $2 \times 2$ matrix

```math
\begin{pmatrix}
1 & 3\\
2 & 4
\end{pmatrix}
```

the maximum value is 8 and the path that yields this value is `[(0, 0), (0, 1), (1, 1)]`. Note that if we were to go down from `(0, 0)` istead of going right, we could only achieve 7 points.

---

### Exercise 5

Given an amount of money $F$, coin denominations $P = p_1, ..., p_n$, and an infinite number of coins of each denomination, find the minimum number of coins of the given denominations that add up to $F$. In other words, find $C = [c_1, c_2, ..., c_m]$ such that $\sum C = \sum_{i=1}^m c_i = F$, all $c_i \in P$, and $m$ is minimal. This problem is commonly known as the change-making, or coin change problem. Note that any denomination in $P$ can be used infinitely many times, so the values in $Q$ don't have to be distinct.

Design and implement an algorithm that solves this problem using dynamic programming. Return a list $C$ that fulfills all criteria. If multiple such lists exist, return only one.

**Constraints:**
- $F \geq 0$
- $p_i > 0$ for all $i = 1, ..., n$
- $n > 0$

Use the following outline:

```py
from typing import List


def coin_change(F: int, P: List[int], n: int) -> List[int]:
    # TODO
```

Hint: just like before, start by computing the minimum number of coins needed to make the change.

Example: for $F = 10$, $n=4$ and $P = \{1, 2, 4, 7 \}$ the desired output is either `[7, 2, 1]` or `[4, 4, 2]` (in whatever permuation). There isn't a way to change $F$ with only 2 coins from the denominations of $P$ and any more than 3 coins is not minimal.

---

### Exercise 6

Given two strings, find their longest common subsequence. A subsequence is similar to a substring (or a subarray in the case of arrays), but it does not have to be contiguous. In other words, the subsequences of a sequence $S$ are all sequences that can be derived from $S$ by deleting an arbitrary (possibly zero) number of elements from $S$ and not changing the order of the remaining elements.

For example, subsequences of the string `"apple"` include `"ap"`, `"pp"`, `"ae"`, `"pe"`, `"ale"`, the empty string, and so on. Strings such as `"elp"` and `"pap"` are not subsequences of `"apple"` because the original order of elements is not preserved.

Design and implement an algorithm using dynamic programming that determines the longest common subsequence of two strings. If multiple such subsequences exist, return only one.

**Constraints:**
- The length of both strings is greater than, or equal to zero.

Use the following outline:

```py
def longest_common_subsequence(s1: str, s2: str) -> str:
    # TODO
```

Hint: start by determining the *length* of the longest common subsequence.

Examples: the longest common subsequence of `"apple"` and `"alien"` is `"ale"`.
The lengths of the longest common subsequences of the strings `"adcbd"` and `"dacdb"` is three and there are five such sequences: `"dcd"`, `"acd"`, `"dcb"`, `"acb"`, and `"adb"`.
