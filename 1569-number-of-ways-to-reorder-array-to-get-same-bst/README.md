# 1569. Number of Ways to Reorder Array to Get Same BST

**LeetCode Problem:** [1569. Number of Ways to Reorder Array to Get Same BST](https://leetcode.com/problems/number-of-ways-to-reorder-array-to-get-same-bst/)

## 1. Problem Summary

Given an array of distinct integers `nums`, inserting its elements into a Binary Search Tree (BST) in the given order creates a particular tree.

We need to count how many different reorderings of `nums` create **the exact same BST**.

The original ordering is included in the count, but we must exclude it from our final answer.

Since the result can be large, return the answer modulo `10⁹ + 7`.

## 2. Intuition

The key observation is that **the first element always becomes the root of the BST**.

Every remaining element is placed into one of two groups:

- **Left subtree:** Elements smaller than the root.
- **Right subtree:** Elements greater than the root.

To create the same BST, we must preserve the relative ordering of elements within each subtree. However, we can interleave the left and right subtree elements in different ways.

For example, suppose the root has 3 elements in its left subtree and 2 in its right subtree.

We need to choose which 3 of the remaining 5 positions will be occupied by left-subtree elements. The right-subtree elements fill the remaining positions.

The number of ways to do this is:

`C(4, 2)`

More generally, if there are `n` elements and `left_count` elements belong to the left subtree, the number of valid interleavings is:

`C(n - 1, left_count)`

We then recursively calculate the valid reorderings for both subtrees and multiply the results.

## 3. Approach: Recursion + Combinatorics

We use a recursive DFS function to count the valid reorderings for each subtree.

**Step 1: Handle the base case**

If the array contains fewer than three elements, there is only one possible ordering that preserves the same BST structure.

**Step 2: Split the array**

Use the first element as the root and divide the remaining elements into two lists:

- `left`: Elements smaller than the root.
- `right`: Elements greater than the root.

**Step 3: Count the interleavings**

Calculate the number of ways to arrange the left and right subtree elements while preserving their individual relative orders.

This is given by:

`comb(n - 1, len(left))`

**Step 4: Combine the results**

Multiply the number of valid reorderings of the left subtree, the right subtree, and the possible interleavings.

Apply the modulo operation to keep the result within the required range.

**Step 5: Exclude the original ordering**

The recursive function counts the original ordering as one valid arrangement. Subtract one from the final result.

## 4. Python Solution

```python
from math import comb

class Solution:
    def numOfWays(self, nums: list[int]) -> int:
        MOD = 10**9 + 7

        def dfs(arr):
            n = len(arr)

            if n < 3:
                return 1

            left = [a for a in arr if a < arr[0]]
            right = [a for a in arr if a > arr[0]]

            return (
                dfs(left)
                * dfs(right)
                * comb(n - 1, len(left))
            ) % MOD

        return (dfs(nums) - 1) % MOD
```

## 5. Complexity Analysis

Let `n` be the number of elements in `nums`.

- **Time Complexity:** Approximately `O(n²)` for the recursive splitting and traversal in the worst case, excluding the cost of computing binomial coefficients. Python's `math.comb` also has a computational cost that depends on the input sizes.
- **Space Complexity:** `O(n²)` in the worst case when accounting for the arrays created at different recursive levels. The recursion stack itself can reach `O(n)` depth.

## 6. Key Takeaways

- The first element determines the BST root.
- The left and right subtrees must retain their internal relative ordering.
- Combinatorics counts the possible interleavings of the two subtrees.
- Recursion solves each subtree independently.
- Subtract one because the original ordering must not be included in the answer.

**Core idea:** Recursively count the valid arrangements of both subtrees, then use combinations to count how many ways their elements can be interleaved without changing the resulting BST.