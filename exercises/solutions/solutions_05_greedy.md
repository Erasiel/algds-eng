# Greedy Algorithms - Solutions

### Exercise 1

Design a simple greedy algorithm for the point collection problem (week 4, exercise 4). Define the greedy choice and show that by making the greedy choice, only one subproblem remains. Show that your algorithm is *not* optimal.

### Solution

A simple greedy choice can be the following: after collecting the points on `board[i][j]`, move to the neighbor with more points (either `board[i + 1][j]` or `board[i][j + 1]`). With this choice, the smaller remaining subproblem is the point collection problem on a smaller matrix. We could easily implement this algorithm as follows:

```py
from typing import List, Tuple


def max_value_path(board: List[List[int]],
                   n: int,
                   m: int
) -> Tuple[int, List[Tuple[int, int]]]:
    path = [(0, 0)]
    points = board[0][0]
    i = 0
    j = 0

    # While we are not at the bottom-right corner, keep collecting points
    while i != n - 1 or j != m - 1:

        # If we can go both down and right, go towards the larger neighbor
        if i + 1 < n and j + 1 < m:
            if board[i + 1][j] > board[i][j + 1]:
                i += 1
            else:
                j += 1

        # If we can't go right, go down
        elif i + 1 < n:
            i += 1

        # If we can't go down, go right
        else:
            j += 1

        # Collect the points on our current position and add the position to
        # the path
        points += board[i][j]
        path.append((i, j))

    return (points, path)
```

To show that an algorithm is not optimal, we have to find an input on which the algorithm's output is not the optimal solution. Let's take the following $3 \times 3$ matrix as an example:

```math
\begin{pmatrix}
2 & 6 & 5 \\
2 & 4 & 1 \\
3 & 3 & 3
\end{pmatrix}
```

Our greedy algorithm would return a path that contains a total of 17 points, however, the optimal solution is 18 points.

---

### Exercise 2

Design a simple greedy algorithm for the coin change problem (week 4, exercise 5). Define the greedy choice and show that by making the greedy choice, only one subproblem remains. Show that your algorithm is *not* optimal.

### Solution

A simple greedy choice is the following: find the largest coin denomination $d_i$ that is not larger than our remaining money, make the change and reduce our remaining money by $d_i$. With this choice, the smaller remaining subproblem is changing a lower amount of money. We could easily implement this algorithm as follows:

```py
from typing import List


def coin_change(F: int, P: List[int], n: int) -> List[int]:
    remaining_money = F
    used_coins = []

    # Sort the coin denominations in descending order
    sorted_coins = sorted(P, reverse=True)

    for coin in sorted_coins:
        while remaining_money >= coin:
            remaining_money -= coin
            used_coins.append(coin)

    return used_coins
```

Finding an input on which the algorithm is not optimal is also quite easy. For $F = 15$, $n = 3$, and $P = [5, 6, 1]$, the greedy algorithm uses five coins (6, 6, 1, 1, 1), but the optimal solution uses only three coins (5, 5, 5).

---

### Exercise 3

We are planning a long car trip, but our car can only carry $n$ liters of fuel. We have a map that shows the gas stations on our path and we calculated the "distance" in fuel consumption between each subsequent gas station. Design and implement an efficient algorithm that determines the locations at which we have to stop to fully refuel, in order to stop as few times as possible.

The input contains $k$ numbers $d_1, ..., d_k$ with each $d_i$ representing the distance (in liters of fuel) between the $i-1^\text{th}$ and the $i^\text{th}$ gas stations. Assume that we start at the $0^{th}$ gas station with a full tank. Return the indices of the gas stations at which we have to refuel in order to stop as few times as possible. If multiple such options exist, return only one. Use the following outline:

```py
from typing import List


def car_trip(distances: List[float], n: float, k: int) -> List[int]:
    # TODO
```

Example: for $n = 10$, $k = 4$, and `distances = [5, 7, 4, 3]` we need two stops at the first and second gas stations.

### Solution

A simple greedy choice can be to go as far as possible without refueling, and only refuel if we can't cover the next part of the trip (because we don't have enough fuel in our tank). It is easy to see that this greedy choice is optimal. The algorithm can be implemented as follows:

```py
from typing import List


def car_trip(distances: List[float], n: float, k: int) -> List[int]:
    stops = []

    # Start with a full tank, our next stop's index is 1
    remaininig_fuel = n
    next_stop = 1

    for dist in distances:

        # Refuel if we can't cover the next part of the trip
        if dist > remaininig_fuel:
            stops.append(next_stop - 1)
            remaininig_fuel = n

        # Travel the next part of the trip
        remaininig_fuel -= dist
        next_stop += 1

    return stops
```

Note that if we only had to find the number of stops and not the indices of the stops, the task could be solved in constant time.

---

### Exercise 4

You are given $n$ real numbers $k_1, ..., k_n$. We say a closed interval $[a, b]$ *covers* a number $k$ if and only if $a \leq k \leq b$. Design and implement an algorithm that finds a minimal number of unit-length closed intervals (i.e. $[a, a+1]$) such that all numbers are covered by at least one of the intervals.

Return a list of two element tuples where each tuple represents an interval by its lower and upper endpoint. If multiple appropriate lists of intervals exist, return only one. Use the following outline:

```py
from typing import List, Tuple


def interval_cover(K: List[float], n: int) -> List[Tuple[float, float]]:
    # TODO
```

Example: for `K = [0.1, 0.3, 0.7, 1.2, 1.3, 1.4, 1.6, 1.8]` ($n=8$) an optimal solution using two intervals is $[0, 1]$ and $[1.1, 2.1]$, where $[0, 1]$ covers the first three points and $[1.1, 2.1]$ covers the last five.

### Solution

Defining a greedy choice for this task can be a little challenging, as not every possible greedy choice will be optimal. For example, starting with an interval that covers as many points as possible and repeating this process with the remaining uncovered points will not be optimal.

An optimal choice is to start an interval with the lowest uncovered point, remove all points that this interval covers from later consideration and continue with the remaining uncovered points. The algorithm can be implemented as follows:

```py
from typing import List, Tuple


def interval_cover(K: List[float], n: int) -> List[Tuple[float, float]]:
    # Sort points in ascending order
    K = sorted(K)

    intervals = []
    last_interval = (K[0], K[0] + 1)
    intervals.append(last_interval)

    for point in K:

        # If the current point is not covered by the last interval, create a
        # new interval and use it to cover the remaining points
        if not (last_interval[0] <= point <= last_interval[1]):
            last_interval = (point, point + 1)
            intervals.append(last_interval)

    return intervals
```

Note that we sort the input points because the exercise does not specify that they are sorted (so we must assume that they are not). A re-implementation of the algorithm without sorting first would rely on a minimum search within the `for` loop, making its running time $O(n^2)$. With sorting, the running time is $O(n \log n)$.

---

### Exercise 5

You are given $n$ items, described by their value ($v_i$) and weight ($w_i$) and a knapsack with capacity $C$. You can put any item in this knapsack as long as the total weight of the items in the knapsack doesn't exceed its capacity. Your goal is to put items into the knapsack so that their total value is maximal. This is commonly known as the knapsack problem.

Design a greedy algorithm for the 0-1 knapsack problem. Define the greedy choice and show that by making the greedy choice, only one subproblem remains.

Run your algorithm on the following input:

| $v_i$ | $w_i$ |
|:-----:|:-----:|
|   5   |   3   |
|   4   |   4   |
|   5   |   2   |
|   5   |   6   |
|   4   |   5   |

and $C = 12$. What is the optimal solution? What would be the solution for the fractional knapsack problem with the same input?

### Solution

The greedy knapsack problem relies on computing $v_i / w_i$ for each item, which allows us to compare the value each item has per unit weight. The greedy choice is to fill the remaining part of the kanpsack with the item that has the highest $v_i / w_i$ ratio among those that are not in the knapsack. If we can fit the entire item into the knapsack, we do so and reduce the remaining capacity by the item's weight. In the fractional problem, if the entire item doesn't fit in the knapsack, but a part of it does, we break the item and fill the knapsack.

Let us now solve the 0-1 knapsack problem with the given input. The $v_i / w_i$ ratios of the items are as follows:

| $v_i$ | $w_i$ | $v_i / w_i$ |
|:-----:|:-----:| :---------: |
|   5   |   3   | 1.666... |
|   4   |   4   | 1 |
|   5   |   2   | 2.5 |
|   5   |   6   | 0.833... |
|   4   |   5   | 0.8 |

Our greedy item selection is as follows:

1. We start with the third item. It fits into the knapsack, bringing our remaining capacity down to 10 and our total value up to 5.
2. We continue with the first item. It fits into the knapsack, bringing our remaining capacity down to 7 and our total value up to 10.
3. We continue with the second item. It fits into the knapsack, bringing our remaining capacity down to 3 and our total value up to 14.

Since we cannot fit either of the remaining items into the knapsack, the greedy solution to the 0-1 problem in this case is 14. It's easy to see that this solution is *not* optimal, because we can fit the first, third and fourth items into the knapsack, as their total weight is 11. This selection of items gives us a total value of 15, which is the optimal solution to the 0-1 problem.

When it comes to the fractional problem, the greedy approach is the same, and the first three selected items are the same as above. However, we still have 3 remaining capacity, so we can continue with the item selection:

4. We continue with the fourth item. It doesn't fit into the knapsack, so we break it and fit a part of it that fills exactly 3 capacity. This gives us a further 3 * (5 / 6) value, bringing our total value up to 16.5 and our remaining capacity down to 0.

Since we have no more unused capacity, the greedy solution to the fractional knapsack problem in this case is 16.5. The greedy algorithm is optimal if we can break items.

Two side notes:
- It is easy to see that at most one item will be broken in the fractional case.
- Running out of items is another condition for ending the item selection process. If this is the case, the remaining capacity after using all items will be nonzero even in the fractional problem.

---

### Exercise 6

Based on the discussion of Exercise 5, implement an algorithm for the fractional knapsack problem, where an item can be used at most once. Your algorithm should calculate the maximum total value that can be put in the knapsack.

Use the following outline, where items are represented by the `Item` class:

```py
from typing import List


class Item:
    def __init__(self, value: int, weight: int) -> None:
        self.value = value
        self.weight = weight


def knapsack(C: int, items: List[Item], n: int) -> float:
    # TODO
```

As further practice, extend your algorithm so that it returns how much of each item should be put in the knapsack for the largest total value. Return a `Dict[Item, float]` object that assigns a real value between 0 and 1 to all items, based on what fraction the item is used in the optimal solution.

Use the following outline:

```py
from typing import List, Dict


class Item:
    def __init__(self, value: int, weight: int) -> None:
        self.value = value
        self.weight = weight


def knapsack(C: int, items: List[Item], n: int) -> Dict[Item, float]:
    # TODO
```

### Solution

The solution to the simple problem follows the discussion of Exercise 5. The implementation is as follows:

```py
from typing import List


class Item:
    def __init__(self, value: int, weight: int) -> None:
        self.value = value
        self.weight = weight


def unit_value(item: Item) -> float:
    return item.value / item.weight


def knapsack(C: int, items: List[Item], n: int) -> float:
    total_value = 0
    remaining_capacity = C

    # Sort items by v_i / w_i in descending order
    items = sorted(items, key=unit_value, reverse=True)

    for item in items:

        # If the whole item fits in the knapsack, place it and continue
        if item.weight <= remaining_capacity:
            total_value += item.value
            remaining_capacity -= item.weight

        # If only a part of the item fits in the knapsack, break it
        # Note that if remaining_capacity is zero (i.e. we filled the knapsack
        # without breaking an item), this will not increase the total value in
        # the knapsack
        else:
            total_value += unit_value(item) * remaining_capacity

            # At most one item will be broken, so after breaking an item, we
            # stop item selection
            break

    return total_value
```

Modifying this solution to return how much of each item is used in the optimal solution is simple:

```py
from typing import List, Dict


class Item:
    def __init__(self, value: int, weight: int) -> None:
        self.value = value
        self.weight = weight


def unit_value(item: Item) -> float:
    return item.value / item.weight


def knapsack(C: int, items: List[Item], n: int) -> Dict[Item, float]:
    remaining_capacity = C

    # At first, we don't use any of the items
    used_ratios = {item: 0 for item in items}

    # Sort items by v_i / w_i in descending order
    items = sorted(items, key=unit_value, reverse=True)

    for item in items:

        # If the whole item fits in the knapsack, place it and continue
        if item.weight <= remaining_capacity:
            remaining_capacity -= item.weight
            used_ratios[item] = 1.0

        # If only a part of the item fits in the knapsack, break it
        # Note that if remaining_capacity is zero (i.e. we filled the knapsack
        # without breaking an item), this will not increase the total value in
        # the knapsack
        else:
            used_ratios[item] = remaining_capacity / item.weight

            # At most one item will be broken, so after breaking an item, we
            # stop item selection
            break

    return used_ratios
```

---

### Exercise 7

Design and implement an algorithm for the 0-1 knapsack problem using dynamic programming. Return the maximum total value that can be put in the knapsack.

Use the following outline, where items are represented by the `Item` class:

```py
from typing import List


class Item:
    def __init__(self, value: int, weight: int) -> None:
        self.value = value
        self.weight = weight


def knapsack(C: int, items: List[Item], n: int) -> float:
    # TODO
```

Hint: Feel free to use the solution to the coin change problem (Week 4, Exercise 5) as starting point.

As further practice, extend your algorithm so that it returns whether an item is used in the optimal solution or not. Return a `Dict[Item, bool]` object that assigns `True` to an item if it is put in the knapsack in the optimal solution and `False` if the item is not used. If multiple optimal solutions exist, return only one.

Use the following outline:

```py
from typing import List, Dict


class Item:
    def __init__(self, value: int, weight: int) -> None:
        self.value = value
        self.weight = weight


def knapsack(C: int, items: List[Item], n: int) -> Dict[Item, bool]:
    # TODO
```

Hint: start by calculating the maximum total value.

### Solution

If we only want to compute the maximum total value, the dynamic programming approach is as follows:

```py
from typing import List


class Item:
    def __init__(self, value: int, weight: int) -> None:
        self.value = value
        self.weight = weight


def knapsack(C: int, items: List[Item], n: int) -> float:
    dp_table = [[0] * (C + 1) for _ in range(n + 1)]

    item_idx = 1

    # Note that throughout the loop, `item == items[item_idx - 1]`
    for item in items:

        for capacity in range(1, C + 1):

            # If we can't use the current item, we can only use the previous
            # items
            if capacity < item.weight:
                dp_table[item_idx][capacity] = dp_table[item_idx - 1][capacity]

            # Otherwise, optimize for the maximum total value
            else:
                # option 1: we don't use the current item
                value_no_use = dp_table[item_idx - 1][capacity]

                # option 2: we use the current item
                value_use = (dp_table[item_idx - 1][capacity - item.weight] +
                             item.value)

                dp_table[item_idx][capacity] = max(value_no_use, value_use)

        # increase the item index
        item_idx += 1

    return dp_table[-1][-1]
```

This is very similar to the solution of the coin change problem and there's a good reason for it: the coin change problem is the special variant of the knapsack problem. One difference we should highlight is that in the coin change problem, there are infinitely many coins of each denomination, but in the 0-1 knapsack problem, an item can only be used at most once. Therefore, when we use an item, we cannot use it again, so when we compute the value we would obtain by using the item, the line

```py
value_use = dp_table[item_idx - 1][capacity - item.weight] + item.value
```

points back to the previous row, because in the current row, we can use the current item, and the previous row corresponds to the subproblems where the current item is not available.

When we need to recover the 'path' to the optimal solution, i.e. which items are used, we again go backwards in the DP table. At any position, we ask 'Did we use the item of the row?', which is shown in the solutions of the subproblems (in exactly the same way as in the coin change problem): if we used the item in the optimal solution, the total value that is achievable *without the item* is lower than *with the item*. In the DP table, we compare `dp_table[item_idx][capacity]` (the solution when we use the item) to `dp_table[item_idx - 1][capacity]` (the solution when we don't use the item). If the value in the row above is the same, we don't need this item, otherwise we do, so we simulate the use of this item and continue from a lower capacity.

The full implementation is as follows:

```py
from typing import List, Dict


class Item:
    def __init__(self, value: int, weight: int) -> None:
        self.value = value
        self.weight = weight


def knapsack(C: int, items: List[Item], n: int) -> Dict[Item, bool]:
    dp_table = [[0] * (C + 1) for _ in range(n + 1)]

    item_idx = 1

    # Note that throughout the loop, `item == items[item_idx - 1]`
    for item in items:

        for capacity in range(1, C + 1):

            # If we can't use the current item, we can only use the previous
            # items
            if capacity < item.weight:
                dp_table[item_idx][capacity] = dp_table[item_idx - 1][capacity]

            # Otherwise, optimize for the maximum total value
            else:
                # option 1: we don't use the current item
                value_no_use = dp_table[item_idx - 1][capacity]

                # option 2: we use the current item
                value_use = (dp_table[item_idx - 1][capacity - item.weight] +
                             item.value)

                dp_table[item_idx][capacity] = max(value_no_use, value_use)

        # increase the item index
        item_idx += 1

    # Recovering the 'path' (which items to use)
    capacity_idx = C
    item_idx = n
    item_usage = {item: False for item in items}

    while capacity_idx > 0 and item_idx > 0:
        # Do we need the current item?
        if dp_table[item_idx][capacity_idx] == dp_table[item_idx - 1][capacity_idx]:
            item_idx -= 1
        else:
            item = items[item_idx - 1]
            item_usage[item] = True
            capacity_idx -= item.weight

            # We can't use the item more than once
            item_idx -= 1

    return item_usage
```
