# The Divide and Conquer Paradigm - Solutions

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


def reverse(s: str, idx: Optional[int] = None) -> str:
    # TODO

# Example call
reverse("tartar sauce")
```

```py
from typing import List, Optional


def index(arr: List[int],
          x: int,
          l: Optional[int] = None,
          r: Optional[int] = None
) -> int:
    # TODO

# Example call
index([1, 2, 3, 4, 5], 4)
```

### Solution

1\. We convert the definition of $n!$ to a recursive definition in the following way: $n! = n \cdot (n - 1) \cdot (n - 2) \cdot ... \cdot 2 \cdot 1 = n \cdot (n-1)!$. While we could consider $n = 1$ as the base case, $0!$ is not only a valid expression, but its value is also 1, so $n = 0$ is the cleanest choice for the base case.

```py
def factorial(n: int) -> int:
    if n < 0:
        raise ValueError("The factorial of a negative number is undefined!")
    if n == 0:
        return 1
    return n * factorial(n - 1)
```

2\. The Fibonacci sequence is already defined recursively as follows: $\text{fib}(n) = \text{fib}(n - 1) + \text{fib}(n - 2)$ with two base cases $\text{fib}(0) = 0$ and $\text{fib}(1) = 1$. Its implementation is therefore very simple:

```py
def fibonacci(n: int) -> int:
    if n < 0:
        raise ValueError("The Fibonacci sequence does not support negative "
                         "indices!")

    if n == 0: return 0
    if n == 1: return 1
    return fibonacci(n - 1) + fibonacci(n - 2)
```

3\. We will use the `idx` variable similar to a loop variable, and the loop will be simulated with recursive calls. We therefore implement the `reverse` function so that `reverse(s, idx)` will return the reverse of `s[idx:]`. As suggested by the example call, the `idx` parameter is optional, and when it is `None` we reverse the whole string (by setting `idx` to zero).

```py
from typing import Optional


def reverse(s: str, idx: Optional[int] = None) -> str:
    if idx is None: idx = 0
    if idx >= len(s): return ""

    return reverse(s, idx + 1) + s[idx]
```

4\. As a starting point, one can use the implementation of the binary search algorithm from the previous week. That implementation was iterative (i.e. it used a loop instead of recursion), so we have to use the same principles as in Exercise 1.3 to convert the loop into a simple recursion:

```py
from typing import List, Optional


def index(arr: List[int],
          x: int,
          l: Optional[int] = None,
          r: Optional[int] = None
) -> int:
    # Initially, `x` can be in the entire array
    if r is None: r = len(arr) - 1
    if l is None: l = 0

    # Base case: we exhausted all possible indices of the list
    if l > r: return -1

    # Middle of the remaining subarray
    m = (r + l) // 2

    # If `x` is at the middle of the remaining subarray, return `m`
    if arr[m] == x:
        return m

    # If the middle element is lower than `x`, continue the search in the
    # subarray `arr[m + 1 : r]`
    elif arr[m] < x:
        return index(arr, x, m + 1, r)

    # If the middle element is higher than `x`, continue the search in the
    # subarray `arr[l : m - 1]`
    else:
        return index(arr, x, l, m - 1)
```

---

### Exercise 2

Our goal is to get to the top of the $n$-th step in a very long flight of stairs. We can only move either one or two steps at a time and we can not go backwards. Design and implement a recursive algorithm that finds the number of distinct movement sequences we can take to get to get on top of the $n$-th step.

**Constraints**
- $n > 0$

Use the following outline:

```py
def steps(n_steps: int) -> int:
    # TODO
```

Example: if $n=3$, the answer is 3. We can either move 1 step 3 times, move 2 steps followed by a 1-step move or move 1 step followed by a 2-step move.

### Solution

Firstly, the constraints specify that `n_steps` is always positive, so we don't have to handle non-positive values.

In calculating the number of distinct movement sequences to the $n$-th step we only need to calculate the same for the $n-1$-st and the $n-2$-nd steps, as these are the two steps from which we can step directly onto the $n$-th step. By solving these two smaller subproblems and adding their solutions, we get the solution to the $n$-th step's problem.

This idea allows us to ignore any step that isn't the $n-1$-st or the $n-2$-nd, as their solutions will be calculated by further dividing the smaller subproblems and therefore they indirectly contribute to the solution of the $n$-th step's problem.

Finally, to avoid infinite recursion, we need a proper base case. In this exercise, simply handling one value of $n$ as a base case (e.g. $n = 1$) will still lead to infinite recursion, so we need (at least) two base cases. It's easy to see that `steps(1)` has to return 1 and `steps(2)` has to return 2, and we can implement these directly as base cases.

The final implementation is very similar to the Fibonacci number implementation (Exercise 1.2):

```py
def steps(n_steps: int) -> int:
    if n_steps == 1: return 1
    if n_steps == 2: return 2

    return steps(n_steps - 1) + steps(n_steps - 2)
```

---

### Exercise 3

On a custom chess board with $n \times m$ positions, we want to move from the top-left corner to the bottom-right corner. We can only move one position down or right at a time and we can not go backwards. Design and implement a recursive algorithm that finds the number of distinct movement sequences we can take to get to get to the bottom-right corner.

**Constraints**
- $n, m > 0$

Use the following outline:

```py
def board(n: int, m: int) -> int:
    # TODO
```

Example: if $n=m=2$, the answer is 2. We can either start by moving down, followed by a right move, or start with a right move, followed by a move down.


### Solution

We can apply the same logic we used in Exercise 2 here. When calculating the number of distinct movement sequences to the position $(i, j)$, we only need to consider two positions: its left and top neighbor, i.e. the positions $(i-1, j)$ and $(i, j-1)$. Calculating the solutions to these two smaller subproblems and adding them will yield the solution to the $(i, j)$ position's problem.

The base case is a little trickier than before. We have to notice that in both the first (left) column and the first (top) row, we have only one movement option. In the first column we can only move down, and in the first row we can only move right. Therefore, the solution to any position in the first row and the first column will be 1.

The final implementation is almost embarassingly simple:

```py
def board(n: int, m: int) -> int:
    if n == 1 or m == 1: return 1
    return board(n - 1, m) + board(n, m - 1)
```

---

### Exercise 4

Using the $O$-notation, analyze the time complexity of the algorithms of the following previous exercises:

- Exercise 1.1: `factorial`
- Exercise 1.3: `reverse`
- Exercise 1.4: `index`
- Exercise 2: `steps`
- Exercise 3: `board`

### Solution

We will use the recursion tree method in all cases. The recursion tree shows the recursive calls made by each function call during a recursive algorithm's execution.

When analyzing the running time, we look at two things: the number of levels in the tree (also known as the *depth* of the tree), and each level's total running time. The number of levels can be figured out by analyzing how much each recursive call reduces the size of the subproblem.

To calculate a level's running time, we need to figure out the runtime of each individual function call by analyzing its complexity without the recursive calls (we can pretend that instead of the calls, the function uses the values returned by these calls). Once we have a function's individual runtime, a level's total runtime is the sum of the running times of all functions on that level.

Finally, the total running time of a recursive function is the sum of the running time of all levels. When the running time of all levels are the same, this formula reduces to the number of levels multiplied by a level's running time.

`factorial`:<br/>
The function's individual runtime is constant. During recursion, each function performs one recursive call that reduces the parameter by 1, so the depth of the recursion is $n$, where $n$ is the original parameter. Since there's only one function call on each level, each level's running time is constant, so the total runtime is $O(n)$.

`reverse`:<br/>
Same as `factorial`.

`index`:<br/>
The function's individual runtime is constant. During recursion, each function performs one recursive call that reduces the length of the relevant subarray by half, so the depth of the recursion is $\log n$, where $n$ is the length of the list. The total runtime is $O(\log n)$.

`steps`:<br/>
The function's individual runtime is constant. During recursion, each function performs two recursive calls. The first reduces the parameter by 1, the second by 2, so the first will be responsible for the depth of the recursion tree, which will be $n$. In the recursive case, each function will create two recursive function calls, so the number of calls on each level of the recursion tree is *roughly* double that of the previous level. Given that the depth of the recursion is linear in the value of $n$, the "doubling function calls" make this algorithm's complexity $O(2^n)$.

The more keen-eyed can notice that the decrease in the function's parameters is not uniform, and therefore not every path from the root to a leaf in the call tree will have a length of $n$. For example, if we follow the path where we always reduce the parameter by two, we would encounter only $n/2$ function calls. With a more detailed analysis (which would involve a lot more math), we could reduce the initial upper bound of $O(2^n)$ to a slightly lower $O(1.618^n)$. For our current level, the naive analysis is sufficient.

`board`:<br/>
Before we begin, we have to note that the running time depends on *two* parameters, namely the values of $n$ and $m$. Knowing this, we can use the same logic as with the `steps` function. The function's individual runtime is constant, the depth of the recursion will be $O(n + m)$, and the "doubling function calls" make this algorithm's complexity $O(2^{n + m})$

---

### Exercise 5

*Note: the description of the following exercise is not based on real events and any similarity to real life is merely coincidental.*

A pirate named Andras got very drunk once and Captain Mark decided to throw him overboard. Luckily for Andras, the crew instead decided to leave him on the $(x, y)$ position of an island that happens to be a perfect rectangle of $n \times m$ positions. Captain Mark shows mercy and offers Andras a deal: if, after $k$ moves, Andras is still on the island, he will take him back on board. However, Andras is still very drunk so he cannot control his movement, and the island is surrounded by sharks who will eat him the moment he steps off the island.

The movement of Andras is very restricted, he can only move one position up, down, left, or right at a time, and he cannot move diagonally. He is moving perfectly randomly, meaning the chance of the four possible moves is equal. Design and implement a recursive algorithm that calculates the probability of survival for our drunken pirate after $k$ steps. Assume the positions on the island start with $(1, 1)$ and end with $(n, m)$.

**Constraints:**
- $n, m > 0$
- $1 \leq x\leq n,\; 1 \leq y \leq m$
- $k \geq 0$

Use the following outline:

```py
def survival(n: int, m: int, x: int, y: int, k: int) -> float:
    # TODO
```

Example: if $n=m=2$, $x=y=1$ and $k=1$, the answer is 0.5. That is because with Andras will step to positions $(0, 1)$, $(1, 0)$, $(1, 2)$ and $(2, 1)$ with a 25% chance each, so in 50% of the cases he will step off the island.

### Solution

Again, we graciously believe the constraints, so we won't check the validity of the parameters in the implementation.

Coming up with a solution requires finding a way to divide a problem into smaller subproblems. A method for this can usually be figured out by analyzing the parameters and finding those that correspond to the size of the problem.

Importantly, there are usually parameters that don't only change the size of the problem, but the problem as a whole. A great example for this is the size of the island, given by the parameters $n$ and $m$. Reducing these might seem like a good choice, but in reality this changes the problem entirely, as all of a sudden you're trying to answer the same question but on a completely different island. Similarly, only changing the position of the character, i.e. $x$ and $y$ changes the problem entirely, and might not even result in a smaller subproblem.

The important parameter that definitely corresponds to the size of the problem is the value $k$, i.e. the number of remaining steps. We can easily see that once this parameter is low enough, the problem is solved: if $k = 0$ and the character is still on the island, the solution is 1. Of course, initially, $k$ might be more than 0, in which case we have to reduce it to get a smaller subproblem. In this case, we simulate moves until $k$ is 0. Importantly, moves can randomly go in all four directions, so in simulating a move we have to look at all four possible directions separately.

To summarize, with $k>0$ remaining moves, at position $(x, y)$, the character has 0.25 chance to go to either of the following positions: $(x+1, y), (x-1, y), (x, y+1), (x, y-1)$. Once either of these moves has been made, the number of remaining moves is reduced by 1.

Finally, we have to handle another base case: stepping off the island. There is no coming back from this, so when the coordinates of the character suggest that they stepped off the island, the chance of survival is 0.

The final implementation is, again, very simple:

```py
def survival(n: int, m: int, x: int, y: int, k: int) -> float:
    # Cover the case where the character steps off the island
    if x < 1 or x > n or y < 1 or y > m: return 0

    # When there are no remaining moves and the character is still on the
    # island, the chance of survival is 1
    if k == 0: return 1

    # Simulate a move in all 4 directions with equal chances, and reduce the
    # number of remaining moves
    return (survival(n, m, x + 1, y, k - 1) * 0.25 +
            survival(n, m, x - 1, y, k - 1) * 0.25 +
            survival(n, m, x, y + 1, k - 1) * 0.25 +
            survival(n, m, x, y - 1, k - 1) * 0.25)
```

---

### Exercise 6

Implement the merge sort algorithm using recursion. Using the $O$-notation, analyze the time complexity of your implementation. Use the following outline:

```py
from typing import List


def merge_sort(arr: List[int]) -> List[int]:
    # TODO
```

### Solution

This algorithm is extensively covered in the lecture, so here, we only highlight the basics. The idea is to sort the array by halving the array, recursively sorting the two half-arrays and merging them together in sorted order. The base case is quite simple: if the array contains at most one element, it is already sorted. Otherwise we split, sort recursively and merge in sorted order.

The splitting process is quite simple, we find the middle index and splice the array accordingly. The two half-arrays are then sorted recursively and we just need to merge them in sorted order. We use one index variable for each subarray, namely `left_idx` and `right_idx`, initially set to 0. We proceed by deciding between merging `left_arr[left_idx]` or `right_arr[right_idx]` into the merged, sorted array, and increasing the corresponding index afterwards. Finally, because the initial split may result in arrays whose lengths are different (e.g. consider an array of length 7), we merge any remaining subarray that hasn't been merged, and then return the merged, sorted array.

The full implementation is as follows:

```py
from typing import List


def merge_sort(arr: List[int]) -> List[int]:
    # Base case: an empty array, or a one-element array is already sorted
    if len(arr) <= 1: return arr

    # Divide the input array into two half-arrays
    m = len(arr) // 2
    left_arr = arr[:m]
    right_arr = arr[m:]

    # Sort them recursively
    left_arr = merge_sort(left_arr)
    right_arr = merge_sort(right_arr)

    # Merge the two sorted half-arrays
    left_arr_idx = 0
    right_arr_idx = 0
    merged_arr = [0] * (len(left_arr) + len(right_arr))
    merged_arr_idx = 0

    while left_arr_idx < len(left_arr) and right_arr_idx < len(right_arr):
        if left_arr[left_arr_idx] < right_arr[right_arr_idx]:
            merged_arr[merged_arr_idx] = left_arr[left_arr_idx]
            left_arr_idx += 1
        else:
            merged_arr[merged_arr_idx] = right_arr[right_arr_idx]
            right_arr_idx += 1
        merged_arr_idx += 1

    # If there are remaining elements in one half-array, append them to the
    # merged array. Note that at most one of the following while loops will be
    # executed.
    while left_arr_idx < len(left_arr):
        merged_arr[merged_arr_idx] = left_arr[left_arr_idx]
        left_arr_idx += 1
        merged_arr_idx += 1

    while right_arr_idx < len(right_arr):
        merged_arr[merged_arr_idx] = right_arr[right_arr_idx]
        right_arr_idx += 1
        merged_arr_idx += 1

    return merged_arr
```

When analyzing the running time, we have to note that the individual running time of the function is *linear* in the length of the parameter array. In the recursive case, the function makes two recursive calls, with both receiving half of the parameter array. This immediately shows that the depth of the recursion is $O(\log n)$, where $n$ is the initial length of the array.

Analyzing each level can be a bit tricky here. The first level's running time is obviously $O(n)$. On the second level, there are two function calls, each of which operating on an array of size $\approx n/2$. Because the function's running time is linear in the length of the array, the total running time of these two functions is roughly $c\cdot n/2 + c \cdot n/2 = O(n)$. On the third level, there are four function calls, and each of them operate on an array of size $\approx n/4$, so the total running time of this level is roughly $4 \cdot (c\cdot n/4) = O(n)$. We could do the same for all levels, but at this point it should be clear that each level's running time is $O(n)$. Since we have $O(\log n)$ levels, the total running time of the algorithm is $O(n \log n)$.
