# Complexity Analysis - Solutions

### Exercise 1

For each of the following functions, find the lowest $g(n)$ such that $f(n) = O(g(n))$
1. $f_1(n) = 5n^3 + 7n^2 + 8n^6 + 6n \log n + 2n + 6n^4$
2. $f_2(n) = 7.3\log n + 0.5\sqrt{n} + 1.2\log \log n + 11$
3. $f_3(n) = 10n^3 + 5n + 8n \log n + 3n^7 + 1.3^n$

### Solution

The lowest asymptotic upper bounds are the following:

1. $f_1(n) = O(n^6)$
2. $f_2(n) = O(\sqrt n)$
3. $f_3(n) = O(1.3^n)$

---

### Exercise 2


Using the `matplotlib` library, visualize the above relations! In other words, if $f(n) = O(g(n))$, show that there exist $c$ and $n_0$ positive constants such that $0 \leq f(n) \leq cg(n)$ for all $n \geq n_0$.

Use the following code snippet, which is also included in the file `visualize.py` to get started. The code contains the implementation of all three functions, as well as the `visualize` function that takes two functions $f$ and $g$, generates `n_points` points from `start` with step size `step`, and plots $f(n)$, $cg(n)$ and $n_0$.


```py
import math
from typing import Callable

from matplotlib import pyplot as plt


Function = Callable[[float], float]


def f01(n: float) -> float:
    return (5 * (n ** 3) +
            7 * (n ** 2) +
            8 * (n ** 6) +
            6 * n * math.log(n, 2) +
            2 * n +
            6 * (n ** 4))


def f02(n: float) -> float:
    return (7.3 * math.log(n, 2) +
            0.5 * math.sqrt(n) +
            1.2 * math.log(math.log(n, 2), 2) +
            11)


def f03(n: float) -> float:
    return (10 * (n ** 3) +
            5 * n +
            8 * n * math.log(n, 2) +
            3 * (n ** 7) +
            (1.3 ** n))


def visualize(f: Function,
              g: Function,
              c: float,
              n0: float,
              n_points: int = 1000,
              start: float = 1 + 1e-7,
              step: float = 1
) -> None:
    f_values = [f(start + i * step) for i in range(n_points)]
    g_values = [c * g(start + i * step) for i in range(n_points)]

    plt.plot(f_values, label="$f(n)$")
    plt.plot(g_values, label="$cg(n)$")
    plt.axvline(n0 // step, color="black", label="$n_0$")
    plt.xticks([n0 // step], ["$n_0$"])
    plt.xlabel("$n$")
    plt.ylabel("Function value")
    plt.legend()
    plt.show()

# TODO: visualize f(n) = O(g(n)) relations
```

### Solution

In order to visualize $f_i(n) = O(g_i(n))$ relations, we need to implement the three $g_i$ functions and then, parametrize the `visualize` function with appropriate `c` and `n0` positive constants. Example calls that visualize these relations:

```py
g01 = lambda n: n ** 6
g02 = lambda n: math.sqrt(n)
g03 = lambda n: 1.3 ** n

visualize(f01, g01, c=9, n0=500)
visualize(f02, g02, c=5, n0=270)
visualize(f03, g03, c=1000, n0=100, n_points=105)
```

Note that the visualizations can work with lower (but still high enough) values of `c`, but in this case, `n0` might have to be higher. Similarly, for higher values of `c`, lower `n0` values can work. An example of this with `f03`:

```py
# Original call
visualize(f03, g03, c=1000, n0=100, n_points=105)

# Higher `c`, lower `n0`
visualize(f03, g03, c=10000000, n0=42, n_points=50)

# Lower `c`, higher `n0`
visualize(f03, g03, c=10, n0=979, n_points=1000)
```

---

### Exercise 3

Using the $O$-notation, analyze the time complexity of the following three algorithms.

```py
def algorithm_01(arr: List[int], x: int) -> int:
    c = False

    for i in range(len(arr)):
        if arr[i] == x: c = True

    if not c: return -1

    # Traverse backwards
    for i in range(len(arr) - 1, -1, -1):
        if arr[i] == x: return i

    return -1


def algorithm_02(arr: List[int]) -> int:
    s = 0
    n = len(arr)
    for i in range(500):
        if n > 0: s += arr[0]
        else: s += -1
    return s


def algorithm_03(arr: List[int]) -> None:
    n = len(arr)
    s = 0
    for i in range(0, n):
        for j in range(i + 1, n):
            s += arr[i] * arr[j]
    return arr
```

### Solution

- `algorithm_01`: $O(n)$
- `algorithm_02`: $O(1)$ (note that the `for` loop does 500 iterations regardless of the size of the input)
- `algorithm_03`: $O(n^2)$

---

### Exercise 4

Using the `matplotlib` library, visualize and compare the real runtimes of the algorithms of Exercise 3 on random inputs. Feel free to take inspiration from the code snippet of Exercise 2. Use the following outline:

```py
import random
import time
from typing import List
from matplotlib import pyplot as plt


def alg01_runtime(n: int) -> float:
    """Measures the runtime of `algorithm_01` on a random input of size `n`."""
    arr = list(range(1, n + 1))
    x = random.randint(1, n)

    start_time = time.time()
    algorithm_01(arr, x)
    end_time = time.time()
    return end_time - start_time


def alg02_runtime(n: int) -> float:
    """Measures the runtime of `algorithm_02` on a random input of size `n`."""
    arr = [random.randint(1, n) for _ in range(n)]

    start_time = time.time()
    algorithm_02(arr)
    end_time = time.time()
    return end_time - start_time


def alg03_runtime(n: int) -> float:
    """Measures the runtime of `algorithm_03` on a random input of size `n`."""
    arr = [random.randint(1, n) for _ in range(n)]

    start_time = time.time()
    algorithm_03(arr)
    end_time = time.time()
    return end_time - start_time


def compare_runtimes(n_points: int = 100,
                     start: int = 1,
                     step: int = 100
) -> None:
    # TODO

```

### Solution

An example of comparing the runtimes of all three algorithms visually:

```py
def compare_runtimes(n_points: int = 100,
                     start: int = 1,
                     step: int = 100
) -> None:

    alg01_runtimes = [alg01_runtime(start + i * step) for i in range(n_points)]
    alg02_runtimes = [alg02_runtime(start + i * step) for i in range(n_points)]
    alg03_runtimes = [alg03_runtime(start + i * step) for i in range(n_points)]

    plt.plot(alg01_runtimes, label="algorithm_01 -- $O(n)$")
    plt.plot(alg02_runtimes, label="algorithm_02 -- $O(1)$")
    plt.plot(alg03_runtimes, label="algorithm_03 -- $O(n^2)$")
    plt.legend()
    plt.show()
```

Based on this graph, it might seem that the runtime of `algorithm_01` is constant instead of linear. This is because we are measuring the real runtime, instead of the abstract runtime, and `algorithm_01` primarily consists of simple, hyper-optimized operations. If we amplify the runtimes (e.g. by 1000), we can clearly see a linearly increasing tendency.

---

### Exercise 5

Design and implement an algorithm that takes an array of integers and an integer `x` as its input and find the index of `x` in the array. Create an improved version of your algorithm for the case when the input array is *sorted* (in ascending order). Analyze the time complexity of your algorithms using the $O$-notation. Use the following outline:

```py
from typing import List


def index(arr: List[int], x: int) -> int:
    # TODO
```

### Solution

A simple solution that does not assume the input array is sorted, with a time complexity of $O(n)$:

```py
from typing import List


def index(arr: List[int], x: int) -> int:
    for i in range(len(arr)):
        if arr[i] == x: return i

    return -1
```

Assuming the array is sorted, we can write a solution that runs in $O(\log n)$ time. The following algorithm is also known as binary search:

```py
from typing import List


def index(arr: List[int], x: int) -> int:
    # Initially, `x` can be in the entire array
    l = 0
    r = len(arr) - 1

    while l <= r:
        # Middle of the remaining subarray
        m = (r + l) // 2

        # If `x` is at the middle of the remaining subarray, return `m`
        if arr[m] == x:
            return m

        # If the middle element is lower than `x`, continue the search in the
        # subarray `arr[m + 1 : r]`
        elif arr[m] < x:
            l = m + 1

        # If the middle element is higher than `x`, continue the search in the
        # subarray `arr[l : m - 1]`
        else:
            r = m - 1

    # If `x` is not in `arr`, return an error code
    return -1
```

---

### Exercise 6

Design and implement an algorithm that calculates the inner product of two 1-dimensional vectors of $n$ elements. Analyze your algorithm's time complexity using the $O$-notation. Use the following outline:

```py
from typing import List


def inner_product(vec1: List[int], vec2: List[int]) -> int:
    # TODO
```

### Solution

A solution with a time complexity of $O(n)$:

```py
from typing import List


def inner_product(vec1: List[int], vec2: List[int]) -> int:
    prod = 0
    for i in range(len(vec1)):
        prod += vec1[i] * vec2[i]
    return prod
```

---

### Exercise 7

Design and implement an algorithm that multiplies two 2-dimensional square matrices of $n \times n$ size. Analyze your algorithm's time complexity using the $O$-notation. Use the following outline:

```py
from typing import List


Matrix = List[List[int]]
def matmul(mat1: Matrix, mat2: Matrix) -> Matrix:
    # TODO
```

### Solution

A solution with a time complexity of $O(n^3)$:

```py
from typing import List


Matrix = List[List[int]]
def matmul(mat1: Matrix, mat2: Matrix) -> Matrix:
    # Initialize result matrix
    n = len(mat1)
    res = [[0 for _ in range(n)] for _ in range(n)]

    # Compute each element of the result matrix
    for i in range(n):
        for j in range(n):

            # Inner product
            for k in range(n):
                res[i][j] += mat1[i][k] * mat2[k][j]

    return res
```

---

### Exercise 8

Design and implement an algorithm that returns all subsets of a set of $n$ numbers. Analyze your algorithm's time complexity using the $O$-notation. Use the following outline:

```py
from typing import List, Set


def subsets(nums: Set[int]) -> List[Set[int]]:
    # TODO
```

### Solution

A solution with a time complexity of $O(2^n)$:

```py
from typing import List, Set

def subsets(nums: Set[int]) -> List[Set[int]]:
    # The empty set is a subset of every set
    result_subsets = [set()]

    for elem in nums:

        # Extend every previous subset with the current element
        extended_subsets = []

        for subset in result_subsets:
            new_subset = subset.copy()
            new_subset.add(elem)
            extended_subsets.append(new_subset)

        # Add the extended subsets to the previous subsets
        result_subsets.extend(extended_subsets)

    return result_subsets
```
