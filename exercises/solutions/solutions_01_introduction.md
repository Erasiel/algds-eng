# Introduction - Solutions

Exercises 1-5 don't have shareable solutions. Make sure you know your h-id (`hxxxxxx`) and you can mount your `home` directory by calling `mount` and logging in. Afterwards, the `/home/hxxxxxx` directory will become available. Also make sure to send your h-id to the lab instructor via email or CooSpace message.

If you have any problems with mounting, contact the lab instructor.

---

### Exercise 6

What's wrong with the Python code snippet below? How would you fix it?

```py
def func(a, b, c):
    return a[0] + b[0] * c
```

### Solution

Even with a simple function like this, many things are wrong. First of all, neither the function name, nor the parameters hint at their purpose. We don't know what the function is intended to do, and what the parameters' types actually are. All we know is that `a` and `b` are supposed to be subscriptable (indexable). For now, we can suppose both are lists. With fixing these issues, we arrive at the following snippet:

```py
def add_firsts(list1, list2, c):
    return list1[0] + list2[0] * c
```

Obviously, the new function name is a bit misleading, because we multiply `list2[0]` with `c`. Having the function name contain this information would result in a very clunky name, so instead, we can document the code like so:

```py
def add_firsts(list1, list2, c):
    """
    Returns the sum of the first element of `list2` multiplied by `c` and the
    first element of `list1`.
    """
    return list1[0] + list2[0] * c
```

Now, we are nearly there, the last thing we're missing is type hinting. We want to hint at the types of parameters and the type of the returned value. With some assumptions, we can write:

```py
def add_firsts(list1: list, list2: list, c: float) -> float:
    """
    Returns the sum of the first element of `list2` multiplied by `c` and the
    first element of `list1`.
    """
    return list1[0] + list2[0] * c
```

However, this is still not good enough. If we want to do type hints (and every self-respecting developer wants to do type hints), we have to make them more detailed. Simply hinting that a variable or parameter is a `list` is not very useful, because we don't know what types of values the list contains. Detailed type hinting uses the `typing` package, that supports a wide variety of types. We can hint at the type of elements in the lists in the following way:

```py
from typing import List


def add_firsts(list1: List[float], list2: List[float], c: float) -> float:
    """
    Returns the sum of the first element of `list2` multiplied by `c` and the
    first element of `list1`.
    """
    return list1[0] + list2[0] * c
```

Here, `List[float]` hints that the list contains only real numbers. Python does not check these types by default, but you can set up your editor / IDE, or run third-party libraries to do so, with varying levels of strictness. Most large Python codebases have similar type hinting, so getting familiar with the `typing` package is heavily recommended.

---

### Exercise 7

Write Python functions that solve the following tasks:
1. Given three integers, `a`, `b` and `c`, determines if $a \in [b, c]$
2. Given a binary string `s`, replaces all zeros with ones and all ones with zeros.
3. Given a list of integers, where every element of the list is between 0 and 9, finds the most frequent element of the list.
4. Determines the number of unique characters in a string.
5. Calculates the mean of a 2-dimensional matrix of real numbers.

Use the principles discussed in the previous exercise.

### Solution

For these simple exercises, we'll omit documentation and other comments.

1\. The implementation is very simple, just pay attention to type hinting:

```py
def interval_contains(a: int, b: int, c: int) -> bool:
    return b <= a <= c
```

2\. A simple solution:

```py
def invert_binary_string(s: str) -> str:
    inverted_s = ""

    for char in s:
        if char == "0": inverted_s += "1"
        else:           inverted_s += "0"

    return inverted_s
```

3\. A simple solution:

```py
def most_frequent(numbers: List[int]) -> int:
    freqs = [0] * 10
    max_freq_num = 0

    for num in numbers:
        freqs[num] += 1
        if freqs[num] > freqs[max_freq_num]:
            max_freq_num = num

    return max_freq_num
```

More elegant solutions can use a `dict` (or even a `collections.defaultdict`) to count frequencies.

4\. A simple solution:

```py
def num_unique_chars(s: str) -> str:
    unique_chars = []

    for char in s:
        if char not in unique_chars:
            unique_chars.append(char)

    return len(unique_chars)
```

A more elegant solution, using a `set`:
```py
def num_unique_chars(s: str) -> str:
    unique_chars = set()

    for char in s:
        unique_chars.add(char)

    return len(unique_chars)
```

5\. Here, again, we need to pay attention to type hints. To type hint a two-dimensional matrix of real values, we can use `List[List[float]]` (which hints at a list containing of lists that contain real numbers). A complete implementation also handles empty matrices (whose mean is `NaN`).

```py
def matrix_mean(matrix: List[List[float]]) -> float:
    n = len(matrix)
    m = len(matrix[0])

    if n == 0 or m == 0: return float("nan")

    sum_values = 0

    for i in range(n):
        for j in range(m):
            sum_values += matrix[i][j]

    return sum_values / (n * m)
```
