# LeetCode 2265 — Count Nodes Equal to Average of Subtree

# 2265. Count Nodes Equal to Average of Subtree

## Problem

Given the root of a binary tree, return the number of nodes where the value of the node is equal to the average of the values in its subtree.

The average is rounded down to the nearest integer.

A subtree includes the current node and all of its descendants.

## Approach

For every node, we need two pieces of information about its subtree:

* The **total sum** of all node values.
* The **total number of nodes**.

A DFS can return both values from each subtree.

For the current node:

1. Get the sum and count from the left subtree.
2. Get the sum and count from the right subtree.
3. Add the current node's value to the total sum.
4. Add the current node to the total count.
5. Calculate the average using integer division.
6. If the average equals the current node's value, increment the result.
7. Return the total sum and count to the parent.

The condition is checked after processing both children because the current node needs the complete sum and count of its subtree.

### Python

```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def averageOfSubtree(self, root: TreeNode) -> int:
        res = [0]

        def dfs(node):
            if not node:
                return (0, 0)

            left = dfs(node.left)
            right = dfs(node.right)

            sums = left[0] + right[0]
            count = left[1] + right[1]

            total = sums + node.val
            count += 1

            if total // count == node.val:
                res[0] += 1

            return (total, count)

        dfs(root)
        return res[0]
```

## Complexity

* **Time:** `O(n)` — each node is visited exactly once.
* **Space:** `O(h)` — recursion stack, where `h` is the height of the tree.

For a balanced tree, the recursion space is `O(log n)`.
For a completely skewed tree, it can be `O(n)`.

## Key Idea

The important part is that we don't need to calculate each subtree separately.

Each recursive call passes only:

```text
(sum of subtree, number of nodes in subtree)
```

The parent combines the results from its two children with its own value, giving everything needed to calculate its subtree's average in `O(1)` time.

This allows the entire tree to be processed in a single DFS traversal.
