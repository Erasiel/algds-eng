# Greedy Algorithms

### Exercise 1

Design a simple greedy algorithm for the point collection problem (week 4, exercise 4). Define the greedy choice and show that by making the greedy choice, only one subproblem remains. Show that your algorithm is *not* optimal.

---

### Exercise 2

Design a simple greedy algorithm for the coin change problem (week 4, exercise 5). Define the greedy choice and show that by making the greedy choice, only one subproblem remains. Show that your algorithm is *not* optimal.

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
