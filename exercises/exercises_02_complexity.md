# Complexity Analysis

### Exercise 1

For each of the following functions, find the lowest $g(n)$ such that $f(n) = O(g(n))$
1. $f_1(n) = 5n^3 + 7n^2 + 8n^6 + 6n \log n + 2n + 6n^4$
2. $f_2(n) = 7.3\log n + 0.5\sqrt{n} + 1.2\log \log n + 11$
3. $f_3(n) = 10n^3 + 5n + 8n \log n + 3n^7 + 1.3^n$

---

### Exercise 2


Using the `matplotlib` library, visualize the above relations! In other words, if $f(n) = O(g(n))$, show that there exist $c$ and $n_0$ positive constants such that $0 \leq f(n) \leq cg(n)$ for all $n \geq n_0$.

Use the following code snippet, which is also included in the file `visualize.py` to get started. The code contains the implementation of all three functions, as well as the `visualize` function that takes two functions $f$ and $g$, generates `n_points` points from `start` with step size `step`, and plots $f(n)$, $cg(n)$ and $n_0$.


```py
import math
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

---

### Exercise 3

Using the $O$-notation, analyze the time complexity of the following algorithms.

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
```

```py
def algorithm_02(arr: List[int]) -> int:
    s = 0
    n = len(arr)
    for i in range(500):
        if n > 0: s += arr[0]
        else: s += -1
    return s
```

```py
def algorithm_03(n: int) -> None:
    for i in range(1, n + 1):
        for j in range(i + 1, n + 1):
            print(f"{i}, {j}")
```

---

### Exercise 4

Design and implement an algorithm that takes an array of integers and an integer `x` as its input and find the index of `x` in the array. Create an improved version of your algorithm for the case when the input array is *sorted* (in ascending order). Analyze the time complexity of your algorithms using the $O$-notation. Use the following outline:

```py
def index(arr: List[int], x: int) -> int:
    # TODO
```

---

### Exercise 5

Design and implement an algorithm that calculates the inner product of two 1-dimensional vectors of $n$ elements. Analyze your algorithm's time complexity using the $O$-notation. Use the following outline:

```py
def inner_product(vec1: List[int], vec2: List[int]) -> int:
    # TODO
```

---

### Exercise 6

Design and implement an algorithm that multiplies two 2-dimensional square matrices of $n \times n$ size. Analyze your algorithm's time complexity using the $O$-notation. Use the following outline:

```py
Matrix = List[List[int]]
def matmul(mat1: Matrix, mat2: Matrix) -> Matrix:
    # TODO
```

---

### Exercise 7

Design and implement an algorithm that returns all subsets of a set of $n$ numbers. Analyze your algorithm's time complexity using the $O$-notation. Use the following outline:

```py
def subsets(nums: Set[int]) -> List[Set[int]]:
    # TODO
```
