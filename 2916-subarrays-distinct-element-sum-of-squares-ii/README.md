# 2916. Subarrays Distinct Element Sum of Squares II

**Difficulty:** Hard  
**Topics:** Array, Hash Table, Segment Tree, Lazy Propagation

## Problem Summary

Given an integer array `nums`, calculate the sum of the squares of the number of distinct elements in every contiguous subarray.

Return the answer modulo `10^9 + 7`.

**Example:**

```text
Input: nums = [1,2,1]
Output: 15
```

Explanation:

- `[1]` → 1 distinct element → `1² = 1`
- `[1,2]` → 2 distinct elements → `2² = 4`
- `[1,2,1]` → 2 distinct elements → `2² = 4`
- `[2]` → 1 distinct element → `1² = 1`
- `[2,1]` → 2 distinct elements → `2² = 4`
- `[1]` → 1 distinct element → `1² = 1`

Total: `1 + 4 + 4 + 1 + 4 + 1 = 15`

## Intuition

A brute-force solution would examine every subarray and count its distinct elements. However, there are \(O(n^2)\) subarrays, making this approach too slow for large inputs.

Instead, we process the array from left to right and maintain the distinct-element counts of subarrays ending at the current index.

When we encounter a number at index `i`, let `last_seen[num]` be its previous occurrence.

Every subarray starting after that previous occurrence gains one new distinct element. Therefore, we increase the counts for the range:

`[last_seen[num] + 1, i]`

If the number has never appeared before, the range starts at index `0`.

The challenge is performing these range increments efficiently while maintaining the sum of squared counts. We solve this using a **segment tree with lazy propagation**.

## Approach

### 1. Maintain three segment tree arrays

We use flat arrays of size `4 * n`:

- `sum_counts`: stores the sum of counts in each segment.
- `sum_squares`: stores the sum of squared counts in each segment.
- `lasy_updates`: stores pending increments that have not yet been propagated to child nodes.

### 2. Update a segment mathematically

Suppose every count in a segment increases by `inc`.

For an individual count \(a\):

\[
(a+inc)^2=a^2+2a\cdot inc+inc^2
\]

For a segment containing `length` elements, this becomes:

\[
\text{newSquares}=
\text{oldSquares}
+2\cdot inc\cdot\text{oldCounts}
+length\cdot inc^2
\]

We can update the segment's sum of counts and sum of squares in constant time without visiting every element.

### 3. Use lazy propagation

When a range update completely covers a segment, we update its stored values directly and record the pending increment.

We propagate that increment to the children only when a later operation needs to access part of the segment.

This avoids repeatedly updating individual positions.

### 4. Process each number

For every index `i`:

1. Find the previous occurrence of `nums[i]`.
2. Calculate `range_left = last_seen.get(nums[i], -1) + 1`.
3. Increment the segment tree over `[range_left, i]`.
4. Update the last-seen position.
5. Add `sum_squares[1]`, the root's sum of squared counts, to the answer.

The root represents the entire range of possible starting positions. After each update, its sum of squares gives the contribution of all subarrays ending at the current index.

## Python Solution

```python
class Solution:
    def sumCounts(self, nums: List[int]) -> int:
        MOD = 10**9+7
        n = len(nums)

        sum_counts =[0]*(4*n)
        sum_squares =[0]*(4*n)
        lasy_updates =[0]*(4*n)

        def update(node_idx,length,inc):
            sum_squares[node_idx]+=2*inc*sum_counts[node_idx] + length*(inc**2)
            sum_counts[node_idx]+= inc*length
            lasy_updates[node_idx]+=inc
        
        def update_range(node_idx,node_left,node_right,query_left,query_right):
            if query_left<=node_left and node_right<=query_right:
                update(node_idx,node_right-node_left+1,1)
                return 
            mid  = (node_left+node_right)//2

            if lasy_updates[node_idx]:
                update(2*node_idx,mid-node_left+1,lasy_updates[node_idx])
                update(2*node_idx+1,node_right-mid,lasy_updates[node_idx])
                lasy_updates[node_idx]=0

            if query_left<=mid:
                update_range(2*node_idx,node_left,mid,query_left,query_right)
            if query_right>mid:
                update_range(2*node_idx+1,mid+1,node_right,query_left,query_right)

            sum_counts[node_idx] = sum_counts[2*node_idx]+ sum_counts[2*node_idx+1]
            sum_squares[node_idx] =sum_squares[2*node_idx] +sum_squares[2*node_idx+1]

        last_seen = {}
        total= 0
        for i, num in enumerate(nums):
            range_left = last_seen.get(num,-1)+1
            update_range(1,0,n-1,range_left,i)
            last_seen[num]=i
            total = (total+sum_squares[1])%MOD
        return total

```

## Complexity Analysis

- **Time Complexity:** \(O(n\log n)\) — Each of the `n` elements triggers one segment tree range update, which takes \(O(\log n)\) time.
- **Space Complexity:** \(O(n)\) — The three segment tree arrays require \(O(n)\) space, and the `last_seen` dictionary requires up to \(O(n)\) additional space.

## Key Takeaway

The main optimization is to **update a range of distinct counts without visiting every element individually**. Combining a mathematical formula for squared values with a lazy segment tree reduces the solution from quadratic time to \(O(n\log n)\).