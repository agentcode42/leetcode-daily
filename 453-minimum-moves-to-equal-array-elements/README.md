# 453. Minimum Moves to Equal Array Elements

[LeetCode Problem – 453. Minimum Moves to Equal Array Elements](https://leetcode.com/problems/minimum-moves-to-equal-array-elements/)

## Problem Summary

Given an integer array `nums`, return the minimum number of moves required to make all elements equal.

In one move, we can increment exactly `n - 1` elements of the array by `1`, where `n` is the size of the array.

The goal is to find the minimum number of moves needed to make every element equal.

## 1. Brute Force Approach

### Intuition

We can directly simulate the operation described in the problem.

In every move:
1. Find the maximum element in the array.
2. Skip one occurrence of that maximum element.
3. Increment every other element by `1`.
4. Increase our move counter.

We repeat this process until all elements become equal.

### Python Code

```python
class Solution:
    def minMoves(self, nums: list[int]) -> int:
        count = 0
        n = len(nums)

        while len(set(nums)) > 1:
            idx_max_val = nums.index(max(nums))

            for i in range(n):
                if i != idx_max_val:
                    nums[i] += 1

            count += 1

        return count
```

### Complexity Analysis

- **Time Complexity:** O(n × (max(nums) - min(nums))) approximately, since each move requires finding the maximum, finding its index, and updating the array.
- **Space Complexity:** O(n) for creating the set used to check whether all elements are equal.

This approach simulates every move, making it too slow for large inputs and resulting in TLE.

## 2. Optimized Approach – Mathematical Observation

### Intuition

Instead of simulating every increment, we can look at the operation from a different perspective.

In each move, we increment `n - 1` elements by `1` and leave one element unchanged.

This is mathematically equivalent to decrementing the remaining element by `1`, because we only care about the relative differences between array elements.

For example:

```text
Original operation:
[1, 2, 3]
[2, 3, 3]

Equivalent operation:
[1, 2, 3]
[1, 2, 2]
```

Both operations produce the same relative differences between elements.

### Why Choose the Minimum Element?

If we use the decrement interpretation, our goal is to make every element equal to the minimum element.

We cannot reduce the elements below the original minimum because that would require additional moves in the opposite direction.

Therefore, the minimum element becomes our target.

### Calculate the Number of Moves

For every element, calculate how many times it needs to be decremented to reach the minimum value.

```text
nums = [1, 2, 3, 4, 4, 5]

Minimum = 1

Differences:
[0, 1, 2, 3, 3, 4]

Total moves:
0 + 1 + 2 + 3 + 3 + 4 = 13
```

The answer is simply the sum of all these differences.

### Python Code – Using a Loop

```python
class Solution:
    def minMoves(self, nums: list[int]) -> int:
        res = 0
        min_val = min(nums)

        for n in nums:
            res += (n - min_val)

        return res
```

### Python Code – Using sum()

We can simplify the same approach using Python's built-in `sum()` function and a generator expression.

```python
class Solution:
    def minMoves(self, nums: list[int]) -> int:
        min_val = min(nums)
        return sum((n - min_val) for n in nums)
```

Both implementations use exactly the same mathematical logic.

## 3. Final Array Observation

We can also calculate the actual final equal value if needed.

Since the minimum value needs to be increased by the total number of moves:

```text
Final Value = Minimum Value + Total Moves
```

For our example:

```text
Minimum = 1
Moves = 13

Final Value = 1 + 13 = 14

Final Array:
[14, 14, 14, 14, 14, 14]
```

We can verify this using the original operation:

Each move increments 5 elements, so 13 moves produce 65 total increments.

Original sum = 19

Final sum = 19 + 65 = 84

84 / 6 = 14

This confirms our mathematical result.

## 4. Complexity Analysis – Optimized Solution

Let `n` be the number of elements in the array.

- **Time Complexity:** O(n), because we find the minimum once and iterate through the array once.
- **Space Complexity:** O(1), excluding the input array, since we only use a few variables. The generator expression does not create another array.

## Key Takeaway

The important observation in this problem is that incrementing `n - 1` elements is equivalent to decrementing one element when considering relative differences.

Instead of simulating potentially thousands or millions of moves, we can calculate the total difference between every element and the minimum value.

**Final Formula:**

\[
\boxed{Answer = \sum_{i=0}^{n-1}(nums[i]-min(nums))}
\]

A simulation problem becomes a simple mathematical calculation once we recognize the equivalent operation.