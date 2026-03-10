# Greedy Algorithms

### Exercise 1

Design and implement a greedy algorithm for the point collection problem from last week. Show that your algorithm is more efficient than the DP algorithm from last week. Show that your algorithm is not optimal.

---

### Exercise 2

Design and implement a greedy algorithm for the minimum change making problem from last week. Show that your algorithm is more efficient than the DP algorithm from last week. Show that your algorithm is not optimal.

---

### Exercise 3

We are planning a long car trip, but our car can only carry $n$ liters of fuel. We have a map that shows the gas stations on our path and we calculated the "distance" in fuel consumption between each subsequent gas station. Design and implement an efficient algorithm that determines the locations at which we have to stop to fully refuel, in order to stop as few times as possible.

The input contains $k$ numbers $d_1, ..., d_k$ with each $d_i$ representing the distance (in liters of fuel) between the $i-1^\text{st}$ and the $i^\text{th}$ gas stations. Assume that we start at the $0^{th}$ gas station with a full tank. Return the minimum number of stops required to complete the trip.

Example: for $n = 10$, $k = 4$, and `distances = [5, 7, 4, 3]` we need two stops at the first and second gas stations.

---

### Exercise 4

You are given $n$ real numbers $k_1, ..., k_n$. We say a closed interval $[a, b]$ ***covers*** a number $k$ if and only if $a \leq k \leq b$. Design and implement an algorithm that finds a minimal number of unit-length closed intervals (i.e. $[a, a+1]$) such that all numbers are covered by at least one of the intervals. Return the minimum number of intervals.

Example: for `K = [0.1, 0.3, 0.7, 1.2, 1.3, 1.4, 1.6, 1.8]` ($n=8$) an optimal solution using two intervals is $[0, 1]$ and $[1.1, 2.1]$, where $[0, 1]$ covers the first three points and $[1.1, 2.1]$ covers the last five.

---

### Exercise 5

Design and implement a greedy algorithm for the fractional knapsack problem.

Given $n$ items, described by their value $v_i$ and weight $w_i$, and a knapsack with capacity $C$, the goal is to "put" items in the knapsack in a way that maximizes the total value in the knapsack. The total weight of the items in the knapsack cannot exceed the capacity of the knapsack. Items can be "broken" where the value of an item fragment is proportional to the size of the fragment (e.g. half the item is worth half its value). Every item can be used at most once.

Your algorithm should return the maximum total value of the items that the knapsack can contain.

Example: for the following $n = 3$ items

|  $i$  | $v_i$ | $w_i$ |
|:-----:|:-----:|:-----:|
|   0   |   2   |   1   |
|   1   |   3   |   2   |
|   2   |   4   |   3   |

and $C=3$, the optimal solution uses the first and the second items, whose total value is 5.

---

### Exercise 6

Show that your greedy algorithm for the fractional knapsack problem (Exercise 05) is not optimal for the 0-1 knapsack problem. Design and implement a dynamic programming algorithm for the 0-1 knapsack problem.
