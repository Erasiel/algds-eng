# Sample Test 1

**Before you begin**

During the test, you don't have access to any website other than CooSpace. In the `algds_test` folder, you are given all practice materials (including solutions), all slides of the lecture, the fourth edition of the Introduction to Algorithms book, and the test itself.

Before you start writing the test, mount your home directory (the `/home/hxxxxxx` directory). Any work in this directory will be automatically saved during the time of the test and is recoverable during and after the test by the instructor. Your solutions should be submitted through the CooSpace system, but files in your home directory can be considered if you fail to upload them. **All files outside your home directory are not secure during the test and will be lost when you shut down your PC.**

You are given four tasks, each worth exactly 8 points. **You have to choose three tasks to complete.** The choice is entirely up to you, but you can only get points for three tasks. You won't get extra points for attempting all four tasks. You can earn up to 24 points in this test, and, as per the requirements, you have to earn at least 8.

Feel free to use built-in data structures (e.g. `set`, `list`, `dict`) and algorithms (e.g. `sort`, `index`) unless specified otherwise.

Each task contains a set of test cases as examples, but be aware that just because your algorithm passes all the example tests, it might not be correct. You are encouraged to write further test cases (specifically to test edge cases), but this is not required. You don't have to test the type of input parameters in your implementation, everything is as seen in the type hints.

You have 110 minutes to complete your work. You can upload your solutions in CooSpace either as separate files for each task, or as one file.

Good luck!

---

### Task 1 - Number of ones

Design and implement an algorithm that calculates the number of ones in a sorted binary array (i.e. an array that only contains ones and zeros). Note that the input can be sorted in either ascending or descending order. Make sure your algorithm runs in at most $O(\log n)$ time, where $n$ is the length of the array.

Use the following outline:

```py
def number_of_ones(arr: List[int], n: int) -> int:
    # TODO
    pass
```

Tests:
```py
assert number_of_ones([0, 0], 2) == 0
assert number_of_ones([1, 1], 2) == 2
assert number_of_ones([0, 0, 1, 1, 1, 1, 1], 7) == 5
assert number_of_ones([1, 1, 1, 1, 1, 0, 0], 7) == 5
```

---

### Task 2 - Coin change possibilities

You are given an amount of money $F$ and a set of denominations $P = \{ p_1, ..., p_n\}$, with an infinite number of coins of each denomination. Design and implement an algorithm that calculates the number of different coin combinations *irrespective of the order of coins* that add up to $F$. Two combinations are different if they are not permutations of each other. Make sure your algorithm's time complexity is polynomial in $|P|$ and $F$.

Use the following outline:

```py
def coin_change_possibilities(F: int, P: Set[int], n: int) -> int:
    # TODO
    pass
```

Tests:

```py
assert coin_change_possibilities(10, {1}, 1) == 1
assert coin_change_possibilities(10, {1, 5}, 2) == 3
assert coin_change_possibilities(10, {1, 5, 7}, 3) == 4
```

Explanations: In all cases, we have 10 money.
1. In the first case, we can only use coins that are worth 1, so the only way to change 10 money is by using 10 pieces of this coin.
2. When we can use denominations of 1 and 5, the 3 ways of changing 10 money are:
    - 10*1
    - 5*1 + 1\*5
    - 2*5
3. When we can use the 7 denomination, along with the previous three possibilities, we can also change 3*1 + 1\*7, leading to four possibilities.

---

### Task 3 - Making up for lost time

Instead of doing housework, you wasted your precious time playing video games, to the point where you have only one day to do your chores. Unfortunately, every one of your tasks can only be completed in a specific time of day, but as an experienced procrastinator, you know exactly how long each task takes to complete. Of course, some tasks overlap. You can only work on one task at a time, and you can't pause a task to return to it later. Your job is to complete as many tasks as possible.

Your input is a list of two-element tuples `(start, end)`, where both `start` and `end` are strings in the form of `hh:mm` representing valid timestamps (e.g. `09:15`), and a number $n$, which is the length of the list. Design and implement an algorithm that determines the maximum number of tasks you can complete. Make sure your algorithm runs in at most $O(n \log n)$ time.

Use the following outline:

```py
def max_tasks(tasks: List[Tuple[str, str]], n: int) -> int:
    # TODO
    pass
```

Tests:

```py
assert max_tasks([("09:15", "09:45"), ("09:45", "13:00")], 2) == 2
assert max_tasks([("09:15", "09:45"), ("09:30", "13:00")], 2) == 1
assert max_tasks([("09:15", "09:45"), ("09:30", "13:00"), ("10:00", "18:00")], 2) == 2
```

Explanations:
1. In this case, you can start the second task right after finishing the first, so there's no overlap and you can complete both tasks.
2. Now the two tasks overlap, so you can only complete one.
3. In this case, the second task overlaps with both the first and the third, but the first and the third tasks don't overlap. The best course of action is to ignore the second task and complete the first and the third.

---

### Task 4 - RPN evaluation

Design and implement an algorithm that evaluates an arithmetic expression that is in Reverse Polish Notation (RPN). The input is a list of strings and numbers, where every element of the list is one of the following:
- One of the four basic arithmetic operators: `"+"`, `"-"`, `"*"`, `"/"`
- A real number of type `float`

Examples of RPN:
| Original (infix) formula      | Reverse Polish Notation | Input of the algorithm                                    | Solution |
|-------------------------------|-------------------------|-----------------------------------------------------------|----------|
| `5 * 4 + 3`                   | `5 4 * 3 +`             | `[5.0, 4.0, "*", 3.0, "+"]`                               | 23       |
| `5 + 4 * 3`                   | `5 4 3 * +`             | `[5.0, 4.0, 3.0, "*", "+"]`                               | 17       |
| `5 * 4 + 3 * 2`               | `5 4 * 3 2 * +`         | `[5.0, 4.0, "*", 3.0, 2.0, "*", "+"]`                     | 32       |
| `(5 + 3) / (4 - 2)`           | `5 3 + 4 2 - /`         | `[5.0, 3.0, "+", 4.0, 2.0, "-", "/"]`                     | 4        |
| `((1 + 2) * 3 + 6) / (8 - 5)` | `1 2 + 3 * 6 + 8 5 - /` | `[1.0, 2.0, "+", 3.0, "*", 6.0, "+", 8.0, 5.0, "-", "/"]` | 5        |

The algorithm also receives $n$, the length of the list, as its input. Make sure your algorithm runs in at most $O(n)$ time. Use the following outline:

```py
def rpn_eval(rpn: List[Union[str, float]], n: int) -> float:
    # TODO
    pass
```

Tests:
```py
assert rpn_eval([5.0, 4.0, "*", 3.0, "+"], 5) == 23
assert rpn_eval([5.0, 4.0, 3.0, "*", "+"], 5) == 17
assert rpn_eval([5.0, 4.0, "*", 3.0, 2.0, "*", "+"], 7) == 32
assert rpn_eval([5.0, 3.0, "+", 4.0, 2.0, "-", "/"], 7) == 4
assert rpn_eval([1.0, 2.0, "+", 3.0, "*", 6.0, "+", 8.0, 5.0, "-", "/"], 11) == 5
```
