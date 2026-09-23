# LeetCode 1658 — Minimum Operations to Reduce X to Zero

# 1658. Minimum Operations to Reduce X to Zero

[LeetCode Problem](https://leetcode.com/problems/minimum-operations-to-reduce-x-to-zero/)

## 🧩 Problem

You are given an integer array `nums` and an integer `x`.

In one operation, you can remove either the **leftmost** or **rightmost** element from the array and subtract its value from `x`.

Return the **minimum number of operations** required to reduce `x` exactly to `0`.

If it is impossible, return `-1`.

### Example

```text
nums = [1,1,4,2,3], x = 5

Remove 1 from the left
Remove 4 from the left

Operations = 2
```

---

## 🔍 Approach 1: DFS + Memoization

The most direct approach is to simulate the choices we have.

At every step, we can:

1. Remove the element from the left.
2. Remove the element from the right.

So we can recursively explore both possibilities.

### Idea

For every state, we keep track of:

* `left` — left boundary
* `right` — right boundary
* `x` — remaining value

We then cache previously calculated states to avoid solving the same state repeatedly.

```text
                    [left ... right]
                    /              \
             Remove left        Remove right
                /                    \
        [left+1 ... right]     [left ... right-1]
```

### Why it doesn't work

Although memoization removes a lot of duplicate work, the number of possible states can still become very large.

With `N` up to `10^5`, storing a huge number of `(left, right)` states causes excessive memory usage.

This approach eventually results in:

**Memory Limit Exceeded (MLE)**

So we need a different way to look at the problem.

---

## ⚡ Approach 2: Sliding Window

Instead of thinking about the elements we **remove**, let's think about the elements we **keep**.

This change in perspective is the key insight.

### 💡 Key Insight

Let:

```text
total = sum(nums)
```

If the elements we remove add up to `x`, then the elements remaining in the middle must have a sum of:

```text
target = total - x
```

For example:

```text
nums = [1, 1, 4, 2, 3]
total = 11
x = 5

target = 11 - 5
       = 6
```

So instead of finding the minimum number of elements to remove from the ends, we can find the **longest subarray whose sum is `target`**.

Why?

If the longest remaining subarray has length `L`, then we remove:

```text
N - L
```

elements.

Therefore:

> **Minimum removals = N - maximum length subarray with sum `total - x`.**

---

## 🧠 Sliding Window Intuition

Because all numbers in `nums` are positive, we can use a sliding window.

We maintain:

* `left` — start of the current window
* `right` — end of the current window
* `curr` — sum of the current window

For every `right`:

1. Add `nums[right]` to `curr`.
2. If `curr` becomes larger than `target`, move `left` forward until `curr <= target`.
3. Whenever `curr == target`, update the maximum window length.

At the end:

```text
answer = n - longest_subarray_length
```

---

## 💻 Python Solution

```python
class Solution:
    def minOperations(self, nums: list[int], x: int) -> int:
        total = sum(nums)
        target = total - x
        n = len(nums)

        if target < 0:
            return -1

        if target == 0:
            return n

        left = 0
        res = -1
        curr = 0

        for right in range(n):
            curr += nums[right]

            while target < curr:
                curr -= nums[left]
                left += 1

            if target == curr:
                res = max(res, right - left + 1)

        return n - res if res != -1 else -1
```

---

## 🔎 Example Walkthrough

Consider:

```text
nums = [1, 1, 4, 2, 3]
x = 5
```

First calculate:

```text
total = 11
target = 11 - 5 = 6
```

Now we need the **longest subarray with sum 6**.

```text
[1, 1, 4] → sum = 6
```

Its length is `3`.

So:

```text
elements to remove = 5 - 3
                   = 2
```

Therefore:

```text
answer = 2
```

Those two removed elements are:

```text
[1, 1, 4, 2, 3]
 ↑       ↑
remove  remove
```

---

## ⏱️ Complexity Analysis

| Approach          | Time         | Space | Result     |
| ----------------- | ------------ | ----- | ---------- |
| DFS + Memoization | O(N²) states | O(N²) | ❌ MLE      |
| Sliding Window    | O(N)         | O(1)  | ✅ Accepted |

The sliding window runs in **O(N)** time because each element is added to the window once and removed from the window at most once.

---

## 💡 Key Takeaway

The important part of this problem isn't just knowing sliding window.

The real trick is changing the problem:

```text
Remove elements from both ends
            ↓
Find what remains
            ↓
Remaining sum = total - x
            ↓
Find the longest subarray with that sum
            ↓
Minimum operations = N - longest length
```

This is a useful pattern to remember:

> When a problem asks you to remove elements from the ends, try asking what **contiguous portion can remain**.

That change in perspective can turn a recursive search into a simple **O(N) sliding window** solution.
