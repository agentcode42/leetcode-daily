# 2897. Apply Operations on Array to Maximize Sum of Squares

**LeetCode Problem:** [Apply Operations on Array to Maximize Sum of Squares](https://leetcode.com/problems/apply-operations-on-array-to-maximize-sum-of-squares/)

## Problem Summary

We are given an integer array `nums` and a positive integer `k`. We can repeatedly choose two distinct indices and replace their values with their bitwise AND and bitwise OR, respectively.

Our task is to choose `k` elements from the final array to maximize the sum of their squares.

Since the answer can be large, return it modulo `10^9 + 7`.

## Intuition

The key observation is that **bitwise AND and OR redistribute set bits without changing the total number of set bits at any bit position across the array.**

For example, consider two numbers:

- `5 = 101`
- `3 = 011`

Applying AND and OR gives:

- `5 & 3 = 001` (1)
- `5 | 3 = 111` (7)

The set bits are redistributed between the two numbers, but no bit is created or destroyed.

Since squaring larger numbers produces a greater sum, we want to construct the largest possible numbers by gathering as many available set bits as possible into each of the `k` numbers.

To achieve this, we first count how many numbers have each bit set. Then, we construct each number using every bit position that still has an available set bit. After using a bit, we decrease its count so it cannot be reused beyond its original availability.

## Approach

1. **Count set bits:** Create a `count` array of size 32. For every number, check each bit position and increment its count if that bit is set.
2. **Construct numbers greedily:** Repeat `k` times. Build a number by including every bit whose count is greater than zero, starting from the highest bit.
3. **Consume available bits:** Whenever a bit is included, decrease its count by one.
4. **Calculate the sum:** Square each constructed number and add it to the result modulo `10^9 + 7`.

## Solution 1: Bitwise Construction

```python
class Solution:
    def maxSum(self, nums: List[int], k: int) -> int:
        MOD = 10**9 + 7
        res = 0
        count = [0] * 32

        for n in nums:
            for i in range(32):
                if n & (1 << i):
                    count[i] += 1

        for _ in range(k):
            x = 0
            for i in range(31, -1, -1):
                if count[i] > 0:
                    x |= 1 << i
                    count[i] -= 1

            res = (res + x * x) % MOD

        return res
```

### How it works

Instead of converting numbers to binary strings, we construct each number directly using bitwise operations.

- `1 << i` creates a number with only bit `i` set.
- `x |= 1 << i` turns that bit on in `x`.
- `count[i] -= 1` consumes one available copy of the bit.

This approach avoids unnecessary string conversions and directly constructs the desired integer.

## Solution 2: Binary String Construction

```python
class Solution:
    def maxSum(self, nums: List[int], k: int) -> int:
        MOD = 10**9 + 7
        res = 0
        count = [0] * 32

        for n in nums:
            for i in range(32):
                if n & (1 << i):
                    count[i] += 1

        for _ in range(k):
            binary = ""

            for i in range(31, -1, -1):
                if count[i] > 0:
                    binary += "1"
                    count[i] -= 1
                else:
                    binary += "0"

            x = int(binary, 2)
            res = (res + x * x) % MOD

        return res
```
```C
int maxSum(int* nums, int numsSize, int k) {
    int count[32] = {0};
    long long res = 0;
    long long MOD = 1000000007;
   
    for (int j = 0; j < numsSize; j++) {
        int val = nums[j];
        for (int i = 0; i < 32; i++) {
            if (val & (1LL << i)) {
                count[i]++;
            }
        }
    } 


    for (int j = 0; j < k; j++) {
        long long x = 0;
        for (int i = 31; i >= 0; i--) {
            if (count[i] > 0) {
                x |= (1LL << i);
                count[i]--;    
            }
        }
        res = (res + (x * x) % MOD) % MOD;
    }   
    return (int)res;   
}

```

### How it works

This solution follows the same greedy strategy, but constructs each number as a binary string.

- Append `"1"` when a set bit is available and decrease its count.
- Otherwise, append `"0"`.
- Convert the completed binary string into an integer using `int(binary, 2)`.
- Square the integer and add it to the result.

Both solutions produce the same result. The first is more direct and avoids creating and converting binary strings.

## Complexity Analysis

Let `n` be the length of `nums` and `B = 32` be the number of bit positions checked.

**Time Complexity:** `O(n × B + k × B)`, which simplifies to **O(32n + 32k)** or **O(n + k)** when the bit width is fixed.

**Space Complexity:** **O(B)**, or **O(1)** auxiliary space for a fixed 32-bit representation. The second solution also creates a temporary binary string of length 32, which remains constant space.

## Key Takeaway

The main trick is to **count available set bits and greedily pack them into the largest possible numbers**. Because the objective is to maximize the sum of squares, concentrating available bits into each constructed number gives the optimal result.

This problem is a good example of how bit manipulation and a greedy strategy can replace a more complicated search for the optimal arrangement.