# The Divide and Conquer Paradigm

### Exercise 1

Design and implement **recursive** algorithms for the following problems:
1. Factorial calculation
2. Computing the n-th Fibonacci number
3. Reversing a string
4. Finding the index of a number in a sorted list of numbers (binary search)

Use the following outlines:

```py
def factorial(n: int) -> int:
    # TODO
```

```py
def fibonacci(n: int) -> int:
    # TODO
```

```py
from typing import Optional


def reverse(s: str, idx: Optional[int] = None) -> int:
    # TODO

# Example call
reverse("tartar sauce")
```

```py
from typing import List, Optional


def index(arr: List[int],
          x: int,
          r: Optional[int] = None,
          l: Optional[int] = None
) -> int:
    # TODO

# Example call
index([1, 2, 3, 4, 5], 4)
```

---

### Exercise 2

Our goal is to get to the top of the $n$-th step in a very long flight of stairs. We can only move either one or two steps with at a time and we can not go backwards. Design and implement a recursive algorithm that finds the number of distinct movement sequences we can take to get to get on top of the $n$-th step. Use the following outline:

```py
def steps(n_steps: int) -> int:
    # TODO
```

Example: if $n=3$, the answer is 3. We can either move 1 step 3 times, move 2 steps followed by a 1-step move or move 1 step followed by a 2-step move.

---

### Exercise 3

On a custom chess board with $n \times m$ positions, we want to move from the top-left corner to the bottom-right corner. We can only move one position down or right at a time and we can not go backwards. Design and implement a recursive algorithm that finds the number of distinct movement sequences we can take to get to get to the top-right corner. Use the following outline:

```py
def board(n: int, m: int) -> int:
    # TODO
```

Example: if $n=m=2$, the answer is 2. We can either start by moving up, followed by a right move, or start with a right move, followed by a move up.

---

### Exercise 4

Using the $O$-notation, analyze the time complexity of the algorithms of the following previous exercises:

- Exercise 1.1: `factorial`
- Exercise 1.3: `reverse`
- Exercise 1.4: `index`
- Exercise 2: `steps`
- Exercise 3: `board`

---

### Exercise 5

*Note: the description of the following exercise is not based on real events and any similarity to real life is merely coincidental.*

A pirate named Andras got very drunk once and Captain Mark decided to throw him overboard. Luckily for Andras, the crew instead decided to leave him on the $(x, y)$ position of an island that happens to be a perfect rectangle of $n \times m$ positions. Captain Mark shows mercy and offers Andras a deal: if, after $k$ moves, Andras is still on the island, he will take him back on board. However, Andras is still very drunk so he cannot control his movement, and the island is surrounded by sharks who will eat him the moment he steps off the island.

The movement of Andras is very restricted, he can only move one position up, down, left, or right at a time, and he cannot move diagonally. He is moving perfectly randomly, meaning the chance of the four possible moves is equal. Design and implement a recursive algorithm that calculates the probability of survival for our drunken pirate after $k$ steps. Assume the positions on the island start with $(1, 1)$ and end with $(n, m)$. Use the following outline:

```py
def survival(n: int, m: int, x: int, y: int, k: int) -> float:
    # TODO
```

Example: if $n=m=2$, $x=y=1$ and $k=1$, the answer is 0.5. That is because with Andras will step to positions $(0, 1)$, $(1, 0)$, $(1, 2)$ and $(2, 1)$ with a 25% chance each, so in 50% of the cases he will step off the island.

---

### Exercise 6

Implement the merge sort algorithm using recursion. Using the $O$-notation, analyze the time complexity of your implementation. Use the following outline:

```py
from typing import List


def merge_sort(arr: List[int]) -> List[int]:
    # TODO
```
