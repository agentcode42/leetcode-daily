# 3789. Minimum Cost to Acquire Required Items

[LeetCode Problem](https://leetcode.com/problems/minimum-cost-to-acquire-required-items/)

## Problem Summary

We need to acquire at least `need1` items of type 1 and `need2` items of type 2.

There are three purchasing options:

- Buy one item of type 1 for `cost1`.
- Buy one item of type 2 for `cost2`.
- Buy one item of both types together for `costBoth`.

The goal is to find the minimum total cost to acquire the required quantities.

## Intuition

There are three possible strategies:

1. **Buy items separately:** Purchase all type 1 and type 2 items individually.
2. **Buy combined items for the smaller requirement:** Use combined purchases to satisfy the smaller requirement, then buy the remaining items of the larger requirement individually.
3. **Buy only combined items:** Purchase enough combined items to satisfy the larger requirement. This might result in extra items, but could still be cheaper.

Calculate the cost of all three strategies and return the minimum.

## Approach

**1. Buy everything separately**

Calculate the total cost:

`total = cost1 * need1 + cost2 * need2`

**2. Use combined purchases for the smaller requirement**

If `need1` is smaller, buy `need1` combined items and purchase the remaining type 2 items individually.

Otherwise, buy `need2` combined items and purchase the remaining type 1 items individually.

**3. Use only combined purchases**

Buy `max(need1, need2)` combined items. This guarantees that both requirements are satisfied.

**4. Return the minimum**

Compare the three calculated costs and return the smallest one.

## Code

```python
class Solution:
    def minimumCost(self, cost1: int, cost2: int, costBoth: int, need1: int, need2: int) -> int:
        total = cost1 * need1 + cost2 * need2

        cost3 = costBoth
        total1 = 0

        if need1 < need2:
            total1 = cost3 * need1 + cost2 * (need2 - need1)
        else:
            total1 = cost3 * need2 + cost1 * (need1 - need2)

        total2 = cost3 * max(need1, need2)

        return min(total, total1, total2)
```

## Complexity Analysis

- **Time Complexity:** `O(1)` — Only a constant number of arithmetic operations and comparisons are performed.
- **Space Complexity:** `O(1)` — Only a constant amount of extra space is used.

## Key Takeaway

Instead of checking every possible combination of purchases, we only need to evaluate three strategies: buying separately, combining purchases up to the smaller requirement, or buying combined items for the larger requirement.

The minimum of these three costs gives the optimal answer.