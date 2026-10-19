# 2089. Find Target Indices After Sorting Array

**LeetCode Problem:** [2089. Find Target Indices After Sorting Array](https://leetcode.com/problems/find-target-indices-after-sorting-array/)

**Difficulty:** Easy

## Problem Summary

Given an integer array `nums` and an integer `target`, sort the array in non-decreasing order and return a list of all indices where the value equals `target`.

The returned indices must be in increasing order.

**Example:**

```text
Input: nums = [1,2,5,2,3], target = 2
Output: [1,2]
```

After sorting, the array becomes `[1,2,2,3,5]`. The target `2` appears at indices `1` and `2`.

## 1. Intuition

The straightforward approach is to sort the array and then search for every occurrence of the target.

But do we really need to sort the array?

**No. We only need to count two things:**

- `count_less`: How many elements are smaller than the target?
- `count_target`: How many elements are equal to the target?

After sorting, all elements smaller than the target will appear before it. Therefore, the first occurrence of the target will be at index `count_less`.

If the target appears multiple times, its indices will be consecutive.

For example:

```text
nums = [1, 2, 5, 2, 3]
target = 2

Elements smaller than 2: 1
Elements equal to 2:     2

Target indices: [1, 2]
```

We can calculate the answer directly without sorting the array.

## 2. Approach

1. Initialize `count_less` and `count_target` to zero.
2. Traverse the array once:
   - If an element is smaller than `target`, increment `count_less`.
   - If an element equals `target`, increment `count_target`.
3. Create the result array.
4. Generate `count_target` consecutive indices, starting from `count_less`.
5. Return the result.

The key observation is that **the number of smaller elements determines the starting index, while the number of target elements determines the result length.**

## 3. Python Solution

```python
class Solution:
    def targetIndices(self, nums: list[int], target: int) -> list[int]:
        count_less = 0
        count_target = 0

        for n in nums:
            if n < target:
                count_less += 1
            elif n == target:
                count_target += 1

        res = []
        for i in range(count_target):
            res.append(count_less + i)

        return res
```

## 4. C Solution

```c
/**
 * Note: The returned array must be malloced,
 * assume caller calls free().
 */
int* targetIndices(int* nums, int numsSize, int target, int* returnSize) {
    int count_less = 0;
    int count_target = 0;

    for (int i = 0; i < numsSize; i++) {
        if (nums[i] < target)
            count_less++;
        else if (nums[i] == target)
            count_target++;
    }

    int* res = (int*)malloc(count_target * sizeof(int));

    for (int i = 0; i < count_target; i++) {
        res[i] = count_less + i;
    }

    *returnSize = count_target;
    return res;
}
```

## 5. Complexity Analysis

Let `n` be the number of elements in `nums` and `k` be the number of occurrences of `target`.

- **Time Complexity: O(n)** — We traverse the input array once and generate `k` result indices. Since `k` cannot exceed `n`, the total time complexity is O(n).
- **Python Space Complexity: O(k)** — The result list stores `k` indices. The counting variables use O(1) auxiliary space.
- **C Space Complexity: O(k)** — We dynamically allocate memory for the `k` result indices. The counting variables use O(1) auxiliary space.

## 6. Key Takeaway

Sorting is not always necessary when a problem asks for positions in a sorted array.

Instead of sorting and searching, we use counting to determine the exact starting position and number of occurrences of the target.

**One pass. No sorting. O(n) time.**

This is a useful example of how understanding the structure of the expected result can eliminate unnecessary work.