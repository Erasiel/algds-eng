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
On a custom chess board with $n \times m$ positions, we want to move from the top-left corner to the bottom-right corner. We can only move one position down or right at a time and we can not go backwards. Design and implement a recursive algorithm that finds the number of distinct movement sequences we can take to get to get to the bottom-right corner.

Use the following outlines:

```py
def steps_dp(n: int) -> int:
    # TODO


def board_dp(n: int, m: int) -> int:
    # TODO
```

### Solution

`steps_dp`:<br/>
In this implementation, we handle the case where $n=0$. As such, we have $n + 1$ subproblems, so in order to store the solution of all subproblems we use a simple list of length $n + 1$. In this case, `dp_table[i]` is the number of distinct movement sequences leading to the $i$-th step.

```py
def steps_dp(n: int) -> int:
    dp_table = [0] * (n + 1)

    # Base cases
    if n >= 1: dp_table[1] = 1
    if n >= 2: dp_table[2] = 2

    # 'Recursive' cases
    for nth_step in range(3, n + 1):
        dp_table[nth_step] = dp_table[nth_step - 1] + dp_table[nth_step - 2]

    # The final element of the list is the solution to the original problem
    return dp_table[n]
```

`board_dp`:<br/>
In this problem, we have $n \cdot m$ subproblems, so we need a two-dimensional array of size $n \times m$ to store the solution of all subproblems. In this case, `dp_table[i][j]` is the number of distinct movement sequences leading to the position with the coordinates $(i+1, j+1)$ (note: Python indexing starts from 0, coordinates in the exercise start from 1).

```py
def board_dp(n: int, m: int) -> int:
    dp_table = [[0] * m for _ in range(n)]

    # Base case: first row
    for col_idx in range(m): dp_table[0][col_idx] = 1

    # Base case: first column
    for row_idx in range(n): dp_table[row_idx][0] = 1

    # 'Recursive' cases
    for row_idx in range(1, n):
        for col_idx in range(1, m):
            dp_table[row_idx][col_idx] = dp_table[row_idx - 1][col_idx] + dp_table[row_idx][col_idx - 1]

    # Same as `return dp_table[n - 1][m - 1]`
    return dp_table[-1][-1]
```

---

### Exercise 2

Using the $O$-notation, analyze the time and space complexities of the algorithms of the previous exercise and compare them to their recursive counterparts (see Exercise 4 of week 3).

### Solution

`steps`:<br/>
- Time complexity:
    - Recursive implementation: $O(2^n)$
    - DP implementation: $O(n)$
- Space complexity:
    - Recursive implementation: $O(n)$
    - DP implementation: $O(n)$

`board`:<br/>
- Time complexity:
    - Recursive implementation: $O(2^{n + m})$
    - DP implementation: $O(n \cdot m)$
- Space complexity:
    - Recursive implementation: $O(n + m)$
    - DP implementation: $O(n \cdot m)$
---

### Exercise 3

Re-implement `boards_dp` so that it uses only $O(n)$ or $O(m)$ additional space, without changing its time complexity.


### Solution

We will look at the $O(m)$ space complexity variant, it is easy to convert this to the $O(n)$ variant. In order to achieve this, we will simulate filling all rows in the previous implementation by only storing one row. We can do this, because the indexing `dp_table[row_idx - 1][col_idx]` can be simplified: if we only store one row, before updating the value of `dp_table[col_idx]`, its upper neighbor's value will be stored at `dp_table[col_idx]`, so the update reduces to `dp_table[col_idx] += dp_table[col_idx - 1]`:

```py
def board_dp(n: int, m: int) -> int:
    # First row is all 1s
    dp_table = [1] * m

    # Simulate filling all rows from the second row onwards
    for _ in range(1, n):
        for col_idx in range(1, m):
            dp_table[col_idx] += dp_table[col_idx - 1]

    return dp_table[-1]
```

Importantly, the time complexity remains $O(n \cdot m)$, but we managed to substantially reduce the algorithm's space complexity.

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

### Solution

We will assign a subproblem to each position of the matrix. These subproblems are homogenous with the original subproblem, i.e. they ask: 'How many points can be collected from the top-left corner to the position with indices $(i, j)$?' As such, at each position we need to decide where to come from to reach that position, and collect the points on that position (given in the input matrix).

If the problem only asked for the maximum number of points, the following solution would suffice:

```py
from typing import List


def max_value_path(board: List[List[int]],
                   n: int,
                   m: int
) -> int:

    # Two-dimensional DP table
    dp_table = [[0] * m for _ in range(n)]

    # When we step on the board, we collect the points on the top-left corner
    dp_table[0][0] = board[0][0]

    # First row
    for col_idx in range(1, m):
        dp_table[0][col_idx] = dp_table[0][col_idx - 1] + board[0][col_idx]

    # First column
    for row_idx in range(1, n):
        dp_table[row_idx][0] = dp_table[row_idx - 1][0] + board[row_idx][0]

    # All other positions
    for row_idx in range(1, n):
        for col_idx in range(1, m):

            # Find where we should come from to position (row_idx, col_idx)
            max_source = max(dp_table[row_idx - 1][col_idx],
                             dp_table[row_idx][col_idx - 1])

            # Collect the points at board[row_idx][col_idx]
            dp_table[row_idx][col_idx] = max_source + board[row_idx][col_idx]

    # Max value is dp_table[n - 1][m - 1]
    return dp_table[-1][-1]
```

The exercise also asks for the path that leads to the maximum points. Once we have the DP table completely filled, this is easy to recover: we go backwards from the bottom-right corner, deciding where we came from by finding the neighbor in the DP table with the higher value. This is quite tedious to implement and is intended to serve as an example of optimal path recovery - for similar tasks in the coding tests, finding the value of the optimum will be enough, recovering the path leading to the optimum will not be required.

The full implementation is as follows:

```py
from typing import List, Tuple


def max_value_path(board: List[List[int]],
                   n: int,
                   m: int
) -> Tuple[int, List[Tuple[int, int]]]:

    # Two-dimensional DP table
    dp_table = [[0] * m for _ in range(n)]

    # When we step on the board, we collect the points on the top-left corner
    dp_table[0][0] = board[0][0]

    # First row
    for col_idx in range(1, m):
        dp_table[0][col_idx] = dp_table[0][col_idx - 1] + board[0][col_idx]

    # First column
    for row_idx in range(1, n):
        dp_table[row_idx][0] = dp_table[row_idx - 1][0] + board[row_idx][0]

    # All other positions
    for row_idx in range(1, n):
        for col_idx in range(1, m):

            # Find where we should come from to position (row_idx, col_idx)
            max_source = max(dp_table[row_idx - 1][col_idx],
                             dp_table[row_idx][col_idx - 1])

            # Collect the points at board[row_idx][col_idx]
            dp_table[row_idx][col_idx] = max_source + board[row_idx][col_idx]

    # Max value is dp_table[n - 1][m - 1]
    max_val = dp_table[-1][-1]

    # Path recovery
    path_row_idx = n - 1
    path_col_idx = m - 1
    path = []

    while path_row_idx > 0 or path_col_idx > 0:
        path.insert(0, (path_row_idx, path_col_idx))

        # Decide if we came from above or left
        if path_row_idx > 0 and path_col_idx > 0:
            value_from_above = dp_table[path_row_idx - 1][path_col_idx]
            value_from_left = dp_table[path_row_idx][path_col_idx - 1]

            if value_from_above > value_from_left:
                path_row_idx -= 1
            else:
                path_col_idx -= 1

        elif path_row_idx == 0:
            path_col_idx -= 1
        else:
            path_row_idx -= 1

    # At the end, append (0, 0) at the beginning of the path
    path.insert(0, (0, 0))

    return max_val, path
```

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

Example: for $F = 10$, $n=4$ and $P = 1, 2, 4, 7$ the desired output is either `[7, 2, 1]` or `[4, 4, 2]` (in whatever permuation). There isn't a way to change $F$ with only 2 coins from the denominations of $P$ and any more than 3 coins is not minimal.

### Solution

This problem is covered in the lecture, so we will focus only on the key components of the solution. We start with a two-dimensional DP table of size $(n+1) \times (F + 1)$, where $n = |P|$ is the number of denominations. A subproblem in this DP table, indexed as `dp_table[coin_idx][money]` has the following meaning: 'Given only the first `coin_idx` denominations, what is the minimum number of coins we can use to exchange `money`?'

For example, if the input is $F = 10$, $n = 4$ and $P = 1, 2, 4, 7$, the value of `dp_table[2][7]` will be the minimum number of coins of the first 2 denominations (i.e. 1 and 2) we can use to exchange 7 money. Obviously, in this example, we are interested in `dp_table[4][10]`, i.e. the minimum number of coins of the first four denominations (note that we have exactly four denominations, so we can use all possible coins) we can use to exchange 10 money (again, note that we have 10 money altogether, so we exchange all our money). In general, the solution is `dp_table[n][F]`, or just simply `dp_table[-1][-1]`.

The base cases are simple: if there is 0 money, we need exactly 0 coins. This is represented in the DP table as the first column containing only zeros. The second base case corresponds to the row with index 0. In this row, we can use *zero* of the given denominations, so we can't exchange any amount of money that isn't zero. This will be represented as the first row containing the value $\infty$ (`math.inf` in the implementation) in all but the first column. This is important, as it handles cases where the change cannot be made (e.g. $P$ only contains even numbers and we want to exchange 7 money).

In all other cases, we have to make a decision: do we use the 'new coin of the row', i.e. the denomination that wasn't available in the previous row, or do we ignore it. When we ignore the new coin, we simply refer to the solution at `dp_table[coin_idx - 1][money]`, that is, 'without the current coin, what is the optimal solution for the same amount money?'.

When we use the new coin, the solution is `dp_table[coin_idx][money - P[coin_idx - 1]] + 1`. Let's break this down:
- The first index, corresponding to the row (the number of available coins) remains the same, because we can use the same coin again.
- The second index is reduced by the value of the current coin. This is because we decided to use this coin in the change, and once we do, the money that we need to exchange is reduced by the value of this coin.
- We add a `+ 1` at the end, because we are interested in the minimum number of coins needed to make the change. In this case, we decided to use this coin, so the number of used coins is increased by 1.

If the problem only asked for the minimum number of coins, the following solution would suffice:

```py
from typing import List, Set
import math


def coin_change(F: int, P: List[int], n: int) -> int:
    # Initialize the matrix with infinities, so that we don't have to handle
    # the second base case separately
    dp_table = [[math.inf] * (F + 1) for _ in range(n + 1)]

    # base case: 0 money can be exchanged to 0 coins
    for row_idx in range(n): dp_table[row_idx][0] = 0

    coin_idx = 1

    # Note that throughout the loop, `coin == P[coin_idx - 1]`
    for coin in P:

        for money in range(1, F + 1):

            # If we can't use the current coin, we can only use the previous coins
            if money < coin:
                dp_table[coin_idx][money] = dp_table[coin_idx - 1][money]

            # Otherwise, optimize for the minimum number of coins
            else:
                # option 1: we dont use the current coin
                n_coins_no_use = dp_table[coin_idx - 1][money]

                # option 2: we use the current coin
                n_coins_use = dp_table[coin_idx][money - coin] + 1

                dp_table[coin_idx][money] = min(n_coins_no_use, n_coins_use)

        # Increase the coin index
        coin_idx += 1

    return dp_table[-1][-1]
```

Recovering the 'path' to the optimum can again be done in a backwards way, using the DP table. At any position, we ask 'Did we use the coin of the row?', which is shown in the solutions of the subproblems: if we used the coin in the minimum change, the solution *without the coin* is higher than the solution *with the coin*. In the DP table, we compare `dp_table[coin_idx][money_idx]` (the solution when we use the coin) to `dp_table[coin_idx - 1][money_idx]` (the solution when we don't use the coin). If the solution in the row above is the same, we don't need this coin, otherwise we do, so we continue by simulating the change and continuing from a lower sum of money.

The full implementation is as follows:

```py
from typing import List, Set
import math


def coin_change(F: int, P: List[int], n: int) -> List[int]:
    # Initialize the matrix with infinities, so that we don't have to handle
    # the second base case separately
    dp_table = [[math.inf] * (F + 1) for _ in range(n + 1)]

    # base case: 0 money can be exchanged to 0 coins
    for row_idx in range(n): dp_table[row_idx][0] = 0

    coin_idx = 1

    # Note that throughout the loop, `coin == P[coin_idx - 1]`
    for coin in P:

        for money in range(1, F + 1):

            # If we can't use the current coin, we can only use the previous coins
            if money < coin:
                dp_table[coin_idx][money] = dp_table[coin_idx - 1][money]

            # Otherwise, optimize for the minimum number of coins
            else:
                # option 1: we dont use the current coin
                n_coins_no_use = dp_table[coin_idx - 1][money]

                # option 2: we use the current coin
                n_coins_use = dp_table[coin_idx][money - coin] + 1

                dp_table[coin_idx][money] = min(n_coins_no_use, n_coins_use)

        # Increase the coin index
        coin_idx += 1

    # Recovering the 'path' (which coins to use)
    money_idx = F
    coin_idx = n
    used_coins = []

    while money_idx > 0 and coin_idx > 0:
        # Do we need the current coin?
        if dp_table[coin_idx][money_idx] == dp_table[coin_idx - 1][money_idx]:
            coin_idx -= 1
        else:
            coin_value = P[coin_idx - 1]
            money_idx -= coin_value
            used_coins.append(coin_value)

    return used_coins
```

Following the principles of Exercise 3, we can improve our implementation by reducing its space complexity from $O(n \cdot F)$ to $O(F)$ by only storing one row and using it to simulate the filling of the DP table. However, to recover the coins used in the optimal change, we need an additional list. This secondary list, named `first_change` in the code below, acts as a lookup table: `first_change[x]` contains the coin that should be used first in order to make the optimal change for `x` amount of money.

In the case when using the new coin is better (results in a lower number of used coins), we need to update both the DP table and the `first_change` lookup table to reflect that the new coin should be used in the optimal change. Recovering the solution is very simple, we just have to look up which coin was used first at `F`, add it to the list of used coins, reduce the remaining money by its value and repeat until we exchanged the entire amount.

The complete implementation can be found below. This implementation is *significantly more compact* than the previous implementations, but it is by far the most optimal variant. It is also the variant that was discussed in the lecture.

```py
from typing import List
import math


def coin_change(F: int, P: List[int], n: int) -> List[int]:
    # 1D table with infinities so that we don't have to handle the second base
    # case separately
    dp_table = [math.inf for _ in range(F + 1)]

    # For every amount of money, save which coin to use first when making the
    # optimal change. -1 is used to indicate that the change cannot be made.
    first_change = [-1 for _ in range(F + 1)]

    # Base case: 0 money can be exchanged to 0 coins
    dp_table[0] = 0

    for coin in P:

        # By starting from the coin's value, we handle the case where we can't
        # use the new coin
        for money in range(coin, F + 1):

            # Same as in the previous solution, converted to 1D
            n_coins_no_use = dp_table[money]
            n_coins_use = dp_table[money - coin] + 1

            # If we get a better solution by using the coin, update the
            # subproblem's solution and the first coin to use in the change
            if n_coins_use < n_coins_no_use:
                dp_table[money] = n_coins_use
                first_change[money] = coin

    # Recovering the 'path' (which coins to use)
    used_coins = []
    money = F

    # While we have money to change and we can make the change, find the coins
    # used in the optimal change
    while money > 0 and first_change[money] != -1:
        used_coins.append(first_change[money])
        money -= first_change[money]

    return used_coins
```

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

### Solution

Again, we start with a two-dimensional DP table of size $(n + 1) \times (m + 1)$. As per usual, we assign a subproblem to every position in the DP table. In this case, `dp_table[i][j]` will contain the solution to the following subproblem: 'What is the length of the longest common subsequence of `s1[:i]` and `s2[:j]`?' Let us denote the longest common subsequence as LCS. Again, we are interested in the last element of the DP table, `dp_table[n1][n2]`, where `n1` and `n2` are the lengths of `s1` and `s2`, respectively.

The base cases are simple: if we can use 0 characters from either string, the length of the LCS is 0. This is represented as the first row and the first column of the DP table containing only zeros.

When filling the DP table, the value of `dp_table[s1_idx][s2_idx]` depends on whether the character `s1[s1_idx]` is the same as `s2[s2_idx]`. If they are the same, the corresponding character *has to be* in the LCS of `s1[:s1_idx]` and `s2[:s2_idx]`. Therefore, the solution will be the length of the LCS of `s1[:s1_idx - 1]` and `s2[:s2_idx - 1]` (which is conveniently stored in `dp_table[s1_idx - 1][s2_idx - 1]`) plus one, because the matching characters add one length to the LCS.

If `s1[s1_idx]` and `s2[s2_idx]` are not the same characters, we can ignore one of them and still get the LCS. If we ignore the character from `s1`, the length of the LCS is at `dp_table[s1_idx - 1][s2_idx]`, and if we ignore the character from `s2`, the length of the LCS is at `dp_table[s1_idx][s2_idx - 1]`. We simply have to go with the higher of these two values.

If the problem only asked for the length of the LCS, the following solution would suffice:

```py
def longest_common_subsequence(s1: str, s2: str) -> int:
    n1 = len(s1)
    n2 = len(s2)

    # Initialize the DP table with zeros, so that we don't have to handle the
    # base cases separately
    dp_table = [[0] * (n2 + 1) for _ in range(n1 + 1)]

    # Filling the DP table, note that we start the loop from index 1
    for s1_idx in range(1, n1 + 1):
        for s2_idx in range(1, n2 + 1):

            # If the characters match, they are part of the LCS of the
            # substrings
            if s1[s1_idx - 1] == s2[s2_idx - 1]:
                dp_table[s1_idx][s2_idx] = 1 + dp_table[s1_idx - 1][s2_idx - 1]

            # If the characters don't match, one of them can be ignored
            else:
                lcs_without_s1_last = dp_table[s1_idx - 1][s2_idx]
                lcs_without_s2_last = dp_table[s1_idx][s2_idx - 1]
                dp_table[s1_idx][s2_idx] = max(lcs_without_s1_last,
                                               lcs_without_s2_last)

    return dp_table[-1][-1]
```

Recovering the 'path' to the optimum, i.e. the LCS itself can again be done in a backwards way. We have to find characters that contribute to the length of the LCS: if `dp_table[s1_idx][s2_idx]` is larger than both `dp_table[s1_idx - 1][s2_idx]` and `dp_table[s1_idx][s2_idx - 1]`, then the following are true:
- the characters `s1[s1_idx]` and `s2[s2_idx]` are the same, and
- `s1[s1_idx]` is part of the LCS

If we can ignore one of the characters, i.e. `dp_table[s1_idx][s2_idx] == dp_table[s1_idx - 1][s2_idx]` or `dp_table[s1_idx][s2_idx] == dp_table[s1_idx][s2_idx - 2]`, we have to go along the path of the longer LCS to find the character that cannot be ignored (see before).

The full implementation is as follows:

```py
def longest_common_subsequence(s1: str, s2: str) -> int:
    n1 = len(s1)
    n2 = len(s2)

    # Initialize the DP table with zeros, so that we don't have to handle the
    # base cases separately
    dp_table = [[0] * (n2 + 1) for _ in range(n1 + 1)]

    # Filling the DP table, note that we start the loop from index 1
    for s1_idx in range(1, n1 + 1):
        for s2_idx in range(1, n2 + 1):

            # If the characters match, they are part of the LCS of the
            # substrings
            if s1[s1_idx - 1] == s2[s2_idx - 1]:
                dp_table[s1_idx][s2_idx] = 1 + dp_table[s1_idx - 1][s2_idx - 1]

            # If the characters don't match, one of them can be ignored
            else:
                lcs_without_s1_last = dp_table[s1_idx - 1][s2_idx]
                lcs_without_s2_last = dp_table[s1_idx][s2_idx - 1]
                dp_table[s1_idx][s2_idx] = max(lcs_without_s1_last,
                                               lcs_without_s2_last)

    s1_idx = n1
    s2_idx = n2
    lcs = ""

    while s1_idx > 0 and s2_idx > 0:
        lcs_without_s1_char = dp_table[s1_idx - 1][s2_idx]
        lcs_without_s2_char = dp_table[s1_idx][s2_idx - 1]
        lcs_with_last_chars = dp_table[s1_idx][s2_idx]

        if lcs_with_last_chars > lcs_without_s1_char and lcs_with_last_chars > lcs_without_s2_char:
            lcs = s1[s1_idx - 1] + lcs
            s1_idx -= 1
            s2_idx -= 1
        elif lcs_without_s1_char > lcs_without_s2_char:
            s1_idx -= 1
        else:
            s2_idx -= 1

    return lcs
```

Note that it is possible that two strings have multiple longest common subsequences. This approach recovers only one.
