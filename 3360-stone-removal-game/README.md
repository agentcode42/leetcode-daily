# 3360. Stone Removal Game

[LeetCode Problem Link](https://leetcode.com/problems/stone-removal-game/)

## Problem Summary

Alice and Bob play a game where they take turns removing stones from a pile.

- Alice starts by removing 10 stones.
- Bob must remove 9 stones.
- Alice must remove 8 stones.
- The required number of stones decreases by 1 after every turn.
- A player who cannot remove the required number of stones loses.

Return `true` if Alice wins, otherwise return `false`.

## Intuition

We can simulate the game directly because the number of possible moves is limited.

Instead of trying to calculate the winner using a mathematical formula, we follow the actual game:

1. Start with 10 as the required number of stones.
2. Track whose turn it is.
3. If the current player has enough stones, remove the required amount.
4. Decrease the required amount by 1.
5. Switch turns.
6. If the current player cannot remove the required amount, that player loses.

We only need two variables to simulate the entire game.

## Approach

We use two variables:

- `curr`: Number of stones the current player must remove. Starts at 10 and decreases after every successful move.
- `a`: Tracks the current player. `True` represents Alice, while `False` represents Bob.

### Game Simulation

We continue while `curr > 0`.

**Case 1: Current player has enough stones**

If `curr <= n`:

- Subtract `curr` from `n`.
- Decrease `curr` by 1.
- Switch the current player using `a = not a`.

**Case 2: Current player cannot remove enough stones**

If `curr > n`, the current player loses.

Since `a` represents the losing player's turn, we return `not a` to identify the winner.

The final `return not a` handles the case where all ten possible removals have been completed.

## Step-by-Step Simulation

Consider the example:

`n = 27`

Initially:

- `curr = 10`
- `a = True` (Alice's turn)

| Step | Player | Required | Remaining stones | Result |
|---|---|---:|---:|---|
| 1 | Alice | 10 | 17 | Removes 10 |
| 2 | Bob | 9 | 8 | Removes 9 |
| 3 | Alice | 8 | 0 | Removes 8 |
| 4 | Bob | 7 | 0 | Cannot remove 7 |

Let's follow the variables:

**Initial state**

```python
n = 27
curr = 10
a = True
```

**Turn 1: Alice**

```python
n -= curr      # 27 - 10 = 17
curr -= 1      # 10 -> 9
a = not a      # True -> False
```

**Turn 2: Bob**

```python
n -= curr      # 17 - 9 = 8
curr -= 1      # 9 -> 8
a = not a      # False -> True
```

**Turn 3: Alice**

```python
n -= curr      # 8 - 8 = 0
curr -= 1      # 8 -> 7
a = not a      # True -> False
```

**Turn 4: Bob**

Bob needs to remove 7 stones, but no stones remain.

```python
curr > n       # 7 > 0
return not a   # True
```

Bob loses, so Alice wins.

**Output: `true`**

## Python Solution

```python
class Solution:
    def canAliceWin(self, n: int) -> bool:
        curr = 10
        a = True

        while curr > 0:
            if curr <= n:
                n -= curr
                curr -= 1
                a = not a
            else:
                return not a

        return not a
```

## C Solution

```c
bool canAliceWin(int n) {
    int curr = 10;
    bool a = true;

    while (curr > 0) {
        if (curr <= n) {
            n -= curr;
            curr--;
            a = !a;
        }
        else {
            return !a;
        }
    }

    return !a;
}
```

## Complexity Analysis

**Time Complexity: O(1)**

The required number of stones starts at 10 and decreases after every successful move. Therefore, the loop can execute at most 10 times, regardless of the input size.

**Space Complexity: O(1)**

We only use two additional variables, `curr` and `a`. No additional data structures are required.

## Key Takeaway

This problem is a straightforward game simulation.

When the number of possible moves is small and fixed, simulating the actual process is often the simplest and clearest solution. There is no need to introduce mathematical optimization when the simulation already runs in constant time.