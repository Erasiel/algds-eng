# Complexity Analysis

### Exercise 1

What are the time complexities of the following three algorithms? Use the $O$-notation.

```py
from typing import List


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

---

### Exercise 2

Design and implement an algorithm that takes a list of integers and an integer $x$ as its input and returns the index of $x$ in the list, or -1 if it is not in the list. Analyze the time complexity of your algorithm using the $O$-notation.

---

### Exercise 3

Design and implement an algorithm that takes a **sorted** list of integers and an integer $x$ as its input and returns the index of $x$ in the list, or -1 if it is not in the list. Analyze the time complexity of your algorithm using the $O$-notation.

---

### Exercise 4

Design and implement an algorithm that calculates the inner product of two 1-dimensional vectors of $n$ elements. Analyze the time complexity of your algorithm using the $O$-notation.

---

### Exercise 5

Design and implement an algorithm that multiplies two 2-dimensional square matrices of $n \times n$ size. Analyze the time complexity of your algorithm using the $O$-notation.

---

### Exercise 6

Design and implement an algorithm that returns all subsets of a set of $n$ numbers. Analyze the time complexity of your algorithm using the $O$-notation.
