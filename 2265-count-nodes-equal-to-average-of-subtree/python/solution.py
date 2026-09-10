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
                return (0,0)
            left = dfs(node.left)
            right = dfs(node.right)
            sums = left[0]+right[0]
            count = left[1]+right[1]

            total = sums+node.val
            count +=1
            if total//count == node.val:
                res[0]+=1
            return (total,count)
        dfs(root)
        return res[0]
