# 3524. Find X Value of Array I

[LeetCode Problem](https://leetcode.com/problems/find-x-value-of-array-i/)

## Problem

You are given an array of positive integers `nums` and a positive integer `k`.

For every non-empty contiguous subarray, calculate the product of its elements modulo `k`.

For each possible remainder `x` from `0` to `k - 1`, count how many subarrays have a product whose remainder is `x`.

Return an array of size `k`, where `res[x]` represents the number of subarrays whose product modulo `k` equals `x`.

---

## Intuition

There can be `n * (n + 1) / 2` contiguous subarrays, so checking every subarray individually would take `O(n²)` time.

The important constraint is that:

```text
1 <= k <= 5
```

Since `k` is very small, we can keep track of the number of subarrays ending at the current position for **each possible remainder**.

For example, suppose:

```text
reminders[r]
```

stores the number of subarrays ending at the previous index whose product has remainder `r`.

When we process a new number `n`:

### 1. Start a new subarray

The single-element subarray `[n]` has remainder:

```text
n % k
```

So we add one to that remainder.

### 2. Extend previous subarrays

Every subarray that ended at the previous position can be extended by `n`.

If its previous product had remainder `i`, the new product has remainder:

```text
(n * i) % k
```

So we move all those counts into the corresponding remainder.

### 3. Add the current counts to the answer

Every subarray ending at the current position is now represented in `new_r`, so we add those counts to the global result.

Then:

```text
reminders = new_r
```

and continue to the next number.

---

## Approach

We maintain two arrays:

* `reminders` — counts of subarrays ending at the previous index for every remainder.
* `res` — total counts of all subarrays seen so far for every remainder.

For every `n` in `nums`:

1. Create `new_r` to store counts for subarrays ending at the current index.
2. Add the single-element subarray `[n]`.
3. Extend every previous subarray and calculate its new remainder.
4. Add `new_r` to `res`.
5. Replace `reminders` with `new_r`.

Because `k` is at most `5`, we only perform a constant amount of work for each element.

---

## Code

```python
class Solution:
    def resultArray(self, nums: List[int], k: int) -> List[int]:
        res = [0] * k
        reminders = [0] * k
        
        for n in nums:
            new_r = [0] * k
            new_r[n % k] = 1
            
            for i in range(k):
                curr = (n * i) % k
                new_r[curr] += reminders[i]
                
            for i in range(k):
                res[i] += new_r[i]
                
            reminders = new_r
        
        return res
```

---

## Complexity

Let `n` be the length of `nums`.

* **Time:** `O(n × k)`
* **Space:** `O(k)`

Since `k <= 5`, the time complexity is effectively **O(n)**.

---

## Key Takeaway

Instead of generating every subarray, we only need to remember how many subarrays ending at the previous position produce each possible remainder.

Because there are at most `5` possible remainders, we can update all of them for every number in constant time.
