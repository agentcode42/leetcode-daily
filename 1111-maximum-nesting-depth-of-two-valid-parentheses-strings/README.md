# LeetCode 1111: Maximum Nesting Depth of Two Valid Parentheses Strings

🔗 [Problem](https://leetcode.com/problems/maximum-nesting-depth-of-two-valid-parentheses-strings/)

## Problem

We are given a valid parentheses string `seq`.

We need to split its parentheses into two groups, `A` and `B`, such that:

* Both groups are valid parentheses strings.
* The maximum nesting depth of either group is as small as possible.

The answer is an array where:

* `0` means the character belongs to group `A`
* `1` means the character belongs to group `B`

---

## Intuition

The important observation is that we do not actually need to build the two strings.

We can simply keep track of the current nesting `depth`.

Whenever we encounter an opening parenthesis `(`:

1. Increase the depth.
2. Assign it to one of the two groups based on whether the new depth is even or odd.

For a closing parenthesis `)`:

1. Use the current depth to determine its group.
2. Decrease the depth afterward.

This effectively distributes nested parentheses between the two groups:

* Odd depths → group `1`
* Even depths → group `0`

By alternating the groups based on depth, we split the nesting as evenly as possible.

---

## Approach

1. Initialize `depth = 0`.
2. Traverse every character in `seq`.
3. For `(`:

   * Increase `depth`.
   * Assign `depth % 2`.
4. For `)`:

   * Assign `depth % 2`.
   * Decrease `depth`.
5. Return the resulting array.

The key idea is:

```text
depth % 2
```

This alternates the assignment between the two groups as nesting increases.

---

## Code

```python
class Solution:
    def maxDepthAfterSplit(self, seq: str) -> list[int]:

        res = []

        depth = 0

        for c in seq:

            if c == "(":
                depth += 1
                res.append(depth % 2)

            elif c == ")":
                res.append(depth % 2)
                depth -= 1

        return res
```

---

## Example

### Input

```text
seq = "(()())"
```

We track the nesting depth:

```text
(  -> depth = 1 -> group 1
(  -> depth = 2 -> group 0
)  -> depth = 2 -> group 0
(  -> depth = 2 -> group 0
)  -> depth = 2 -> group 0
)  -> depth = 1 -> group 1
```

Result:

```text
[1, 0, 0, 0, 0, 1]
```

The parentheses are split between the two groups so that neither group contains unnecessarily deep nesting.

---

## Why It Works

At every level of nesting, we alternate between the two groups.

So instead of putting all nested parentheses into the same string, we distribute them:

```text
Depth 1 → Group 1
Depth 2 → Group 0
Depth 3 → Group 1
Depth 4 → Group 0
...
```

This keeps the maximum depth of the two resulting strings balanced.

---

## Complexity

* **Time:** `O(n)` — we process every character once.
* **Space:** `O(n)` — the result array stores one value for every character.
