# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        
        res = float("-inf")

        def dfs(tree):
            nonlocal res
            if not tree:
                return 0
            
            left = dfs(tree.left)
            right = dfs(tree.right)
            left = max(0, left)
            right = max(0, right)

            res = max(res, left + right + tree.val)

            return max(left, right) + tree.val
        
        dfs(root)
        return res