# 3041. Maximize Consecutive Elements in an Array After Modification

[LeetCode Problem Link](https://leetcode.com/problems/maximize-consecutive-elements-in-an-array-after-modification/)

## Problem Summary

We are given an array of positive integers.

We can increase any element by at most `1`. After making these modifications, we need to select the maximum number of elements whose values form a sequence of consecutive integers.

For example:

```python
nums = [2, 1, 5, 1, 1]
```

We can modify the elements to obtain:

```python
[1, 2, 3, 5, 5]
```

Selecting `[1, 2, 3]` gives us a consecutive sequence of length `3`.

Our task is to maximize this length.

## Intuition: From Greedy to Dynamic Programming

My initial approach was to sort the array and create another array containing the incremented values.

The idea was to build consecutive sequences by choosing either the original value or its incremented value.

However, this greedy approach had a limitation.

We maintained only one current value (`curr`) and one sequence length (`curr_len`). Whenever a sequence could not be extended, we restarted from the current element.

The problem is that restarting can make us lose other possible sequences.

An element that cannot extend our current sequence might still be a useful starting point for another sequence.

Therefore, instead of maintaining only one sequence, we need to preserve multiple possibilities.

This leads us to Dynamic Programming.

## Approach: Sorting + Dynamic Programming

### 1. Why Sort?

First, we sort the array:

```python
nums.sort()
```

Sorting allows us to process smaller values before larger values.

This is important because we want to construct consecutive sequences in increasing order.

We don't need to worry about the original positions of elements because the problem only requires selecting elements whose values are consecutive after sorting.

### 2. DP State

We use a dictionary:

```python
dp[value]
```

It represents:

**The maximum length of a consecutive sequence ending at `value`, using the elements processed so far.**

For example:

```python
dp = {
    1: 1,
    2: 2,
    3: 3
}
```

This means:

- A sequence ending at `1` has length `1`.
- A sequence ending at `2` has length `2`.
- A sequence ending at `3` has length `3`.

We maintain these possibilities independently instead of committing to only one sequence.

### 3. Two Choices for Every Element

For each element `x`, we have two choices.

**Choice A: Keep the original value**

We use `x` without modification.

To extend a consecutive sequence, we need a sequence that currently ends at `x - 1`.

Therefore:

```python
dp[x] = dp[x - 1] + 1
```

If no sequence ends at `x - 1`, the default dictionary value is `0`, so we start a new sequence of length `1`.

**Choice B: Increment the element**

We increase `x` to `x + 1`.

To extend a consecutive sequence, we need a sequence that currently ends at `x`.

Therefore:

```python
dp[x + 1] = dp[x] + 1
```

If no sequence ends at `x`, we start a new sequence of length `1`.

### 4. Why Process the Incremented Choice First?

Our implementation uses this order:

```python
dp[x + 1] = dp[x] + 1
dp[x] = dp[x - 1] + 1
```

This ordering matters.

We first calculate the incremented choice using the previous DP state.

Then we calculate the original choice.

If we updated `dp[x]` first, the incremented transition could accidentally use the current element's newly updated state, effectively allowing the same element to be selected twice.

Processing the incremented choice first prevents that.

## Code

```python
class Solution:
    def maxSelectedElements(self, nums: List[int]) -> int:
        nums.sort()
        dp = defaultdict(int)
        res = 0

        for x in nums:
            dp[x+1] = dp[x]+1
            dp[x] = dp[x-1]+1

            res = max(res, dp[x], dp[x+1])

        return res
```

## Complexity Analysis

Let `n` be the length of the input array.

- **Sorting:** O(n log n)
- **DP processing:** O(n), since each dictionary operation takes O(1) average time.
- **Space Complexity:** O(n), because the dictionary can store information for up to two possible ending values per element.

**Overall Time Complexity: O(n log n)**

**Overall Space Complexity: O(n)**

## Key Takeaway

The important lesson from this problem is the transition from Greedy to Dynamic Programming.

Maintaining only one current sequence can cause us to lose other valid possibilities.

Instead, we maintain the best sequence length for every possible ending value.

For every element, we consider both possibilities:

1. Keep the element unchanged.
2. Increase the element by one.

By processing the sorted array and preserving these DP states, we can find the maximum possible length without trying every possible starting point.