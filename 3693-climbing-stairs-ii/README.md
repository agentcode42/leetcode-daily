# LeetCode 3693 — Climbing Stairs II

# 3693. Climbing Stairs II

[LeetCode Problem](https://leetcode.com/problems/climbing-stairs-ii/)

## Problem Summary

You are given an integer `n` representing the destination stair and an array `costs`, where `costs[i]` represents the cost of stepping onto stair `i + 1`.

You can climb either 1, 2, or 3 stairs at a time.

The cost of each jump is the cost of the destination stair plus the square of the number of stairs jumped.

Return the minimum total cost required to reach stair `n`, starting from stair `0`.

## Intuition

We can solve this problem using **Dynamic Programming (Forward DP)**.

Instead of trying to calculate every possible path, we maintain the minimum cost required to reach each stair.

Define:

`dp[i]` = Minimum cost required to reach position `i`.

We initialize all positions with infinity because we are looking for minimum costs. The starting position has a cost of zero:

```python
dp = [float('inf')] * (n+1)
dp[0] = 0
```

From each position, we have three possible jumps:

- Jump 1 stair: Additional cost = `costs[i] + 1`
- Jump 2 stairs: Additional cost = `costs[i+1] + 4`
- Jump 3 stairs: Additional cost = `costs[i+2] + 9`

Each transition updates the destination with the minimum cost found so far.

## Approach

1. Create a DP array of size `n + 1`, initialized with infinity.
2. Set `dp[0] = 0` because we start at position zero without any cost.
3. Iterate through every position from `0` to `n-1`.
4. From each position, calculate the cost of all valid jumps (1, 2, and 3 stairs).
5. Update each destination using `min()` to retain the cheapest path.
6. Return `dp[n]`, which contains the minimum cost to reach the destination.

An important observation is that if multiple paths reach the same position, we only need to retain the cheapest one. All future transitions are identical regardless of the path taken to reach that position.

## Code

```python
class Solution:
    def climbStairs(self, n: int, costs: List[int]) -> int:
        dp = [float('inf')]*(n+1)
        dp[0] = 0

        for i in range(n):
            dp[i+1] = min(dp[i+1], dp[i] + costs[i] + 1)

            if i < n-1:
                dp[i+2] = min(dp[i+2], dp[i] + costs[i+1] + 4)

            if i < n-2:
                dp[i+3] = min(dp[i+3], dp[i] + costs[i+2] + 9)

        return dp[n]
```

## Complexity Analysis

- **Time Complexity:** `O(n)` — We iterate through the stairs once and perform at most three constant-time transitions per position.
- **Space Complexity:** `O(n)` — We maintain a DP array of size `n + 1`.