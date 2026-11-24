# 3411. Maximum Subarray With Equal Products

[LeetCode Problem](https://leetcode.com/problems/maximum-subarray-with-equal-products/)

## Problem Summary

Given an array of positive integers, find the length of the longest contiguous subarray where:

`Product of all elements = GCD of all elements × LCM of all elements`

We need to find the maximum length of such a subarray.

## Intuition

At first, this problem looks like a straightforward application of GCD and LCM. However, there is an important mathematical identity that helps us simplify the problem.

For any two positive integers:

`LCM(a, b) × GCD(a, b) = a × b`

This means **every subarray containing exactly two elements automatically satisfies the condition**.

The interesting part begins when we have three or more elements.

Consider:

`nums = [2, 3, 4]`

For the entire subarray:

- Product = 2 × 3 × 4 = 24
- GCD = 1
- LCM = 12
- GCD × LCM = 12

The condition fails because 24 is not equal to 12.

Why does this happen?

The numbers 2 and 4 share a common prime factor. The product counts that factor multiple times, while the LCM only accounts for the highest required power of that factor.

Now consider:

`nums = [3, 4, 5]`

All three numbers are pairwise coprime, meaning no two numbers share a common factor greater than 1.

- Product = 60
- GCD = 1
- LCM = 60

Here, the condition holds.

### The Key Mathematical Observation

For a subarray containing at least three elements, the equality holds exactly when all elements are pairwise coprime.

This gives us a useful way to understand the problem:

- If all elements are pairwise coprime, GCD is 1 and LCM equals the product.
- If any two elements share a prime factor, the product becomes greater than GCD × LCM.

We could use pairwise GCD checks to identify valid subarrays, but we can take a more direct approach.

## Approach: Brute Force With Incremental GCD, LCM, and Product

We enumerate every possible starting position and extend the subarray one element at a time.

Instead of recalculating the product, GCD, and LCM for every subarray from scratch, we maintain all three values as we extend the current subarray.

For each starting index `i`, initialize:

```python
p = l = g = nums[i]
```

Here:
- `p` stores the current product.
- `l` stores the current LCM.
- `g` stores the current GCD.

Then, for every subsequent element `nums[j]`, update the three values:

```python
p *= nums[j]
l = lcm(l, nums[j])
g = gcd(g, nums[j])
```

Now we can check whether the current subarray satisfies the condition.

If:

```python
p == g * l
```

We update our answer using the current subarray length:

```python
res = max(res, j - i + 1)
```

### Early Termination Optimization

There is one more useful observation.

For any subarray of at least two positive integers:

`Product >= GCD × LCM`

So there are only two possibilities:

1. The equality holds.
2. The product is greater than GCD × LCM.

Once the second condition occurs, extending the subarray cannot restore equality.

Why?

A violation means that at least one prime factor is shared by two or more elements. Adding more elements cannot remove that existing relationship.

Equivalently, the product's extra prime-factor contribution cannot decrease when we extend the subarray.

Therefore, as soon as:

```python
if p > g * l:
    break
```

we can stop exploring this starting index.

There is no reason to extend the subarray further because every longer subarray starting at the same index will also be invalid.

This early termination is what makes the brute-force solution more efficient than checking every possible subarray independently.

## Python Solution

```python
from math import gcd, lcm

class Solution:
    def maxLength(self, nums: List[int]) -> int:
        n = len(nums)
        res = 0

        for i in range(n):
            p = l = g = nums[i]

            for j in range(i + 1, n):
                p *= nums[j]
                l = lcm(l, nums[j])
                g = gcd(g, nums[j])

                if p > g * l:
                    break

                if p == g * l:
                    res = max(res, j - i + 1)

        return res
```

## Example Walkthrough

Consider:

```python
nums = [2, 3, 4]
```

Start with `i = 0`.

Initially:

`p = 2, l = 2, g = 2`

**Extend the subarray by adding 3:**

Current subarray: `[2, 3]`

| Value | Calculation | Result |
|---|---|---:|
| Product | 2 × 3 | 6 |
| LCM | LCM(2, 3) | 6 |
| GCD | GCD(2, 3) | 1 |
| GCD × LCM | 1 × 6 | 6 |

The condition holds.

Current length = 2.

`res = 2`

**Extend the subarray by adding 4:**

Current subarray: `[2, 3, 4]`

| Value | Calculation | Result |
|---|---|---:|
| Product | 6 × 4 | 24 |
| LCM | LCM(6, 4) | 12 |
| GCD | GCD(1, 4) | 1 |
| GCD × LCM | 1 × 12 | 12 |

Now:

`24 > 12`

The condition fails.

We immediately break out of the inner loop because adding more elements cannot make this subarray valid again.

Next, we move to `i = 1`, starting with `[3, 4]`, which satisfies the condition.

The maximum valid length remains 2.

**Output:**

```python
2
```

## Complexity Analysis

Let `n` be the length of the array and `M` be the maximum element.

**Time Complexity: O(n² log M)**

- We have an outer loop over all starting positions.
- For each starting position, we extend the subarray using an inner loop.
- Each extension performs a GCD and LCM calculation, both logarithmic in the magnitude of the values.

The early termination can reduce the actual number of iterations, but the worst-case time complexity remains O(n² log M).

**Space Complexity: O(1)** auxiliary space.

We only maintain a fixed number of variables: product, GCD, LCM, loop indices, and the result. (Ignoring the space required for Python's integer representation.)

## Takeaway

The most useful part of this problem is the mathematical observation that connects the product, GCD, and LCM.

Instead of treating these as three independent calculations, we can understand what makes their equality possible: pairwise coprimality.

That observation also gives us a valid early termination condition, allowing us to prune unnecessary exploration without introducing more complicated data structures or algorithms.