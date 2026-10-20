# LeetCode 3886 — Sum of Sortable Integers

# 3886. Sum of Sortable Integers

[LeetCode Problem](https://leetcode.com/problems/sum-of-sortable-integers/)

## Problem Summary

Given an integer array `nums`, find the sum of all positive integers `k` such that:

- `k` divides the length of the array.
- If we sort every consecutive block of length `k` independently, the entire array becomes sorted.

Return the sum of all valid values of `k`.

## Intuition

Instead of actually sorting the array for every possible block size, we can check whether each block size satisfies the conditions for the entire array to become sorted.

For a block of size `k`, two things must be true:

1. **Each block must be sortable with one cyclic descent at most.** Count how many times an element is greater than the next element, including the comparison between the last and first elements of the block. If this count exceeds `1`, the block cannot be sorted by a single cyclic rotation.
2. **The blocks must fit together in sorted order.** The maximum element of the previous block must not exceed the minimum element of the current block.

If both conditions hold for every block, `k` is valid, so we add it to the answer.

## Approach

1. Get the length of the array, `n`.
2. Try every possible block size `k` from `1` to `n`.
3. Skip `k` if it does not divide `n`, because all blocks must have equal length.
4. For each remaining `k`:
   - Divide the array into consecutive blocks of size `k`.
   - Track the minimum and maximum values in each block.
   - Count cyclic descents using `nums[i + j] > nums[i + (j + 1) % k]`.
   - Reject the block size if the descent count exceeds `1` or if the previous block's maximum is greater than the current block's minimum.
5. If every block passes both checks, add `k` to `res`.
6. Return `res`.

## Python Solution

```python
class Solution:
    def sortableIntegers(self, nums: list[int]) -> int:
        n = len(nums)
        res = 0

        for k in range(1, n + 1):
            if n % k:
                continue

            flag = True
            prev_max = 0

            for i in range(0, n, k):
                count = 0
                max_n = min_n = nums[i]

                for j in range(k):
                    a = nums[i + j]
                    b = nums[i + (j + 1) % k]

                    if a > b:
                        count += 1

                    min_n = min(a, min_n)
                    max_n = max(a, max_n)

                if count > 1 or prev_max > min_n:
                    flag = False
                    break

                prev_max = max_n

            if flag:
                res += k

        return res
```
```C
int sortableIntegers(int* nums, int numsSize) {
    int n = numsSize;
    int res = 0;
    for(int k =1;k<n+1;k++){
        if (n%k) continue;
        bool flag = true;
        int prev_max = 0;
        for (int i=0;i<n;i+=k){
            int count = 0;
            int curr_max=nums[i];
            int curr_min=nums[i];
            for (int j=0;j<k;j++){
                int a= nums[i+j];
                int b = nums[i+(j+1)%k];
                if (a>b)count++;
                if (a<curr_min)curr_min=a;
                if (a>curr_max)curr_max=a;
            }
            if (count>1 || prev_max>curr_min){
                flag = false;
                break;
            }
            prev_max = curr_max;
        }
        if (flag)res+=k;
    }
    return res;
}
```

## Complexity Analysis

Let `n` be the length of `nums`.

- **Time Complexity:** `O(n²)` — We check every possible block size, and each valid divisor requires examining the array in blocks. The total work is bounded by the sum of `n` checks for up to `n` candidate sizes.
- **Space Complexity:** `O(1)` — We use only a fixed number of variables, without creating additional arrays.

## Key Takeaway

The key is to avoid sorting each block explicitly. By counting cyclic descents and checking the minimum and maximum values across neighboring blocks, we can determine whether a block size works in constant auxiliary space.